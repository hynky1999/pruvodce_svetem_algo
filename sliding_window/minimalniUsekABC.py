alfa = 'abcdefghijklmnopqrstuvwxyz'
alfa_hash = {x:0 for x in alfa}
text = 'abcdefghijklmnopqrstuvwxyz'
alfa_len = 0
start_index = 0
minimal_len = float("inf")
for i,x in enumerate(text):
    if alfa_hash[x] == 0:
        alfa_len += 1
    alfa_hash[x] += 1
    while alfa_len == len(alfa):
        char = text[start_index]
        if alfa_hash[char] == 1:
            alfa_len -= 1
            minimal_len = min(minimal_len,i-start_index+1)
        alfa_hash[char] -= 1
        start_index += 1
print(minimal_len)
    
        
