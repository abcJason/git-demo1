import random

x = random.randint(1, 50)

print(x)
while x > 0:
    y = int(input("1~50猜一個數字:"))
    if x == y:
        print("猜對了!!!")
        print(x)
        break
    elif x > y:
        print("猜錯了~~")
        print(f"50~{y}")

    else:
        print("猜錯了~~")
        print(f"{y}~50")
