import function

def main():
    height:int = int(input("身高（cm）?"))
    weight:int = int(input("體重（kg）?"))

    bmi = function.caculate_bmi(height, weight)
    print(bmi)
    print(function.get_result(bmi))

if __name__ == '__main__':
    main()