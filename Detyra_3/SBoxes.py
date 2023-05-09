from SubKeyGenerator import *

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
        pass

    @staticmethod
    def binary_message_divide(binary_message):
        pass

    @staticmethod
    def padding(message):
        difference = 64 - len(message)
        return message + '0'*difference

    @staticmethod
    def feistel_round(message):
        pass

    @staticmethod
    def feistel_function(message_32bit, subkey_48bit):
        pass

    @staticmethod
    def xor(a, b):
        pass

    @staticmethod
    def switch_left_with_right(message):
        pass

    def encrypt(self):
        pass
