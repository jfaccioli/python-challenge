# Modules
import os
import csv

# Set path for file
dirname = os.path.dirname(__file__)
election_csv = os.path.join(dirname, "Resources", "election_data.csv")

# Define lists
votes = []
vote_numbers = []
candidates = []
candidates_count = []
total_percent = []

# Open the CSV
with open(election_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

# Define header
    header = next(csv_reader)

# Create loop through csv_reader
    for row in csv_reader:

        # Define current_id, add to the votes list, create a variable for the lenght of the votes list
        current_id = (row[0])        
        votes.append(current_id)
        votes_count = len(votes)

        # Create an empty list of unique candidates and adding candidates if not present yet
        current_candidate = row[2]

        if current_candidate not in candidates:
            candidates.append(current_candidate)

        # Create a list to store the number of votes corresponding to the uniques candidates
        vote_numbers.append(current_candidate)

        # Loop through list of unique candidates and add the count of number of votes
    for x in candidates:
        candidates_count.append(vote_numbers.count(x))

        # Calculate percent of vote of a candidate out of total of vote
        total_percent.append(round(vote_numbers.count(x) / votes_count * 100, 3))

    # Winner
    winner = candidates[candidates_count.index(max(candidates_count))]

            
print("Election Results")
print("----------------------")
print(f"Total Votes: {votes_count}")
print("----------------------")
for p in range(len(candidates)):
    print(f'{candidates[p]}: {total_percent[p]}% ({candidates_count[p]})')
print("----------------------")
print(f"Winner: {winner}")
print("----------------------")

# Specify the file to write to
PyPoll_results = os.path.join(dirname, "Analysis", "PyPoll_Results.txt")

# Write the txt file
with open(PyPoll_results, 'w') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("----------------------\n")
    txtfile.write(f"Total Votes: {votes_count}\n")
    txtfile.write("----------------------\n")
    for p in range(len(candidates)):
        txtfile.write(f'{candidates[p]}: {total_percent[p]}% ({candidates_count[p]})\n')
    txtfile.write("----------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("----------------------\n")