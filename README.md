<div align="center">
    <h1 align="center">QA-Portuguese-small</h2>
    Portuguese preprocessed split from <a href="https://huggingface.co/datasets/clips/mqa">MQA dataset</a> <br>
  This repository contains a dataset of question-answer pairs in Portuguese, uploaded to Hugging Face. The dataset consists of 500,000 rows, with each row containing a question and its corresponding answer in     Portuguese.
</div>


#### Usage

```python
from datasets import load_dataset

data = load_dataset("Jpzinn654/qa-portuguese-small")
```

## Overview

The project involves:

- **Loading** a large question-answer dataset from Hugging Face.
- **Selecting** the first 500,000 rows of the dataset.
- **Saving** the dataset in both CSV and JSON formats.
- **Pushing** the processed dataset to the Hugging Face hub for easy access and sharing.

## Dataset Details

- **Name:** qa-portuguese
- **Source:** Hugging Face
- **Rows:** 500,000 question-answer pairs
- **Languages:** Portuguese

