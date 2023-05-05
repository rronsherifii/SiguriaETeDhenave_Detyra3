# remove 8th parity bits //done
# pc1 for keys based on table
# divide key in two parts, shift the parts based on the round
# bits that are shifted left in the beginning are appended at the end of the part of the key
# Concatenate the two parts for each round
# for each of 16 subkeys, apply pc2 based on specified table like in pc1
# win 16 subkeys of des

import random

# lista index_list_1 permban vlerat nga 1 deri ne 64 per indekset e anetareve, pa perfshire bitat e paritetit
index_list_1 = list()

# lista index_list_2 permban vlerat nga 1 deri ne 56 per celesin e kompresuar pas pc1
index_list_2 = list()


# funksioni poshte gjeneron nje celes te cfaredoshem 64 bitesh
def generate_binary_key():
    # Generate a random integer between 0 and 2^48 - 1
    random_int = random.randint(0, 2 ** 64 - 1)

    # Convert the integer to a binary string
    binary_string = bin(random_int)[2:].zfill(64)

    return binary_string


def remove_parity_bits(binary_key):
    new_binary_key = list()

    for i in range(0, len(binary_key)):
        if ((i + 1) % 8 == 0):
            pass
        else:
            index_list_1.append(i + 1)
            new_binary_key.append(binary_key[i])
    return ''.join(new_binary_key)


pc1_table = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36,
             63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]

pc2_table = [
    14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]

# e mbushim matricen me subkeys te shiftuar njera pas tjetres. Pasi subkey i ardhshem varet nga ai paraprak
# na duhet te perdorim rekursion ashtu qe ne fund futet celesi i shiftuar si hyrje per krijimin e celesit te ri
# ne fund te cdo shiftimi ruajme celesin ne matrice
subkey_matrix = []


def permutate_pc1(pc1, binary_key_56):
    permutated_key = list()

    for i in range(0, len(pc1)):
        for j in range(0, len(index_list_1)):
            if (pc1[i] == index_list_1[j]):
                permutated_key.append(binary_key_56[j])

    return ''.join(permutated_key)


def shift_left(binary_string, shamt):
    new_index = shamt % len(binary_string)

    shifted_string = binary_string[new_index:] + binary_string[:new_index]

    return shifted_string


shift_table = {
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


def divide_and_shift(subkey_56, shamt):
    part1 = subkey_56[:28]
    part2 = subkey_56[28:]

    part1 = shift_left(part1, shamt)
    part2 = shift_left(part2, shamt)

    shifted_key_joined = part1 + part2

    # pas shiftimit indekso anetaret nga 1 deri ne 56, keto indekse na duhen per perdorimin e pc2
    if len(index_list_2) == 56:
        pass
    else:
        for i in range(0, len(shifted_key_joined)):
            index_list_2.append(i + 1)

    return shifted_key_joined


def permute_pc2(pc2, binary_string):
    # shendrrimi i celesit 56 bitesh te shiftuar e permutuar ne 48 bitesh
    final_subkey = list()

    for i in range(0, len(pc2_table)):
        for j in range(0, len(index_list_2)):
            if pc2[i] == index_list_2[j]:
                final_subkey.append(binary_string[j])

    return ''.join(final_subkey)


def main_shifting(key_56_after_pc1):
    round_subkey = list()

    for i in range(0, 16):
        if i == 0:
            key_to_add = divide_and_shift(key_56_after_pc1, shift_table[1])
            round_subkey.append(key_to_add)
            subkey_matrix.append(key_to_add)
        else:
            key_to_add = divide_and_shift(round_subkey[i - 1], shift_table[i + 1])
            round_subkey.append(key_to_add)
            subkey_matrix.append(key_to_add)

    return subkey_matrix


def final_subkeys_pc2(shifted_16_subkeys):
    final_des_subkeys = list()
    for i in range(0, len(shifted_16_subkeys)):
        round_subkey = permute_pc2(pc2_table, shifted_16_subkeys[i])
        final_des_subkeys.append(round_subkey)

    return final_des_subkeys


binary_key_64 = generate_binary_key()
print("Binary key generated is : ", binary_key_64)

new = remove_parity_bits(binary_key_64)
print("compressed key is: ", new)

permute = permutate_pc1(pc1_table, new)
print("Permuted key is:", permute)

print("Tash marrim celesin e permutuar pas pc1 56 bitesh dhe gjenerojme 16 subcelesa te shiftuar")
shifted_keys = main_shifting(permute)
print("Celesat e shiftuar jane: ")
for i in range(0, len(shifted_keys)):
    print(shifted_keys[i] + "\n")

print("Si fund, pasi cdo celes hyn neper pc2, subkeys final per cdo round jane:")
final_subkeys = final_subkeys_pc2(shifted_keys)
for i in range(0, len(final_subkeys)):
    print("Key i roundit ", i, " eshte: ", final_subkeys[i])
