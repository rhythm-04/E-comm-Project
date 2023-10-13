# E-commerce Web Scraping and Data Analysis

This project is a Python-based web scraping application for gathering product information from Amazon and Flipkart and then cleaning and structuring the data for further analysis. Additionally, this project aims to establish an SQL database to store the collected data and visualize it using Power BI.

## Table of Contents
- [Introduction](#introduction)
- [Project Overview](#project-overview)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Future Enhancements](#future-enhancements)
- [License](#license)

## Introduction

Welcome to the E-commerce Web Scraping and Data Analysis project! This project is designed to collect data from popular e-commerce websites, Amazon and Flipkart, using web scraping techniques. The collected data includes product names, URLs, prices, MRPs, ratings, and rating counts. The data is then cleaned and structured using Python's Pandas library to prepare it for analysis.

## Project Overview

### Web Scraping
- The project utilizes Python with Selenium and BeautifulSoup to scrape product information from Amazon and Flipkart.
- Users are prompted to input a search query and the number of pages they wish to scrape.
- The data from Amazon and Flipkart is collected and stored in separate lists for further processing.

### Data Cleaning
- After scraping, the data is cleaned and structured.
- Missing values are handled, and data types are converted to ensure consistency and compatibility for analysis.

### SQL Database
- The next step is to establish an SQL database to store the cleaned data. This database will facilitate data retrieval and reporting.

### Data Visualization
- In the future, the data stored in the SQL database will be analyzed and visualized using Power BI to gain insights and make informed decisions.

## Getting Started

To run the web scraping application, you'll need to have the following installed:
- Python
- Selenium
- BeautifulSoup
- Pandas
- Chrome WebDriver

Ensure that you have the necessary packages installed by running:
```
pip install pandas selenium beautifulsoup4
```

You also need to download the Chrome WebDriver corresponding to your Chrome browser version. You can find it here: [Chrome WebDriver Downloads](https://sites.google.com/chromium.org/driver/)

## Usage

1. Install the required packages as mentioned in the "Getting Started" section.

2. Run the Python script:
```
python e_commerce_scraper.py
```

Follow the on-screen prompts to provide the search query and the number of pages to scrape for both Amazon and Flipkart.

The scraped data will be stored in CSV files with the search query as the filename.

## Future Enhancements

The future plans for this project include:
- Establishing a SQL database using PostgreSQL and Psycopg2 to store the scraped and cleaned data.
- Building data visualizations and dashboards using Power BI to provide insights into the e-commerce data.
- Using Machine Learning to choose the optimum product for the person according to the requirements.  

Stay tuned for updates and improvements!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
