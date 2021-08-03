from binascii import hexlify , unhexlify
from pwn import xor

charSet= 'ABCDEFGHIJKLMNOPQRSTUVXYWZabcdefghijklmnopqrstuvwxyz'
string= '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736' #Input String
string = unhexlify(string)
length = len(charSet)
def xor():
for i in range(length):
    output = xor(string,ord(charSet[i]))
    
    if(output.decode('UTF-8').isprintable()):
        print(output)
xor()

#Output = b'Cooking MC's like a pound of bacon'
