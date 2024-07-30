# PDF Splitter and Encrypter

## Description

This project contains scripts to split a large PDF file into smaller PDFs, each containing two pages, and then encrypt those PDFs with a password. It comprises two main functions:

1. `split_pdf`: Splits a large PDF into smaller PDF files.
2. `encrypt_pdf`: Encrypts the smaller PDF files with a password.

## Prerequisites

Ensure you have the following installed:
- Python 3.x
- PyPDF2 library

To install the PyPDF2 library, run:
```bash
pip install pypdf2
```
 
## Directory Structure

The project directory should be structured as follows:
```bash
project_directory/
│
├── split_encrypt.py
├── payslips.pdf
├── output_pages/           # Directory to store split PDF files
└── encrypted_pages/        # Directory to store encrypted PDF files
```

## Running the Scripts

1. Ensure that the pdf file is in the project directory and file name in the script is changed to that file name
2. Run the split_pdf function to split the large PDF file:
```bash
python page_seperator.py
```
3. Run the `run` function to encrypt the split PDF files:
```bash
python pdf_encryptor.py
```

The split PDF files will be saved in the `output_pages` directory, and the encrypted PDF files will be saved in the `encrypted_pages` directory. Code is documented using docstrings if any changes are needed to be made.

