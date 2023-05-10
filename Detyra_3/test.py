# sub keys
# Key = 64 bit hex -> binary √
# Gjenru dictionary me indeksa √
# Key 64 bit e kthejme ne 56 bit dhe e bejme PC1 (permes PC1) √
# Key 56 bit, sherben si hyrje per round 1
# Round 1: Key 56 bit ndahet ne dy pjese dhe secila behet shift left (varet) dhe behen join
# Round 2: Key 56 bit nga round 1, ndahet ne dy pjese dhe behet shift left, dhe join
# ...
# Round i: Key 56 bit nga round i-1, ndahet ne dy pjese behet shift left dhe join
# ...
# Per secilin round kemi nje PC2, i cili na i kthen ne 48 bit dhe i ben permute

from FeistelCipher import *
from SubKeyGenerator import *

message = "Ky eshte dekriptimi i bere me algoritmin DES"
key = '133457799BBCDFF1'
subkey1 = '000110110000001011101111111111000111000001110010'

print("16 subkeys generated: ")
feistel = FeistelCipher(message, key)

# mesazhi = feistel.message_to_binary(message)
# print("\nMessage to binary: ", mesazhi)
#
# divided = feistel.binary_message_divide(mesazhi)
# print("\nBinary message in blocks of 64: ", divided)
#
# message32 = divided[0][32:]
# print("\nRight half of message: ",message32)
#
#
# message48 = feistel.P_Box(message32)
# print("Permuted 48 bits of message: ",message48)
#
# xored_msg = feistel.XOR(message48,subkey1)
# print("\nXored 48 bit permute with subkey of round: ",xored_msg)
#
# list_before_sbox = feistel.slice_number(xored_msg)
#
# print("\nList before sbox",list_before_sbox)
#
# sbox_output_decimal = feistel.get_sbox_output_decimal(list_before_sbox)
# print("\nOutput decimal of sboxes is: ", sbox_output_decimal)
#
# sbox_output_binary = feistel.get_sbox_binary(sbox_output_decimal)
# print("\nOutput of sboxes in binary: ",sbox_output_binary)
#
# last_permute = feistel.Straight_PBox(sbox_output_binary)
# print("\nMessage after last permute: ",last_permute)
#
#
# other_way = feistel.feistel_function(message32,subkey1)
# print("\nFeistel function : ",other_way)
#
# round = feistel.feistel_round(mesazhi,subkey1)
#
#
# decimal_val = feistel.binary_to_decimal(subkey1)
# print("\nBinary to decimal: ",decimal_val)
#
# binary_val = feistel.decimal_to_binary(decimal_val)
# print("\nDecimal to binary: ", binary_val)


output = feistel.execute()

feistel2 = FeistelCipher(output,key)
feistel2.execute_d()

