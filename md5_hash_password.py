import md5

counter = 1
md5_hash = raw_input("enter the md5 hash:")
wordlist = open('/usr/share/wordlists/rockyou.txt', 'r')

for password in wordlist:
    filemd5 = md5.new(password.strip()).hexdigit()
    print("trying password %d: %s" %(counter,password.strip())
    counter+=1

    if md5_hash == filemd5:
        print("password found: %s" %password)
	break
else: print(password not found.)
