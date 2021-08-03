from binascii import hexlify
from pwn import xor

#Input String and Key
string = "Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"
key = "ICE"

output = hexlify(xor(string,key)).decode('UTF-8')
print(output)

#Output = '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20690a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'
