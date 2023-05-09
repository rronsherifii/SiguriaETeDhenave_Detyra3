from SubKeyGenerator import *

KeyGenerator = SubKeyGenerator('12345678')
subkeys = list()
subkeys = KeyGenerator.generate()

print(subkeys)
