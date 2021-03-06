#Week 3 - Python-Challenge Homework Part 2 - PyPoll

# Import the modules/dependencies
import os
import csv

# What are the variables?
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# Path for CSV File
#csvpath = os.path.join('.', 'Documents', 'Data Analytics', 'Week 3', '3 - Python - Homework', 'PyPoll', 'Resources', 'PyPollResources_election_data.csv')
csvpath = os.path.join('Resources', 'PyPollResources_election_data.csv')


#Open & Read the CSV File
with open(csvpath, newline='') as csvfile:

    # CSV Delimiter & Variable holding the content
    csvreader = csv.reader(csvfile,delimiter=',')
    
    # Read the header first - SKIP IF NO HEADER!!
    csv_header = next(csvfile)
    
    # Read each row after the header
    for row in csvreader:
        total_votes = total_votes + 1
    
        # Calculate Total Number of Votes Each Candidate Won
        if (row[2] == "Khan"):
            khan_votes += 1
        elif(row[2] == "Correy"):
            correy_votes += 1
        elif(row[2] == "Li"):
            li_votes += 1
        else:
            otooley_votes += 1
       
    # Calculate Percentage of Votes for each candidate
    khan_percent = khan_votes / total_votes
    correy_percent = correy_votes / total_votes
    li_percent = li_votes / total_votes
    otooley_percent = otooley_votes / total_votes
    
    # Calculating the Winner basef on the popular vote
    winner = max(khan_votes, correy_votes, li_votes, otooley_votes)
    
    if winner == khan_votes:
        winner_name = "Khan"
    elif winner == correy_votes:
        winner_name = "Correy"
    elif winner == li_votes:
        winner_name = "Li"
    else:
        winner_name = "O'Tooley"

# Print Analysis
print(f"Election Results")
print(f"---------------------------")
print(f"Total Votes: {total_votes}")
print(f"---------------------------")
print(f"Kahn: {khan_percent:.3%}({khan_votes})")
print(f"Correy: {correy_percent:.3%}({correy_votes})")
print(f"Li: {li_percent:.3%}({li_votes})")
print(f"O'Tooley: {otooley_percent:.3%}({otooley_votes})")
print(f"---------------------------")
print(f"Winner: {winner_name}")
print(f"---------------------------")

# Specify File To Write To
output_file = os.path.join('Analysis', 'PyPollResources_election_data.txt')

# Open File Using "Write" Mode. Specify The Variable To Hold The Contents
with open(output_file, 'w') as txtfile:

# Write New Data
    txtfile.write(f"Election Results\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Kahn: {khan_percent:.3%}({khan_votes})\n")
    txtfile.write(f"Correy: {correy_percent:.3%}({correy_votes})\n")
    txtfile.write(f"Li: {li_percent:.3%}({li_votes})\n")
    txtfile.write(f"O'Tooley: {otooley_percent:.3%}({otooley_votes})\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Winner: {winner_name}\n")
    txtfile.write(f"---------------------------\n")
