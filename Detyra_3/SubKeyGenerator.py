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

class SubKeyGenerator:

    def __init__(self, key):
        self.__key = key
        self.pc1_table = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52,
                     44, 36, 63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13,
                     5, 28, 20, 12, 4]
        self.pc2_table = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31,
                     37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]
        self.shift_table = {1: 1, 2: 1, 3: 2, 4: 2, 5: 2, 6: 2, 7: 2, 8: 2, 9: 1, 10: 2, 11: 2, 12: 2, 13: 2, 14: 2, 15: 2,
                       16: 1}

    @staticmethod
    def hex_to_binary(hex_key):
        # Convert the hexadecimal string to an integer
        decimal_num = int(hex_key, 16)
        # Convert the decimal number to a binary string
        binary_string = bin(decimal_num)[2:]
        # Pad the binary string with leading zeros if necessary
        num_padding_bits = len(hex_key) * 4 - len(binary_string)
        if num_padding_bits > 0:
            binary_string = '0' * num_padding_bits + binary_string
        return binary_string

    @staticmethod
    def get_index_dictionary(key):
        key_indexes = dict()
        for i in range(1, len(key)+1):
            key_indexes[i] = key[i-1]
        return key_indexes

    @staticmethod
    def PC1(key_64bits_indexes, permutation_table):
        permuted_key_56bit = ''
        for i in permutation_table:
            permuted_key_56bit += key_64bits_indexes[i]
        return permuted_key_56bit

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

    @staticmethod
    def round(key_56bits, round_number, permutation_table):
        pass

    def generate(self):
        key_binary = SubKeyGenerator.hex_to_binary(self.__key)
        key_64bit_indexes = SubKeyGenerator.get_indexes(key_binary)
        permuted_key_56bits = SubKeyGenerator.PC1(key_64bit_indexes, self.pc1_table)
        subkeys_48bit = list()

