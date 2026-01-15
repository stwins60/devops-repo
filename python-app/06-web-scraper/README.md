# Web Scraping Application

Python web scraper using BeautifulSoup and Requests for data extraction.

## Features

- HTML parsing
- Data extraction
- CSV export
- Error handling
- Rate limiting

## Project Structure

```
06-web-scraper/
├── src/
│   ├── __init__.py
│   ├── scraper.py
│   ├── parser.py
│   └── exporter.py
├── output/
│   └── .gitkeep
├── config/
│   └── settings.py
├── requirements.txt
└── README.md
```

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python src/scraper.py --url https://example.com --output output/data.csv
```
