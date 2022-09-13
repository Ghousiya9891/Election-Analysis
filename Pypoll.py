import csv
import os

#create a variable to load the file path

file_to_load=os.path.join("Resources","election_results.csv")

# create and assign a variable to store the results in a new file

# file_to_save=os.path.join("analysis","election_analysis.txt")

# open the election results and read the file

with open(file_to_load) as election_data:

    file_reader=csv.reader(election_data)
    headers=next(file_reader)
    print(headers)

    #Print each row in csv file

    #for row in file_reader:
        #print the headers
        #print(row[0])