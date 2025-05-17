# 結構化專案程式 - function
import random

def game_1():
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

def game_2():
    user = int(input("[0]剪刀[1]石頭[2]布: "))
    computer = random.randint(0, 2)
    data = ["剪刀", "石頭", "布"]
    print("我出的:", data[user])
    print("電腦的:", data[computer])
    
    if (user + 1) % 3 == computer:
        print("電腦贏")
    elif(computer + 1) % 3 == user:
        print("我贏了")
    else:
        print("平手")



while True:
    choice = input("which game do you want to play?")
    if choice == "1":
        game_1()
    elif choice == "2":
        game_2()
    else:
        print("Error, Please enter 1 or 2")
    play = input("Would you like to play again, y/n?")
    if play == "y":
        continue
    else:
        break

