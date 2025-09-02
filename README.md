# Simple Web Scraper

A Python-based web scraper that extracts remote job listings from RemoteOK.com based on user-provided search terms.

## Features

- Scrapes remote job listings from RemoteOK.com
- Filters jobs based on user-provided search terms
- Extracts key information including:
  - Company name
  - Position title
  - Date posted
  - Job tags
  - Job listing URL
- Saves results to a CSV file for easy analysis

## Prerequisites

- Python 3.x
- Virtual Environment (recommended)

## Required Libraries

```
beautifulsoup4==4.13.4
pandas==2.3.1
requests==2.32.4
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/anuraj/simple-web-scrapper.git
cd simple-web-scrapper
```

2. Create and activate a virtual environment:
```bash
python -m venv .dev
# On Windows
.dev\Scripts\activate
# On Linux/Mac
source .dev/bin/activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Activate the virtual environment if not already activated
2. Run the script:
```bash
python Src/app.py
```
3. Enter the job role or technology you want to search for (e.g., Python, React, DevOps)
4. The script will create a CSV file with the job listings in your current directory

## Output

The script generates a CSV file named `remoteok_[search_term]_jobs.csv` containing the following information for each job:
- Company name
- Position title
- Date posted
- Tags (up to 5)
- Job listing URL

## License

This project is licensed under the terms included in the LICENSE file.

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request