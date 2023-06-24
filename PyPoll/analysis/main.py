# import the os and csv modules
import os
import csv
import sys

# create a path to the csv
csvpath = os.path.join('..','Resources','election_data.csv')

#variables and lists
total_votes = 0
unique_candidates = []
candidate_votes = []
vote_percent = []
candidate_list = []

# open and read the csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #skip the header
    csvheader = next(csvreader)
    #loop through csv after header
    for row in csvreader:
        #get total votes
        total_votes += 1
        #make a full candidate list with duplicates
        candidate_list.append(row[2])
    #loop through the candidate list
    for i in set(candidate_list):
        #create unique candidate list
        unique_candidates.append(i)
        #create vote count list per candidate
        v = candidate_list.count(i) 
        candidate_votes.append(v)
        #calculate % of total, round to 3rd decimal, and add to list
        percent = round((v/total_votes)*100, 3)
        vote_percent.append(percent)
    #use max() to get highest amount of candidate votes
    winning_vote_num = max(candidate_votes)
    #use winning vote number to get index of the winner in the unique candidates list
    winner = unique_candidates[candidate_votes.index(winning_vote_num)]
    
    
print("Election Results")
print("-------------------------")
#print total votes
print(f'Total Votes: {total_votes}')
print("-------------------------")

#The percentage and total number of votes each candidate won
for candidate in range(len(unique_candidates)):
    print(f'{unique_candidates[candidate]}: {(vote_percent[candidate])}% ({(candidate_votes[candidate])})')

print("-------------------------")   
#The winner of the election based on popular vote
print(f'{winner}') 
print("-------------------------") 
#print to text file
with open('pypoll_read_me_export.txt','w') as f:
    f.write("Election Results\n")
    f.write("-------------------------\n")
    f.write(f'Total Votes: {total_votes}\n')
    f.write("-------------------------\n")
    for candidate in range(len(unique_candidates)):
        f.write(f'{unique_candidates[candidate]}: {(vote_percent[candidate])}% ({(candidate_votes[candidate])})\n')
    f.write("-------------------------\n")   
    f.write(f'{winner}\n')
    f.write("-------------------------\n")
    





    
    
    
    