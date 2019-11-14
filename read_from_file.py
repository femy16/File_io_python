#opens file data.txt and save a handle to the file in f

f=open("data.txt")
print(type(f))
#Read the entire content of file into text
text=f.readlines()

#print the content of text to console
print(text)
print(type(text))
f.close()
for l in text :
    print(l)
