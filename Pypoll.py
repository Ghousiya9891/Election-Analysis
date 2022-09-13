import csv
import os

#create a variable to load the file path

file_to_load=os.path.join("Resources","election_results.csv")
# initializing total vote counter
total_votes=0
# creating empty list to add candidate names
candidate_options=[]
# create a empty dictionary (This will store the votes for each candidate as we loop through the rows)
candidate_votes={}

# create and assign a variable to store the results in a new file

# file_to_save=os.path.join("analysis","election_analysis.txt")

# open the election results and read the file

with open(file_to_load) as election_data:

    file_reader=csv.reader(election_data)
       #print the headers
    headers=next(file_reader)
    print(headers)

    #Print total votes row in csv file
    for i in file_reader:
        # Count the total votes
        total_votes=total_votes+1
        # Retrieve the candidates from the file
        candidate_name=i[2]
            
        # To get the unique values (add the name to the list only if the name is not present)
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name]=0
        #Begin tracking the candidate votes
        
          # Add a vote to that candidate's count
        candidate_votes[candidate_name]+=1
    
    
#print the votes    
print(total_votes)

#print the names
print(candidate_options)

#print each candidate votes
print(candidate_votes)

# Determine the percentage of votes for each candidate by looping through the counts.
winning_candidate=""
winning_count=0
winning_percentage=0

for i in candidate_votes:
    votes=candidate_votes[i]
    #Votes for each candidate
    print(f'The number of votes for {i} are {votes}')
    #percentage of votes for each candidate
    vote_percentage=float(votes)/float(total_votes)*100
    print(f'Percentage of votes for {i} are {vote_percentage:.2f}\n')

    #Determining winning candidate and winning votes
    if(votes>winning_count) and (vote_percentage>winning_percentage):
        winning_count=votes
        winning_percentage=vote_percentage
        winning_candidate=i
print(f'The winning candidate is {winning_candidate} with {winning_count} votes and {winning_percentage:.2f} percent of votes')