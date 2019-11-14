#creating file with 100 lines

from string import ascii_uppercase

with open("bigfile.txt","a") as f:
    for i in range(100):
        f.write(ascii_uppercase+ "\n")
    