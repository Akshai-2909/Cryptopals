from binascii import unhexlify
import base64
  
def conversion():  
  string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d' #Input String
  string = unhexlify(string)
  output = base64.b64encode(string)
  print(output.decode('UTF-8'))

conversion()

#Output = SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
