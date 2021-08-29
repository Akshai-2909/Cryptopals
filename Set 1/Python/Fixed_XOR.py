from pwn import xor
from binascii import hexlify, unhexlify

def xor():   
    string1 = unhxelify('1c0111001f010100061a024b53535009181c' )
    string2 = unhexlify('686974207468652062756c6c277320657965')
    output = hexlify(xor(string1,string2))
    print(output)
    
xor()    

#Output = 746865206b696420646f6e277420706c6179
