#Version of PyBank
import csv

# Read the CSV file
file_path = 'C://Users//sowmi//Documents//GitHub//kousalya16.github.io//python-challenge//PyBank//Resources//budget_data.csv'  #Replace with the actual file path


def PyBank(file_path):

        with open(file_path, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            csvheader= next(csvreader)  # storing the header row
            data = list(csvreader)

        # Initialize variables
        total_months = 0
        net_total = 0
        changes = []
        previous_profit_loss = 0
        greatest_increase = 0
        greatest_decrease = 0

        # Loop through the data
        for i, row in enumerate(data):
            date = row[0]
            profit_loss = int(row[1])

            # Calculate total months and net total
            total_months += 1
            net_total += profit_loss

            # Calculate changes and find greatest increase and decrease
            if i != 0:
                change = profit_loss - previous_profit_loss
                changes.append(change)

                if change > greatest_increase:
                    greatest_increase = change
                    greatest_increase_date = date

                if change < greatest_decrease:
                    greatest_decrease = change
                    greatest_decrease_date = date

            previous_profit_loss = profit_loss

        # Calculate average change
        average_change = sum(changes) / (total_months - 1) if total_months > 1 else 0

        # Prepare the results as strings
        result_lines = [
            "Financial Analysis",
            "------------------",
            f"Total Months: {total_months}",
            f"Net Total: ${net_total}",
            f"Average Change: ${average_change:.2f}",
            f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})",
            f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})"
        ]

        return result_lines

result_lines=PyBank(file_path)
# Print results
for line in result_lines:
    print(line)

# Save results to a text file
output_file_path = 'C://Users//sowmi//Documents//GitHub//kousalya16.github.io//python-challenge//PyBank//analysis//financial_analysis.txt'
with open(output_file_path, 'w') as txtfile:
    txtfile.write("\n".join(result_lines))


#additional test case
print("\n\nConsidering a sample test case with just 15 rows")

test_case_file_path="C://Users//sowmi//Documents//GitHub//kousalya16.github.io//python-challenge//PyBank//Resources//budget_data_few.csv"
test_result_lines=PyBank(test_case_file_path)

for line in test_result_lines:
    print(line)

