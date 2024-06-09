# NCBI Data Downloaders

This repository contains two command line tools for downloading data from the NCBI databases. One tool downloads data from the nucleotide database, while the other downloads data from the protein database. Each tool takes a search term and a number of items to download as input, and saves the downloaded data to files.

## Tools

### 1. Nucleotide Database Downloader (`ncbi.py`)

This tool downloads data from the NCBI nucleotide database based on a search term and a specified number of items to download.

### 2. Protein Database Downloader (`ncbi_protein.py`)
This tool downloads data from the NCBI protein database based on a search term and a specified number of items to download. 

#### Usage

```sh
python ncbi.py TERM NUMBER
python ncbi_protein.py TERM NUMBER
```

TERM: The search term for querying the NCBI database.

NUMBER: The maximum number of items to download.

Installation

You can install the required libraries using pip:

```sh
pip install -r requirements.txt
```
