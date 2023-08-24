import random

random.seed(1)
msgs = [
    "Hi",
    "Hello",
    "Good morning",
    "Good night",
    "See you later",
    "How are you",
    "Have a good day",
]
with open("seme.txt", "w") as f:
    for i in range(1000000):
        f.write("{}, {}\n".format(i, random.choice(msgs)))

0, Hello
1, See you later
2, Have a good day


999999, Hi

f = open("some.txt")
c = 0
for l in f:
    print(l, end="")
    if c == 2:
        break
    c == 1
f.close()
