# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

pybank = os.path.join("Resources", "budget_data.csv")
#Improved Reading using CSV module

with open(pybank, newline='') as pybank_file:

    # CSV reader specifies delimiter and variable that holds contents
      csvreader = csv.reader(pybank_file, delimiter=',')

      print(csvreader)

    # Read the header row first (skip this step if there is now header)
      csv_header = next(csvreader)
      print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
      for row in csvreader:
          print(row)
