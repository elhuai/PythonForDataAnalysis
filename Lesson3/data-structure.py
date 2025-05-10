
#串列資料list
# 相同相關系的資料組合再一起

# tuple
#「使用小括號和逗號」和「使用 tuple()」
# 保存暫時的資料（打包-不能修改）
# 好處： 1.讀取速度比list快  2.佔用空間比較小  3.不輕易修改，資料更安全

# # tuple  與串列 list 的差異 
# tuple「只要建立了，就不能修改內容」。
# tuple 使用「小括號」，串列 list 使用「方括號」。
# 如果 tuple 裡只有一個元素，後方必須加上「逗號」( 多個元素就不用 )。

#物件資料dictionary 
#放多組相關性的資料

students = ["s1","s2","s3"]

stu1 = {"name":"robert",
        "chinese":78,
        "english":98,
        "math":73}

stu2 = {"name":"alice",
        "chinese":72,
        "english":88,
        "math":63}

stu3 = {"name":"jenny",
        "chinese":65,
        "english":78,
        "math":93}

students=[stu1,stu2,stu3]
for i in students:
    print(f"姓名: {i['name']},國文:{i['chinese']},英文:{i['english']},數學:{i['math']}")
