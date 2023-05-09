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

    ##Ky eshte feistel f
    @staticmethod
    def feistel_function(message_32bit, subkey_48bit):
        message_48bit = FeistelCipher.P_Box(message_32bit)
        sbox_input = FeistelCipher.XOR(message_48bit,subkey_48bit)
        sbox_input_list = FeistelCipher.slice_number(sbox_input)
        sbox_decimal_list = FeistelCipher.get_sbox_output_decimal(sbox_input_list)
        sbox_binary = FeistelCipher.get_sbox_binary(sbox_decimal_list)

        return FeistelCipher.Straight_PBox(sbox_binary)

    @staticmethod
    def binary_to_decimal(binary_string):
        decimal_value = 0
        binary_string = str(binary_string)

        binary_string = binary_string[::-1]  # e kthen string mbrapsht

        for i in range(0, len(binary_string)):
            decimal_value += int(binary_string[i]) * (2 ** i)

        return decimal_value

    @staticmethod
    def decimal_to_binary(decimal_num):

        binary_num = bin(decimal_num)
        return binary_num[2:]

    @staticmethod
    def slice_number(binary_number):
        binary_list = list()
        start = 0
        step = 6
        for i in range(0, 8):
            binary_list.append(binary_number[start:step])
            start = step
            step += 6
        return binary_list

    @staticmethod
    def Sbox_Access(entry, sbox):
        row = list()
        column = list()

        row.append(entry[0])
        row.append(entry[len(entry) - 1])

        for i in range(1, len(entry) - 1):
            column.append(entry[i])

        row = FeistelCipher.binary_to_decimal(''.join(row))
        column = FeistelCipher.binary_to_decimal(''.join(column))

        return sbox[row][column]

    @staticmethod
    def get_sbox_output_decimal(binary_list):
        final_list = list()
        for i in range(0, 8):
            final_list.append(FeistelCipher.Sbox_Access(binary_list[i], SBoxes.sboxes_list[i]))
        return final_list


    @staticmethod
    def get_sbox_binary(list_decimal):
        lista = list()
        for i in range(0, len(list_decimal)):
            lista.append(FeistelCipher.decimal_to_binary(list_decimal[i]))

        return ''.join(lista)

    @staticmethod
    def P_Box(message):
        e_table = [
            32,  1,  2,  3,  4,  5,  4,  5,
            6,  7,  8,  9,  8,  9, 10, 11,
            12, 13, 12, 13, 14, 15, 16, 17,
            16, 17, 18, 19, 20, 21, 20, 21,
            22, 23, 24, 25, 24, 25, 26, 27,
            28, 29, 28, 29, 30, 31, 32,  1
        ]
        message_dictionary = SubKeyGenerator.get_index_dictionary(message)
        extended_message = SubKeyGenerator.PC(message_dictionary, e_table)

        return extended_message

    @staticmethod
    def Straight_PBox(message):
        last_pbox = [
            16,  7, 20, 21, 29, 12, 28, 17,
            1, 15, 23, 26,  5, 18, 31, 10,
            2,  8, 24, 14, 32, 27,  3,  9,
            19, 13, 30,  6, 22, 11,  4, 25
        ]
        message_dictionary = SubKeyGenerator.get_index_dictionary(message)
        extended_message = SubKeyGenerator.PC(message_dictionary, last_pbox)

        return extended_message

    @staticmethod
    def xor(a, b):
        if a == '1' and b == '1':
            return '0'
        elif a == '1' and b == '0':
            return '1'
        elif a == '0' and b == '1':
            return '1'
        elif a == '0' and b == '0':
            return '0'

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