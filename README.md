# Frequency Balanced Datasets Lead to Better Language Models [![arXiv](https://img.shields.io/badge/arXiv-2407.09732-<COLOR>.svg)](https://aclanthology.org/2023.findings-emnlp.527/)

This repository contains a Python script to analyze the quality of a text corpus, removing sentences that contain only high-frequency words and generating statistics on word distribution.


## Requirements
Before running the script, install the required dependencies:

```bash
pip install -r requirements.txt
```

The main dependencies include:
- `nltk`
- `matplotlib`
- `seaborn`
- `tqdm`
- `numpy`

## Usage
Run the script with the following parameters:

```bash
python quality_corpus.py -l [language] -f [file]
```

### Parameters:
- `-l` / `--language` : Corpus language (`en`, `es`, `ca`).
- `-f` / `--file` : Path to the text corpus file.

### Example execution:
```bash
python quality_corpus.py -l es -f corpus.txt
```

## Output
The script will generate:
1. **A filtered file:** `filtered_corpus.txt` containing the cleaned sentences.
2. **Graphs:** Showing the most common word frequencies.
3. **Statistics:**
   - Mean word frequency.
   - Number of lines before and after filtering.

## Notes
- The corpus must be in **TXT format**, with **one sentence per line**.
- If the corpus is very large, the script processes it in chunks to prevent excessive memory usage.


## Citation
If you find this work helpful, please consider citing:

```bibtex
@inproceedings{zevallos-etal-2023-frequency,
    title = "Frequency Balanced Datasets Lead to Better Language Models",
    author = "Zevallos, Rodolfo  and
      Farr{\'u}s, Mireia  and
      Bel, N{\'u}ria",
    editor = "Bouamor, Houda  and
      Pino, Juan  and
      Bali, Kalika",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2023",
    month = dec,
    year = "2023",
    address = "Singapore",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2023.findings-emnlp.527/",
    doi = "10.18653/v1/2023.findings-emnlp.527",
    pages = "7859--7872",
    abstract = "This paper reports on the experiments aimed to improve our understanding of the role of the amount of data required for training attention-based transformer language models. Specifically, we investigate the impact of reducing the immense amounts of required pre-training data through sampling strategies that identify and reduce high-frequency tokens as different studies have indicated that the existence of very high-frequency tokens in pre-training data might bias learning, causing undesired effects. In this light, we describe our sampling algorithm that iteratively assesses token frequencies and removes sentences that contain still high-frequency tokens, eventually delivering a balanced, linguistically correct dataset. We evaluate the results in terms of model perplexity and fine-tuning linguistic probing tasks, NLP downstream tasks as well as more semantic SuperGlue tasks. The results show that pre-training with the resulting balanced dataset allows reducing up to three times the pre-training data."
}
```
