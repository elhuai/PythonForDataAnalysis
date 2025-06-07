
import csv

# 串列型態
with open('個股日成交資訊.csv',encoding='utf-8',newline='') as csvfile:
    reader = csv.reader(csvfile) #會有標題
    stacks1:list[list] = list(reader)
    for i in stacks1:
        print(stacks1.index(i),i)

type(stacks1)
print(stacks1)

# 物件型態
with open('個股日成交資訊.csv',encoding='utf-8',newline='') as csvfile:
    reader = csv.DictReader(csvfile) #會有標題
    # list(reader)
    stacks2:list[dict] = list(reader)
type(stacks2)
print(f"stacks2 共有 {len(stacks2)} 筆資料")