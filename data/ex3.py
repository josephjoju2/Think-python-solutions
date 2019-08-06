import string, pprint,random

def process_file(filename):
    hist={}
    fp=open(filename)
    for line in fp:
        process_line(line,hist)
    return hist

def process_line(line,hist):
    
    line=line.replace('-',' ')
    
    for word in line.split():
        word=word.strip(string.punctuation+string.whitespace)
        word=word.lower()
       
        hist[word]=hist.get(word,0)+1

hist=process_file('emma.txt')
pprint.pprint(hist)


t=[]
for w,f in hist.items():
    t.append((f,w))
t.sort(reverse=True)
for freq,word in t[0:10]:
    print(word+'\t'+str(freq))
 

def random_word(h):
    t=[]
    for word,freq in h.items():
        t.extend([word]*freq) 
    return random.choice(t) 

print(random_word(hist))  
