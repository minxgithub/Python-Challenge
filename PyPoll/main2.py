import os
import csv

# Path to collect data from the Resources folder
poll_csv_path = os.path.join('Resources', 'election_data.csv')

# Read in the CSV file
with open(poll_csv_path, 'r') as csvfile:
    election_data = csv.reader(csvfile, delimiter=',')

    # Read the header row
    header = next(election_data)

    # Creat an empty list for Candidates
    Candidates = []
    
    for row in election_data:
        # Append to update the Candidates list
        Candidates.append(row[2])
        Total_Votes = len(Candidates)
    
    # Create a new list with unique Candidate names
    Candidates_unique = []    
    
    for name in Candidates:
        if name not in Candidates_unique:
            Candidates_unique.append(name)

# Set output1 variable to hold the result title and total number of votes info
output1 = ("Election Results\n"
"----------------------------\n"
f'Total Votes: {Total_Votes}\n'
"----------------------------\n")    
# Print output1 content to terminal
print(output1)

# Specify the path and name of the output file to write to
output_file = os.path.join('Analysis', 'Result2.txt')

# Open the output file using "write" mode
with open(output_file, 'w') as resultfile:
    # Write output1 content to the output file
    resultfile.write(output1)
    
    # Set winner count to 0
    Winner_count = 0
    
    for i in range(len(Candidates_unique)):
        # Calculate the total number and percentage of votes for each candidate
        Number_votes = Candidates.count(Candidates_unique[i])
        Percentage_votes = round(Number_votes/Total_Votes * 100, 5)
        
        # Determine who is the Winner
        if Number_votes > Winner_count:
            Winner_count = Number_votes
            Winner = Candidates_unique[i]
        
        # Print each candidate's name, percentage and total number of votes to terminal
        print(f'{Candidates_unique[i]}: {Percentage_votes}%  ({Number_votes})')
        # Write each candidate's name, percentage and total number of votes to the output file
        resultfile.write(f'{Candidates_unique[i]}: {Percentage_votes}%  ({Number_votes})\n')
    
    # Set output2 variable to hold the winner info
    output2 = ("----------------------------\n"
    f'Winner: {Winner}\n'
    "----------------------------")
    # Print output2 content to terminal
    print(output2)
    # Write output2 content to the output file
    resultfile.write(output2)