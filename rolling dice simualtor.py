import random
again=True
while again:
    print(random.randint(1,6))
    another=input("Want to try another time y/n:")
    if another.lower()=="y":
        continue
    else:
        break