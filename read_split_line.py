
f=open("data.txt")

text=f.read().split("\n")
f.close()
print(text)

for l in text:
    print(l)
