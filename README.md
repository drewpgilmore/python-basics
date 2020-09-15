# Python Summarizer
Simple demonstration of reading a CSV with Python and writing out a text file summary. 

##Example 1: Election Results

##Example 2: Profit/Loss Tracker

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
