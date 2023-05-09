from SubKeyGenerator import *
from SBoxes import *

# 1) E ndajme mesazhin dhe e shenderrojme ne binar, blloqet i ndajme ne 64 bit, te fundit e bejme padding
# 2) Per secilin bllok 64 bitesh, e ndajme pergjysme dhe pjesen e djathte e bartim,
#     ndersa te djathten e bejme expand dhe e bejme xor me subkey, e me pas futet ne SBoxes
# 3) Pasi del nga SBox behet xor me pjesen e majte

# Funksioni P-Box
# Expand 32 -> 48
class FeistelCipher:
    def __init__(self, message, key):
        self.__message = message  # mesazhi
        self.__subkeys = SubKeyGenerator.generate(key)  # lista me 16 subkeys

    @staticmethod
    def message_to_binary(message):
        binary_message = list()
        for i in message:
            binary_message.append(bin(ord(i))[2:])
            #message

        return ''.join(binary_message)


    @staticmethod
    def binary_message_divide(binary_message):
        blocks = list()
        start = 0
        step = 64

        length = len(binary_message)
        limit=0

        while length != 0:
            if(length<64):
                limit +=1
                break
            else:
                length -= 64
                limit += 1

        for i in range(0,limit):
            blocks.append(binary_message[start:step])
            start = step
            step += 64

        return blocks
    # This function adds padding to the message to make it 64 blocks
    @staticmethod
    def padding(message):
        difference = 64 - len(message)
        return message + '0'*difference

    # This function simulates one round of the feistel cipher
    @staticmethod
    def feistel_round(message, subkey):
        left_part = message[:32]
        right_part = message[32:]
        function_output = FeistelCipher.feistel_function(right_part, subkey)
        new_right_part = FeistelCipher.XOR(left_part, function_output)
        return right_part + new_right_part

    @staticmethod
    def feistel_function(message_32bit, subkey_48bit):
        pass

    @staticmethod
    def xor(a, b):
        pass

    @staticmethod
    def XOR(word1, word2):
        result = ''
        for i in range(word1):
            result += FeistelCipher.xor(word1[i], word2[i])
        return result

    @staticmethod
    def switch_left_with_right(message):
        pass

    def encrypt(self):
        pass

msg = FeistelCipher.message_to_binary("Hello Guys")
print(msg)


blocks = FeistelCipher.binary_message_divide(msg)
print(blocks)