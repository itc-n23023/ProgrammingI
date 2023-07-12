import random

while True:
    kasiramozi = random.choice([chr(ord("a") + i) for i in range(26)])
    print(kasiramozi)
    if kasiramozi == "r":
        break
