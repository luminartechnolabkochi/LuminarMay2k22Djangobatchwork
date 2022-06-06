word="hai hai heloo"

words=word.split(" ")#['hello', 'hai', 'hello', 'hai']

wc={} #"hello":2,"hai":2

for w in words: #w="hello","hai","hello,"hai"
    if w in wc:
        wc[w]+=1
    else:
        wc[w]=1
print(wc)

