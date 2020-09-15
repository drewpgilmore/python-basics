# Python Summarizer
Simple demonstration of reading a CSV with Python and writing out a text file summary. Both examples utilized os and csv modules to iterate through CSV files. The same exercise was later run in pandas to demonstrate the increase in efficiency.
```python
#learning to drive stick
import os
import csv

#self-driving Tesla
import pandas as pd
```
## Example 1: Election Results
Iterated through 1M+ voting records to simulate tallying data for a select number of candidates. Of course, Pandas .value_counts() made light work of the task. 
```python
file_path = 'Resources/election_data.csv'
election_results_data = pd.read_csv(file_path)
summary_data = election_results_data['Candidate'].value_counts()
print(summary_data)
```

## Example 2: Profit/Loss Tracker
Month-over-month tracking of profit/loss, printing out simple summary for given time period.

```python
print(f'''
    Financial Analysis\n
    Total Months: {len(months)}\n
    Total: ${profitLossRunningTotal}\n
    Average Change: ${avg_change}\n 
    Greatest Increase: {months[Greatest_Increase_Index]} (${str(Greatest_Increase)})\n
    Greatest Decrease: {months[Greatest_Decrease_Index]} (${str(Greatest_Decrease)})
''')
```
