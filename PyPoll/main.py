import os
import csv

pollPath = os.path.join('Resources','election_data.csv')
output_file = os.path.join('analysis','election_results.txt')

candidates = {}

voterList = []
candidates = []

with open(pollPath, encoding="utf8") as pollFile, open(output_file, "w") as summaryFile:
    csvReader = csv.reader(pollFile, delimiter=",")
    headers = next(csvReader)
    for row in csvReader:
        voterList.append(row[0])
        candidates.append(row[2])

    print(f'Elections Results\nTotal Votes: {len(voterList)}\n\n')
    summaryFile.write(f'Elections Results\nTotal Votes: {len(voterList)}\n\n')

    uniqueCandidates = list(set(candidates))
    votes = []
    percentages = []

    for word in uniqueCandidates:       
        voteCount = candidates.count(word)
        votes.append(voteCount)
        percentage = "{:.2%}".format(voteCount/len(candidates))
        percentages.append(percentage)
        print(f'{word}: {percentage} ({voteCount})')
        summaryFile.write(f'{word}: {percentage} ({voteCount})\n')

    print(candidate_summary)
    winner = uniqueCandidates[votes.index(max(votes))]
    print(f'\nWinner: {winner}')
    summaryFile.write(f'\nWinner: {winner}')