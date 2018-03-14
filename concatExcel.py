import pandas as pd

# Read from excel to panda.DataFrame
file = 'output.xlsx'
df = pd.read_excel(file)

# Prune index from file
evenPruned = df[df.index % 2 != 0].ix[:, (x for x in range(0, len(df.columns)) if x != 0)]
oddPruned = df[df.index % 2 != 1].ix[:, (x for x in range(0, len(df.columns)) if x != 0)]

# Set index of both frames from 0 to n
evenPruned.index = pd.RangeIndex(len(evenPruned.index))
oddPruned.index = pd.RangeIndex(len(oddPruned.index))

# Merge DataFrames
finalDf = pd.merge(oddPruned, evenPruned, left_index=True, right_index=True)

# Write to excel
writer = pd.ExcelWriter('output.xlsx')
finalDf.to_excel(writer,'Sheet1')
writer.save()
