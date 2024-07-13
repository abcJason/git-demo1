import random

x = random.randint(1, 50)

count = 1
for i in range(5):
    print("-" * 50)
    print(f"第{count}回合")
    y = int(input("1~50猜一個數字:"))
    if x == y:
        print("猜對了!!!")
        print(f"總共{count}回合結束~")
        break
    elif x > y:
        print("猜錯了~~")
        print("猜高一點了")
    else:
        print("猜錯了~~")
        print("猜低一點了")
    count += 1
