import os
import subprocess
import pandas as pd

def main():
    # Prompt for input and output file names
    input_file = input("Enter the path to the input CSV file containing SMILES: ").strip()
    output_file = input("Enter the name for the output CSV file: ").strip()

    # Define the parent directory containing assay subfolders
    parent_dir = "model_wt"

    # Verify input file exists
    if not os.path.isfile(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        return

    # Verify parent directory exists
    if not os.path.isdir(parent_dir):
        print(f"Error: Parent directory '{parent_dir}' not found.")
        return

    # Read the SMILES input file
    try:
        smiles_df = pd.read_csv(input_file)
    except Exception as e:
        print(f"Error reading input file: {e}")
        return

    if smiles_df.shape[1] < 1:
        print("Error: Input file must have at least one column with SMILES.")
        return

    # Force first column to be named "SMILES"
    smiles_column = "SMILES"
    result_df = pd.DataFrame({smiles_column: smiles_df.iloc[:, 0]})

    # Iterate through each assay subfolder
    for assay_name in os.listdir(parent_dir):
        assay_dir = os.path.join(parent_dir, assay_name)
        model_path = os.path.join(assay_dir, "best.pt")

        if not os.path.isdir(assay_dir) or not os.path.isfile(model_path):
            continue  # skip if no model found

        print(f"Running predictions for assay: {assay_name}")

        pred_file = f"pred_{assay_name}.csv"

        # Run Chemprop prediction using GPU 0
        env = os.environ.copy()
        env["CUDA_VISIBLE_DEVICES"] = "0"

        try:
            subprocess.run([
                "chemprop", "predict",
                "--test-path", input_file,
                "--model-paths", model_path,
                "--uncertainty-method", "classification",
                "--preds-path", pred_file
            ], check=True, env=env)
        except subprocess.CalledProcessError as e:
            print(f"Error running Chemprop for assay {assay_name}: {e}")
            continue

        # Read predictions and merge into results
        try:
            pred_df = pd.read_csv(pred_file)
            if pred_df.shape[1] < 2:
                print(f"Warning: Predictions for {assay_name} not found in expected format.")
                continue

            # Add predictions as new column under the assay name
            result_df[assay_name] = pred_df.iloc[:, 1]

            # Remove temporary prediction file
            os.remove(pred_file)

        except Exception as e:
            print(f"Error processing predictions for {assay_name}: {e}")

    # Save final results with SMILES as first column
    result_df.to_csv(output_file, index=False)
    print(f"Prediction matrix saved to {output_file}")

if __name__ == "__main__":
    main()
