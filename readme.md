The make_preds.py together with the model weights in  model_wt folder can be used to make 
activity classification predictions for compounds of interest.

The model_wt folder consists of model weights produced using the GNN architecture included in the Chemprop package

The make_preds.py file expects a csv file with SMILES strings in one column. Users will also be prompted to pick a name for the output csv file.
If the input file has "N" number of SMILES then the output will be a Matrix of N x 47. 
