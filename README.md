# E-commerce Web Scraping, Data Analysis, and Database Storage

This project is a Python-based web scraping application for gathering product information from Amazon and Flipkart, cleaning and structuring the data, and storing it in a PostgreSQL SQL database. The project is currently in the process of establishing data visualization using Power BI for insights and decision-making.

## Table of Contents
- [Introduction](#introduction)
- [Project Overview](#project-overview)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Future Enhancements](#future-enhancements)
- [License](#license)

## Introduction

Welcome to the E-commerce Web Scraping, Data Analysis, and Database Storage project! This project is designed to collect data from popular e-commerce websites, Amazon and Flipkart, using web scraping techniques. The collected data includes product names, URLs, prices, MRPs, ratings, and rating counts. The data is then cleaned and structured using Python's Pandas library and stored in a PostgreSQL SQL database.

## Project Overview

### Web Scraping
- The project utilizes Python with Selenium and BeautifulSoup to scrape product information from Amazon and Flipkart.
- Users are prompted to input a search query and the number of pages they wish to scrape for both Amazon and Flipkart.
- The scraped data is now cleaned and structured and includes price categories for analysis.

### SQL Database
- The project has successfully established a PostgreSQL SQL database to store the cleaned data from both Amazon and Flipkart.
- The data is stored with additional price categories to facilitate analysis.

### Data Visualization (In Progress)
- In the future, the data stored in the SQL database will be analyzed and visualized using Power BI to gain insights and make informed decisions.

## Getting Started

To run the web scraping application and store data in the SQL database, you'll need to have the following installed:
- Python
- Selenium
- BeautifulSoup
- Pandas
- Chrome WebDriver
- PostgreSQL
- Psycopg2

Ensure that you have the necessary packages installed by running:
```
pip install pandas selenium beautifulsoup4
```

You also need to download the Chrome WebDriver corresponding to your Chrome browser version. You can find it here: [Chrome WebDriver Downloads](https://sites.google.com/chromium.org/driver/)

## Usage

1. Install the required packages as mentioned in the "Getting Started" section.

2. Run the Python script to scrape data and store it in the SQL database:
```
python e_commerce_scraper.py
```

Follow the on-screen prompts to provide the search query and the number of pages to scrape for both Amazon and Flipkart.

The scraped and cleaned data will be stored in the SQL database and the same SQL database will be connected to Power BI for further visualizations.

## Future Enhancements

The project is continuously evolving, with ongoing work in the following areas:

- Building data visualizations and dashboards using Power BI to provide insights into the e-commerce data.
- Using Machine Learning to choose the optimum product for users according to their requirements.

Stay tuned for more updates as the project progresses, and new insights are gained through data visualization and analysis!


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
