import csv

def analyze_financial_data(file_path):
    # Initialize variables for financial analysis
    total_months = 0
    total_profit_losses = 0
    previous_month_profit_losses = 0
    monthly_change_list = []
    greatest_increase = ["", 0]
    greatest_decrease = ["", float("inf")]

    with open(file_path, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        header = next(csvreader)
        for row in csvreader:
            total_months += 1
            total_profit_losses += int(row[1])
            if total_months > 1:
                monthly_change = int(row[1]) - previous_month_profit_losses
                monthly_change_list.append(monthly_change)
                if monthly_change > greatest_increase[1]:
                    greatest_increase[0] = row[0]
                    greatest_increase[1] = monthly_change
                if monthly_change < greatest_decrease[1]:
                    greatest_decrease[0] = row[0]
                    greatest_decrease[1] = monthly_change
            previous_month_profit_losses = int(row[1])
    average_change = sum(monthly_change_list) / len(monthly_change_list)
    financial_analysis = (
        "Financial Analysis\n"
        "----------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: ${total_profit_losses}\n"
        f"Average Change: ${average_change:.2f}\n"
        f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
        f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})"
    )
    print(financial_analysis)  # Print to terminal
    with open('financial_analysis_results.txt', 'w') as textfile:  # Export to text file
        textfile.write(financial_analysis)

def analyze_election_data(file_path):
    # Initialize variables for election analysis
    total_votes = 0
    candidates = {}
    winner = ""
    winner_votes = 0

    with open(file_path, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        header = next(csvreader)
        for row in csvreader:
            total_votes += 1
            candidate_name = row[2]
            if candidate_name not in candidates:
                candidates[candidate_name] = 0
            candidates[candidate_name] += 1
    election_results = "Election Results\n-------------------------\n"
    election_results += f"Total Votes: {total_votes}\n-------------------------\n"
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        election_results += f"{candidate}: {percentage:.3f}% ({votes})\n"
        if votes > winner_votes:
            winner = candidate
            winner_votes = votes
    election_results += "-------------------------\n"
    election_results += f"Winner: {winner}\n-------------------------"
    print(election_results)  # Print to terminal
    with open('election_results.txt', 'w') as textfile:  # Export to text file
        textfile.write(election_results)

# Paths to the CSV files
financial_data_path = 'C:/Users/maria/Downloads/Starter_Code (7)/Starter_Code/PyBank/Resources/budget_data.csv'
election_data_path = 'C:/Users/maria/Downloads/Starter_Code (7)/Starter_Code/PyPoll/Resources/election_data.csv'

# Execute the analyses
analyze_financial_data(financial_data_path)
analyze_election_data(election_data_path)
