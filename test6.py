message= input("Enter Text: ")
index=0
while index  < len(message):
    print(chr(ord(message[index])+3), end='')
    index +=1