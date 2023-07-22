a=int(input("Input a = "))
b=int(input("Input b = "))
output=''
result=''
count=0
with open('ciphertext.txt','r') as c:
      cipher=c.read()
for i in range(len(cipher)):
    if cipher[i].isalpha() and cipher[i].islower():
        num=str(ord(cipher[i])-97)
        output=output+num+''
    elif cipher[i]==' ':
        output=output+'\t'
    elif cipher[i].isalpha() and cipher[i].isupper():
        num=str(ord(cipher[i])-39)
inverse=str((int(output)-b)//a)

#applying microkey
with open('microkey.txt','r') as k:
      key=k.read()
for i in range(len(key)):
    if key[i]=='1':
          count+=1
          inverse = inverse[:i+count] + ' ' + inverse[i+count:]
    else:
        inverse=inverse

#convertin string to list and converting into alphabet
separated_num=inverse.split()
for i in separated_num:
      result=result+str(chr(int(int(i)+97)))
      
with open('decrypted.txt','w') as s:
      s.write(str(result))
print(result)
