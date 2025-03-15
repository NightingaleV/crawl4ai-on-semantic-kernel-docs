# Crawler 4 AI

Following script is a web crawler that scrapes data from the website [Crawler 4 AI](https://www.crawler4ai.com/). 
The script's objective is to extract the docs regarding any library to create a chat bot.

## Installation

```
pip install -r requirements.txt
```

### Docker

```
docker build -t crawler4ai .
docker run -it crawler4ai
```

## Usage

```
python _01_crawl_semantic_kernel_docs.py
python _02_pdf_api_docs_to_md.py
```

