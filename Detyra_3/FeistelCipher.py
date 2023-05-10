from SubKeyGenerator import *
from SBoxes import *


class FeistelCipher:

    # works
    def __init__(self, message, key):
        self.__message = message
        self.__subkey_object = SubKeyGenerator(key)
        self.__subkeys = self.__subkey_object.generate()
        print(self.__subkeys)

    # works
    @staticmethod
    def message_to_binary(message):
        binary_message = list()
        for i in message:
            word = bin(ord(i))[2:]
            binary_message.append(FeistelCipher.char_to_8_bit(word))


        return ''.join(binary_message)

        # works
    # This function adds padding to the message to make it 64 blocks
    @staticmethod
    def padding(message):
        difference = 64 - len(message)
        return message + '0'*difference

    # works
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
            blocks.append(FeistelCipher.padding(binary_message[start:step]))
            start = step
            step += 64

        return blocks


    # works
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

    # works
    @staticmethod
    def XOR(word1, word2):
        result = ''
        for i in range(len(word1)):
            result += str(FeistelCipher.xor(word1[i], word2[i]))
        return result

    # works
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

    # works
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

    # works
    @staticmethod
    def Sbox_Access(entry, sbox):
        row = entry[0] + entry[-1]
        column = entry[1:5]

        row = FeistelCipher.binary_to_decimal(row)
        column = FeistelCipher.binary_to_decimal(column)

        return sbox[int(row)][int(column)]

    # works
    @staticmethod
    def get_sbox_output_decimal(binary_list):
        final_list = list()
        for i in range(0, 8):
            final_list.append(FeistelCipher.Sbox_Access(binary_list[i], SBoxes.sboxes_list[i]))
        return final_list

    # works
    @staticmethod
    def get_sbox_binary(list_decimal):
        lista = list()
        for i in range(0, len(list_decimal)):
            lista.append(FeistelCipher.decimal_to_binary(list_decimal[i]))

        return ''.join(lista)

    # works
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

    # works
    @staticmethod
    def feistel_function(message_32bit, subkey_48bit):
        message_48bit = FeistelCipher.P_Box(message_32bit)
        sbox_input = FeistelCipher.XOR(message_48bit, subkey_48bit)
        sbox_input_list = FeistelCipher.slice_number(sbox_input)
        sbox_decimal_list = FeistelCipher.get_sbox_output_decimal(sbox_input_list)
        sbox_binary = FeistelCipher.get_sbox_binary(sbox_decimal_list)

        return FeistelCipher.Straight_PBox(sbox_binary)

    # This function simulates one round of the feistel cipher
    # works
    @staticmethod
    def feistel_round(message, subkey):
        left_part = message[:32]
        right_part = message[32:]
        function_output = FeistelCipher.feistel_function(right_part, subkey)
        new_right_part = FeistelCipher.XOR(left_part, function_output)
        return right_part + new_right_part

    # works
    @staticmethod
    def binary_to_decimal(binary_string):
        decimal_value = 0
        binary_string = str(binary_string)

        binary_string = binary_string[::-1]  # e kthen string mbrapsht

        for i in range(0, len(binary_string)):
            decimal_value += int(binary_string[i]) * (2 ** i)

        return decimal_value


    # works
    @staticmethod
    def decimal_to_binary(decimal_num):
        binary_num = bin(decimal_num)[2:]

        difference = 4 - len(binary_num)
        if (difference > 0):
            binary_num = '0' * difference + binary_num
        else:
            binary_num = binary_num

        return binary_num

    # works
    @staticmethod
    def switch_left_with_right(message):
        left_part = message[:32]
        right_part = message[32:]
        return right_part + left_part

    # works
    @staticmethod
    def char_to_8_bit(char):
        difference = 8 - len(char)
        return '0'*difference + char

    # works
    @staticmethod
    def binary_to_plaintext(binary_string):
        # Split the binary string into 8-bit chunks
        binary_chunks = [binary_string[i:i + 8] for i in range(0, len(binary_string), 8)]

        # Convert each binary chunk to an integer
        int_values = [int(chunk, 2) for chunk in binary_chunks]

        # Convert each integer to its corresponding ASCII character
        plaintext_chars = [chr(value) for value in int_values]

        # Join the plaintext characters together into a string
        plaintext = ''.join(plaintext_chars)

        return plaintext

    def execute(self):
        binary_message = FeistelCipher.message_to_binary(self.__message)
        print("\n\nBinary Message is : ",binary_message)
        binary_message_blocks = FeistelCipher.binary_message_divide(binary_message)
        print("\nBinary in blocks: ",binary_message_blocks)

        #placeholder = binary_message_blocks[0]
        counter = 0
        encrypted_message_blocks = list()
        for block in binary_message_blocks:
            placeholder = binary_message_blocks[counter]
            for i in range(0, 16):
                placeholder = FeistelCipher.feistel_round(placeholder, self.__subkeys[i])
            placeholder = FeistelCipher.switch_left_with_right(placeholder)
            #encrypted_message_blocks.append(FeistelCipher.switch_left_with_right(placeholder))
            encrypted_message_blocks.append(placeholder)
            counter += 1

        binary_string = ''.join(m for m in encrypted_message_blocks)
        print("\nBinary i enkriptuar: ",binary_string)
        output_text = FeistelCipher.binary_to_plaintext(binary_string)
        print("\nTeksti i enkriptuar: ",output_text)

        return output_text

    def execute_d(self):
        binary_message = FeistelCipher.message_to_binary(self.__message)
        print("\n\nBinary Message is : ",binary_message)
        binary_message_blocks = FeistelCipher.binary_message_divide(binary_message)
        print("\nBinary in blocks: ",binary_message_blocks)

        counter  = 0
        # placeholder = binary_message_blocks[0]
        encrypted_message_blocks = list()
        subkeys = self.__subkeys
        subkeys.reverse()
        for block in binary_message_blocks:
            placeholder = binary_message_blocks[counter]
            for i in range(0, 16):
                placeholder = FeistelCipher.feistel_round(placeholder, subkeys[i])
            placeholder = FeistelCipher.switch_left_with_right(placeholder)
            #encrypted_message_blocks.append(FeistelCipher.switch_left_with_right(placeholder))
            encrypted_message_blocks.append(placeholder)
            counter += 1

        binary_string = ''.join(m for m in encrypted_message_blocks)
        print("\nBinary i enkriptuar: ",binary_string)
        output_text = FeistelCipher.binary_to_plaintext(binary_string)
        print("\nTeksti i enkriptuar: ",output_text)

        return output_text
