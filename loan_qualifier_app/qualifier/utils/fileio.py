# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data


def save_csv(csv_output_data, csvpath):
    """Saves a CSV file to the path provided.
    
    Args:
        csv_output_data: The desired data to be saved in th csv.
        csvpath (Path): The desired location and file name for the saved csv file output.
    """
    # Set the output header
    header = ["Lender", "Max Loan Amount", "Max Loan to Value", "Max Debt to Income", "Minimum Credit Score", "Interest Rate"]

    with open(csvpath, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        # Write the header to the CSV file
        csvwriter.writerow(header)
        
        for item in csv_output_data:
            csvwriter.writerow(item)