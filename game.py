import random

x = random.randint(1, 50)

for i in range(5):
    y = int(input("1~50猜一個數字:"))
    if x == y:
        print("猜對了!!!")
        print(x)
        break
    elif x > y:
        print("猜錯了~~")
        print("猜高一點了")
    else:
        print("猜錯了~~")
        print("猜低一點了")

if X != y:
    print(f"答案為{x}")
