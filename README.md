# IMDb Top 250 Movie Rating Scraper

## 1. Project Overview

The IMDb Top 250 Movie Rating Scraper is a Python-based project that attempts to collect movie information from the IMDb website.

It extracts movie titles, release years, and ratings and stores the collected information in a CSV file.

## 2. Objectives

- To learn web scraping using Python.
- To collect movie information automatically.
- To extract movie titles, years, and ratings.
- To organize and store data in CSV format.

## 3. Technologies Used

- **Python** – Main programming language.
- **Playwright** – Browser automation.
- **BeautifulSoup** – HTML parsing and data extraction.
- **Pandas** – Data organization and processing.
- **Regular Expressions** – Identifying years and ratings.
- **CSV** – Storing the collected data.
- **Visual Studio Code** – Code development.

## 4. Features

- Opens the IMDb website using a browser.
- Scrolls through the webpage.
- Attempts to extract movie titles, release years, and ratings.
- Avoids duplicate movie titles.
- Organizes the collected information into a table.
- Saves the results in a CSV file.

## 5. Project Structure

```text
IMDb Movie Rating Scraper/
│
├── imdb_scraper.py
├── imdb_top_250_movies.csv
└── README.md
```

The CSV file is generated when the program runs successfully.

## 6. How It Works

1. Playwright opens the IMDb website.
2. The program scrolls through the webpage.
3. BeautifulSoup reads the available HTML content.
4. Regular expressions help identify years and ratings.
5. Pandas organizes the collected information.
6. The results are saved in a CSV file.

**Workflow:**

IMDb Website → Playwright → BeautifulSoup → Data Processing → Pandas → CSV File

## 7. Installation

Install Python and the required libraries.

Run the following command in the terminal:

```bash
py -m pip install playwright beautifulsoup4 pandas
```

Install the Playwright browser:

```bash
py -m playwright install chromium
```

## 8. How to Run

Open the project folder in Visual Studio Code.

Run the following command in the terminal:

```bash
py imdb_scraper.py
```

The program attempts to collect up to 250 movie records and save the results as `imdb_top_250_movies.csv`.

## 9. Expected Output

The CSV file contains these columns:

| Column | Description |
|---|---|
| Title | Movie title |
| Year | Movie release year |
| Rating | Movie rating |

The program also displays the number of records extracted and the first five rows.

## 10. Advantages

- Reduces manual data collection.
- Organizes movie information.
- Provides practice with Python libraries.
- Helps understand browser automation and web scraping.

## 11. Limitations

- Requires an internet connection.
- Website restrictions may prevent data collection.
- Changes to the webpage may affect extraction.
- Some movie details may be missing or incorrectly extracted.

## 12. Future Enhancements

- Collect additional movie details.
- Add movie search and filtering.
- Improve error handling and data validation.
- Add a web interface.
- Include data visualization.

## 13. Conclusion

This project demonstrates the basic concepts of web scraping and data processing using Python. It provides practical experience with browser automation, HTML parsing, and CSV file handling.

**Note:** The actual number and accuracy of collected records depend on the website response and the extraction code.
