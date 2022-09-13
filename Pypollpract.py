import csv
import os
#  Assign a variable for the file to load using absolute path.

"""""
file_to_load='Resources\election_results.csv'

# Open the election results and read the file.

election_data=open(file_to_load,'r')

# To do: perform analysis.

election_data.close()

# Perform same open operation using with

with open(file_to_load) as file_data:

    print(file_data)
"""    

# opening csv file using os.path.join() function

file_to_load=os.path.join("Resources","election_results.csv")

# Open the election results and read the file.

with open(file_to_load) as election_data:

    #print the file object
    print(election_data)

# Code to write a file to the directory

file_to_save=os.path.join("analysis","election_analysis.txt")

# Using the open() function with the "w" mode we will write data to the file.

outfile=open(file_to_save, 'w')

# Write some data to the file.

outfile.write("Hello World")

# Close the file

outfile.close()

#Using with write to the file

with open(file_to_save,'w') as txtfile:
    #Write some data to the file
    txtfile.write("Counties in the Election\n")
    txtfile.write("------------------------\n")
    txtfile.write("Araphoe\n")
    txtfile.write("Denver\n")
    txtfile.write("Jefferson")  
txtfile.close()





