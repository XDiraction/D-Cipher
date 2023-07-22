a=int(input("Input a = "))
b=int(input("Input b = "))
text_withspace=''
text_nospace=''
output=''
micro_key=''
with open('plaintext.txt','r') as p:
      plain=p.read()
#converting alphabet to number
for i in range(len(plain)):
    if plain[i].isalpha() and plain[i].islower():
        num=str(ord(plain[i])-97)
        text_withspace=text_withspace+num+''
        for j in range(len(num)-1):
              micro_key=micro_key+'0'
        micro_key=micro_key+'1'
        
    elif plain[i]==' ':
        text_withspace=text_withspace+' '
    elif plain[i].isalpha() and plain[i].isupper():
        num=str(ord(plain[i])-39)
        text_withspace=text_withspace+num+''
        for j in range(len(num)-1):
              micro_key=micro_key+'0'
        micro_key=micro_key+'1'
        
    else:
        text_withspace=text_withspace

#eliminating the spaces
text_nospace=text_withspace.replace(' ','')

#transforming the number
number=str(a*(int(text_nospace))+b)

#converting the cipher back to alphabet
for i in range(len(number)):
    if number[i].isnumeric():
        letter=chr(int(number[i])+97)
        output=output+letter+''
    else:
        output=output+number[i]+' '
           


#writing the microkey in a file named "microkey.txt"
with open('microkey.txt','w') as k:
      k.write(str(micro_key))

with open('ciphertext.txt','w') as c:
      c.write(str(output))

print(output)

