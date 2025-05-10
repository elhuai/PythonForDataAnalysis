#   多項條件式
scores = input("")
if scores <60:
    print("不及格")
elif scores < 70:
    print("丙")
elif scores < 80:
    print("乙")
elif scores < 90:
    print("甲")
else:
    print("優")

#血壓
presure = 92
# if 80 <= presure  <=120:
# if presure < 80 or presure > 120::
if presure >= 80 and presure <= 120:
    print("正常")
else:
    print("異常")