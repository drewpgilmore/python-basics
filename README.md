# Python Summarizer
Simple demonstration of reading a CSV with Python and writing out a text file summary. Both examples utilized os and csv modules to iterate through CSV files. 
```python
import os
import csv
```
The same exercise was later run in pandas to demonstrate the increase in efficiency.
```python
import pandas as pd
```
## Example 1: Election Results



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
