#Version of pypoll

import csv

# Get the path of the CSV file
file_path = 'C://Users//sowmi//Documents//GitHub//kousalya16.github.io//python-challenge//PyPoll//Resources//election_data.csv'  # Replace with the actual file path


def PyPoll(file_path):
        #read the csv file
        with open(file_path, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            header = next(csvreader)# storing the header row.
            data = list(csvreader)

        # Initialize variables
        total_votes = 0
        candidate_votes = {}
        # Loop through the data
        for row in data:
            candidate = row[2]

            # Count total votes
            total_votes += 1

            # Count votes for each candidate
            if candidate in candidate_votes:
                candidate_votes[candidate] += 1
            else:
                candidate_votes[candidate] = 1

        # Calculate the winner
        winner = max(candidate_votes, key=candidate_votes.get)


        result_lines = [
            "Election Results",
            "-------------------------",
            f"Total Votes: {total_votes}",
            "-------------------------"
        ]
        for candidate, votes in candidate_votes.items():
            percentage = (votes / total_votes) * 100
            result_lines.append(f"{candidate}: {percentage:.3f}% ({votes})")
        result_lines.extend([
            "-------------------------",
            f"Winner: {winner}",
            "-------------------------"
        ])

        return result_lines

        
result_lines=PyPoll(file_path)
# Print results
for line in result_lines:
    print(line)

# Save results to a text file
output_file_path = 'C://Users//sowmi//Documents//GitHub//kousalya16.github.io//python-challenge//PyPoll//analysis//election_results.txt'
with open(output_file_path, 'w') as txtfile:
    txtfile.write("\n".join(result_lines))
    
    

#additional test case

print("\n\nConsidering a sample test case with just 15 rows")

test_case_file_path="C://Users//sowmi//Documents//GitHub//kousalya16.github.io//python-challenge//PyPoll//Resources//election_data_few.csv"
test_result_lines=PyPoll(test_case_file_path)

for line in test_result_lines:
    print(line)


