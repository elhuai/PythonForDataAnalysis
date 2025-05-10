import random

# 1加到10
total = 0
for i in range(1,11):
    total += i
print(total)


i = 0
amount = 0
while i < 10:
    i += 1
    amount += i
print(amount)

# total_time = 0
# while True:
#     num = int(input("enter a number(if you enter 0, it'll over)"))
#     if num == 0:
#         break
#     total += num 
# print(f"total = {total}")


time = 0
answer = random.randint(1,99)
minNum = 0
maxNum = 99 

while True:
    number = int(input("enter a number"))
    time += 1
    if  number == answer:
        print(f"{number} 猜對了唷，花了{time} 次")
        break
    elif number > answer:
        maxNum = number-1
        print(f"{minNum}~{maxNum},{number} 猜太大了")
    else:
        minNum = number+1
        print(f"{minNum}~{maxNum},{number} 猜太小了")