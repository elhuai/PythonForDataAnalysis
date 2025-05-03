#input 詢問
name = input("請輸入姓名：")
print(name)

#type() 顯示資料型態
print(type(name))

#python 是動態型別
name = 123
print(type(name))
# name從原本的string變成int

#只有數值型別可以數學運算，但字串和字串可以相加相乘
print(7+3)
print("Hello" + "World")
print("Hello" * 3)


#長方形算法
width = float(input("請輸入長方形的寬："))
height = float(input("請輸入長方形的高："))
area = width * height
print("長方形的面積為：", area)

#
side = float(input("請輸入對邊："))
another_side = float(input("請輸入鄰邊："))
# 斜邊長度 = (對邊^2 + 鄰邊^2)的平方根
hypotenuse = (side ** 2 + another_side ** 2) ** 0.5
# hypotenuse = math.sqrt(side ** 2 + another_side ** 2)
# math.sqrt() 是計算平方根的函數
print("斜邊長度為：", hypotenuse)
