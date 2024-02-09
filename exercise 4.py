Maths =int(input("Maths: "))
if Maths <0 or Maths>100:
    print("Invalid")
English =int(input("English: "))
if English <0 or English >100:
    print("Invalid")
Biology =int(input("Biology: "))
if Biology <0 or Biology >100:
    print("Invalid")
Physics =int(input("Physics: "))
if Physics <0 or Physics >100:
    print("Invalid")


Chemistry =int(input("Chemistry: "))
if Chemistry <0 or Chemistry<100:
    print("Invalid")
sum =int(Maths+English+Biology+Physics+Chemistry)
# print(f"Total Score is{sum}")
# print(f"Average score is {sum/5}")


if sum/5 >=71 and sum/5<=100:
    print("A")
elif sum/5 >=61 and sum/5<=70:
    print("B")
elif sum/5 >=51 and sum/5<=60:
    print("C")
elif sum/5 >=40 and sum/5<=50:
     print("D")
elif sum/5 >=0 and sum/5<=39:
    print("E")
else:
    print("Invalid input")


