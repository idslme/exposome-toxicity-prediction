# Blood Exposome Toxicity Prediction

This repository provides a computational pipeline to predict compound toxicity across **47 Tox21 assays** and **GHS acute oral toxicity** categories. It leverages deep learning models trained using the **Directed Message Passing Neural Network (DMPNN)** architecture from the Chemprop package.

---

## Project Overview

The goal of this project is to enable high-throughput toxicity screening of blood exposome compounds using pre-trained models. The predictions include:

- Binary classification for 47 Tox21 assays
- GHS acute oral toxicity tagging

---

##  Installation

To set up the environment locally, use the provided `environment.yml` file. It contains all dependencies needed to run the prediction pipeline.

```bash
conda env create -f environment.yml
conda activate chemprop_env
chemprop --help
python make_preds.py

```

This project was developed and tested using Conda. While Conda is recommended for setup, a pip-compatible requirements.txt is also included.

---

## Usage

The make_preds.py script can be used to run the toxicity classification predictions as follows:

```bash
python make_preds.py input_file.csv output_file.csv
```

The script will prompt users to select 2 files
(1) A list of SMILES in a .csv file format with a single column of SMILES string 
(2) Name for an output .csv file which will contain bioactivity predictions from 47 assays as well as GHS acute oral toxicity classification

For ease of use and minimal local setup, all calculations can be run directly via the following Google Colab note book:
https://colab.research.google.com/drive/1bqjZ_ap2TBZrRWik5qrSr2AvZzngJEW4#scrollTo=au4ebqnK9-Kw
