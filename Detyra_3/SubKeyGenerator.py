class SubKeyGenerator:


    def __init__(self, key):
        self.__key = key
        self.__permuted_key1 = ''
        self.__dictionary_key = dict()
        self.pc1_table = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44,
                     36, 63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20,
                     12, 4]
        self.pc2_table = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2,
                 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]

        self.shift_table = {
            1: 1,
            2: 1,
            3: 2,
            4: 2,
            5: 2,
            6: 2,
            7: 2,
            8: 2,
            9: 1,
            10: 2,
            11: 2,
            12: 2,
            13: 2,
            14: 2,
            15: 2,
            16: 1
        }
        self.__round_key = ''

    def hex_to_binary(self):
        # Convert the hexadecimal string to an integer
        decimal_num = int(self.__key, 16)

        # Convert the decimal number to a binary string
        binary_string = bin(decimal_num)[2:]

        # Pad the binary string with leading zeros if necessary
        num_padding_bits = len(self.__key) * 4 - len(binary_string)
        if num_padding_bits > 0:
            binary_string = '0' * num_padding_bits + binary_string

        return binary_string

    def get_indexes(self):
        for i in range(1, len(self.__key)+1):
            self.__dictionary_key[i] = self.__key[i-1]
    def permute_pc1(self):
        for i in self.pc1_table:
            self.__permuted_key1 += self.__dictionary_key[self.pc1_table]


    @staticmethod
    def shift_left(half_round_key, shamt):
        shifted_string = half_round_key[shamt:] + half_round_key[:shamt]
        return shifted_string
    @staticmethod
    def divide_and_shift(round_key, shamt):
        part1 = round_key[:28]
        part2 = round_key[28:]

        part1 = SubKeyGenerator.shift_left(part1, shamt)
        part2 = SubKeyGenerator.shift_left(part2, shamt)

        shifted_key_joined = part1 + part2

        return shifted_key_joined
    def encrypt(self):
        self.__key = self.hex_to_binary()
        self.get_indexes()
        self.permute_pc1()
        self.__round_key = SubKeyGenerator.divide_and_shift(self.__permuted_key1,)

