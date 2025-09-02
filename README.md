# Blood Exposome Toxicity Prediction

This repository provides a computational pipeline to predict compound toxicity across **47 Tox21 assays** and **GHS acute oral toxicity** categories. It leverages deep learning models trained using the **Directed Message Passing Neural Network (DMPNN)** architecture from the Chemprop package.

---

## Project Overview

The goal of this project is to enable high-throughput toxicity screening of blood exposome compounds using pre-trained models. The predictions include:

- Binary classification for 47 Tox21 assays
- GHS acute oral toxicity tagging

---

##  Installation

To set up the environment locally, use the provided `requirements.txt` file. It contains all dependencies needed to run the prediction pipeline.

```bash
# Create a new conda environment
conda create --name tox_pred_env python=3.8

# Activate the environment
conda activate tox_pred_env
# Install dependencies
pip install -r requirements.txt

```

---

## Usage

The make_preds.py script can be used to run the toxicity classification predictions as follows:

```bash
python make_preds.py input_file.csv output_file.csv
```

The script will prompt users to select 2 files
(1) A list of SMILES in a .csv file format with a single column of SMILES string 
(2) Name for an output .csv file which will contain bioactivity predictions from 47 assays as well as GHS acute oral toxicity classification
