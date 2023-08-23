# Python Challenge: PyBank and PyPoll
# Python Challenge: PyBank and PyPoll

## Project Description

Welcome to the Python Challenge: PyBank and PyPoll! This project involves creating Python scripts to analyze financial and election data, showcasing your data processing and analysis skills. The two assignments, PyBank and PyPoll, require you to process CSV files, perform calculations, and generate insightful reports. By completing these assignments, you'll demonstrate your ability to extract meaningful information from data and present it clearly.

## PyBank

The PyBank assignment focuses on analyzing financial records to gain insights into the company's financial performance. The dataset, `budget_data.csv`, contains two columns: "Date" and "Profit/Losses". Your task is to develop a Python script that calculates the following key metrics:

1. **Total Months:** Calculate the total number of months included in the dataset.
2. **Net Total:** Determine the net total amount of "Profit/Losses" over the entire period.
3. **Average Change:** Calculate the changes in "Profit/Losses" over the entire period, and then compute the average of those changes.
4. **Greatest Increase:** Identify the greatest increase in profits (date and amount) over the entire period.
5. **Greatest Decrease:** Identify the greatest decrease in profits (date and amount) over the entire period.

The final analysis is both printed to the terminal and exported to a text file named `financial_analysis.txt`.

## PyPoll

The PyPoll assignment focuses on modernizing the vote-counting process for a small, rural town. The provided dataset, `election_data.csv`, includes columns for "Voter ID", "County", and "Candidate". Your task is to develop a Python script that calculates the following election-related insights:

1. **Total Votes:** Calculate the total number of votes cast in the election.
2. **Candidates List:** Create a list of candidates who received votes.
3. **Percentage and Total Votes:** Calculate the percentage of votes each candidate won and determine the total number of votes each candidate received.
4. **Winner Determination:** Identify the winner of the election based on popular vote.

The election analysis is presented in the terminal and exported to a text file named `election_results.txt`.

## Python `csv` Module

Both the PyBank and PyPoll modules utilize the Python `csv` module for efficient processing of CSV files. The module simplifies tasks such as reading data, iterating through rows and columns, and extracting relevant information. It's an essential tool for handling structured data in CSV format.

## Accessing the Files

To access the files in this GitHub repository and explore the PyBank and PyPoll assignments:

1. **Clone the Repository:** Start by cloning the repository to your local machine. Open a terminal or command prompt and use the following command:
                         git clone <repository_url>

Replace `<repository_url>` with the actual URL of your GitHub repository.

2. **Navigate to Assignment Folders:**
- **PyBank:** Navigate to the `PyBank` folder. This folder contains the Python script `main.py` for the PyBank assignment.
  - Location: `python-challenge/PyBank/`
- **PyPoll:** Navigate to the `PyPoll` folder. This folder contains the Python script `main.py` for the PyPoll assignment.
  - Location: `python-challenge/PyPoll/`

3. **CSV Data and Analysis Results:**
- **Resources Folder:** Inside each assignment folder, you'll find a `Resources` folder that contains the CSV data file (`budget_data.csv` for PyBank and `election_data.csv` for PyPoll).
  - Location: `python-challenge/PyBank/Resources/` and `python-challenge/PyPoll/Resources/`
- **Analysis Folder:** The analysis results, such as the financial analysis report for PyBank and the election results for PyPoll, are saved in the `analysis` folder within each assignment folder.
  - Location: `python-challenge/PyBank/analysis/` and `python-challenge/PyPoll/analysis/`

4. **Running the Scripts:**
- Open a terminal or command prompt and navigate to the respective assignment folder (`PyBank` or `PyPoll`).
- Run the script using the following command:

  ```
  python main.py
  ```

This will execute the script and display the analysis in the terminal.
