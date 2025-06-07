import pandas as pd
import numpy as np
import csv

with open('個股日成交資訊.csv',encoding='utf-8',newline='') as csvfile:
    reader = csv.reader(csvfile) #會有標題
    stacks:list[list] = list(reader)

df1 = pd.DataFrame(stacks)
df1.to_excel("個股日成交資訊.xlsx",sheet_name="第一頁",index=False)

rf = pd.read_excel("個股日成交資訊.xlsx")
print(rf.tail())