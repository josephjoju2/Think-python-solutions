import string
line="hey, how are u _maddy?"
newline=""
for word in line.split():
    word=word.strip(string.punctuation+string.whitespace+'-')
    word=word.lower()+" "
    newline+=word
    
print(line)
print(newline)
