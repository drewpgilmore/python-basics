import pandas as pd

file_path = 'Resources/election_data.csv'

election_results_data = pd.read_csv(file_path)

summary_data = election_results_data['Candidate'].value_counts()

print(summary_data)



