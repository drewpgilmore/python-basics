import os
import csv

pollPath = os.path.join('..','Resources','election_data.csv')

voterList = []
candidates = []

with open(pollPath, encoding="utf8") as pollFile:
    csvReader = csv.reader(pollFile, delimiter=",")
    headers = next(csvReader)
    for row in csvReader:
        voterList.append(row[0])
        candidates.append(row[2])

    print("Elections Results")
    print("-------------------------")
    print("Total Votes: " + str(len(voterList)))
    print("-------------------------")

    uniqueCandidates = list(set(candidates))
    votes = []
    percentages = []

    for word in uniqueCandidates:
        voteCount = candidates.count(word)
        votes.append(voteCount)
        percentage = voteCount/len(candidates)
        percentages.append(percentage)
        print(word + ": " + str("{:.2%}".format(percentage)) + " (" + str(voteCount) + ")")
    
    print("-------------------------")
     
    winner = uniqueCandidates[votes.index(max(votes))]
    print("Winner: " + winner)
    print("-------------------------")