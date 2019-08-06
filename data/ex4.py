suffix_map={}
prefix=()
line='heyy baby, how are you..'

def start():
    for word in line.split():
        #order=2
        process_word(word,order=2)

def process_word(word, order):
    global prefix
    if len(prefix)<order:
        prefix+=(word,)
        return
    
    try:
        suffix_map[prefix].append(word)
    except:
        suffix_map[prefix]=[word]

start()
print(prefix)
print(suffix_map)
