# PyPoll Roadmap

import csv
import os

# Assign a variable for the file to load and save, and join the path in the os
file_to_load = os.path.join('election_results.csv')
file_to_save = os.path.join('election_analysis.txt')

# initialize total vote counter
total_votes = 0

# declare counties
county = []
county_votes = {}
lg_county_turnout = ""
big_county_votes = 0

# declare candidate options and votes
candidate_options = []
candidate_votes = {}

# declare winning candidate outputs
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    headers = next(file_reader)

    for row in file_reader:
        # add to total vote count
        total_votes += 1

        # print candidate name from each row
        candidate_name = row[2]

        # If candidate name does not match any existing candidate...
        if candidate_name not in candidate_options:

            # add the candidate name from index 2 to the created list
            candidate_options.append(candidate_name)

            # begin tallying each candidate's votes; key is candidate name, integer the value
            candidate_votes[candidate_name] = 0

        #If candidate's name appears in row, add to their vote count
        candidate_votes[candidate_name] += 1

        # Save to txt file


with open(file_to_save, "w") as txt_file:
    candidate_votes[candidate_name] +=1
    election_results = (
        f"\nElection Resutls\n"
        f"------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"------------------------\n")
    print(election_results, end="")

    txt_file.write(election_results)

    for candidate_name in candidate_votes:

        #retrieve votes for candidate
        votes = candidate_votes[candidate_name]

        # calculate % of votes for the candidate
        vote_percentage = (votes) / (total_votes) * 100

        candidate_results= (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        print(candidate_results)

        txt_file.write(candidate_results)

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

        winning_candidate_summary = (
        f"--------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"--------------------------\n")

print(winning_candidate_summary)
txt_file.write(election_results)

    

    