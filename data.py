import pandas as pd
import numpy as np



data=pd.read_csv("data.csv")
# print(data)
value=[]
user=(input("data with seprate coma" )).split(",")
for i in user:
    row_index, column_index = np.where(data ==int(i))
    value.append((f"number is :{i} is row={row_index},column={column_index}"))
print(value)