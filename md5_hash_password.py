import hashlib

pash_hash = input('md5_hash:')
wordlist = open(/usr/share/wordlists/rockyou.txt,"r")

for words in wordlist   
    enc_word = word.encode('utf-8')
    
digest = hashlib.md5(enc_word.strip()).hexdigest()

if digest = pash_hash
    print('password found')
    print('password'+word)
    flag = 1
    break

if flag = 0
    print('password not in list')
