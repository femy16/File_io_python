import re
import collections 

with open("1155-0.txt") as f:
    text=f.read().lower()
    # words=text.split(" ")
    words=re.findall("\w+",text)
    #Filter words and keep only those with 5 letter or more
    long_words1=[]
    for word in words:
        if len(word)>=5:
            long_words1.append(word)
# long_words2=[word for word in words if len(word)>=5]      
# unique_words=set(words)

word_count=collections.Counter(long_words1)
print(word_count["a"])
top_10= word_count.most_common(5)

print(top_10)
# print(len(words))
# print(len(unique_words))
