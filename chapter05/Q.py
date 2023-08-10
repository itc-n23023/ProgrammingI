s1 = "{:>4s}{:>4s}{:>4s}{:>4s}{:>4s}\033[32m{:>4s}\033[0m\033[31m{:>4s}\033[0m".format(
    "Mom", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"
)
s1 += "\n"
s2 = "{:4s}".format(" ")
for i in range(1, 32):
    if i % 7 == 5 or i % 7 == 6:
        s2 += "\033[32m{:>4s}\033[0m".format(str(i))
    else:
        s2 += "{:>4s}".format(str(i))
    if i % 7 == 0:
        s2 += "\n"
s1 += s2
print(s1)
