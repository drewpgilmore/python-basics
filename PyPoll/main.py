import os
import csv

poll_path = os.path.join('Resources','election_data.csv')
output_file = os.path.join('analysis','election_results.txt')

voter_list = []
candidates = []

with open(poll_path, encoding="utf8") as poll_file, open(output_file, "w") as summary_file:
    csv_reader = csv.reader(poll_file, delimiter=",")
    headers = next(csv_reader)
    for row in csv_reader:
        voter_list.append(row[0])
        candidates.append(row[2])

    print(f'''
    Elections Results\n
    Total Votes: {len(voter_list)}\n
    ''')
    
    summary_file.write(f'Elections Results\nTotal Votes: {len(voter_list)}\n\n')

    unique_candidates = list(set(candidates))
    votes = []
    percentages = []

    for word in unique_candidates:       
        vote_count = candidates.count(word)
        votes.append(vote_count)
        percentage = "{:.2%}".format(vote_count/len(candidates))
        percentages.append(percentage)
        print(f'{word}: {percentage} ({vote_count})')
        summary_file.write(f'{word}: {percentage} ({vote_count})\n')

    winner = unique_candidates[votes.index(max(votes))]
    print(f'Winner: {winner}')
    summary_file.write(f'Winner: {winner}')