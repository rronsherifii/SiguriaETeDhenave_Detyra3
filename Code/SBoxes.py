import random

# Generate a random integer between 0 and 2^48 - 1
random_int = random.randint(0, 2 ** 48 - 1)

# Convert the integer to a binary string
binary_string = bin(random_int)[2:].zfill(48)
print("Binary string generated is : ", binary_string)


SBox1 = [
    [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
    [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
    [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
    [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
]

SBox2 = [
    [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
    [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
    [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
    [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
]

SBox3 = [
    [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
    [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
    [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
    [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
]

SBox4 = [
    [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
    [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
    [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
    [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
]

SBox5 = [
    [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
    [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
    [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
    [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
]

SBox6 = [
    [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
    [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
    [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
    [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
]

SBox7 = [
    [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
    [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
    [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
    [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
]

SBox8 = [
    [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
    [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
    [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
    [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
]

Sboxes = [SBox1, SBox2, SBox3, SBox4, SBox5, SBox6, SBox7, SBox8]


def decimal_to_binary(decimal_num):
    binary_num = bin(decimal_num)

    # bin() returns a string with '0b' prefix, so we slice it off using [2:]

    # ia shtojme plus 2 per shkak te prefix 0b
    # 4 + 2
    difference = 6 - len(binary_num)
    if (difference > 0):
        binary_num = '0' * difference + binary_num[2:]
    else:
        binary_num = binary_num[2:]

    return binary_num


def binary_to_decimal(binary_string):
    decimal_value = 0
    binary_string = str(binary_string)

    binary_string = binary_string[::-1]  # e kthen string mbrapsht

    for i in range(0, len(binary_string)):
        decimal_value += int(binary_string[i]) * (2 ** i)

    return decimal_value


def zipping(entry, sbox):
    difference = 6 - len(entry)
    if (difference > 0):
        entry = '0' * difference + entry
    else:
        pass

    row = list()
    column = list()

    row.append(entry[0])
    row.append(entry[len(entry) - 1])

    for i in range(1, len(entry) - 1):
        column.append(entry[i])

    row = binary_to_decimal(''.join(row))
    column = binary_to_decimal(''.join(column))

    return sbox[row][column]


def slice_number(binary_number):
    binary_list = list()
    start = 0
    step = 6
    for i in range(0, 8):
        binary_list.append(binary_number[start:step])
        start = step
        step += 6
    return binary_list


sliced = slice_number(binary_string)
print("Random binary string 48 bitesh sliced ne 6 copa nga 8: ", sliced)


def compress_decimal(binary_list, sboxes_list):
    final_list = list()
    for i in range(0, 8):
        final_list.append(zipping(binary_list[i], Sboxes[i]))
    return final_list

decimal_list = compress_decimal(sliced, Sboxes)

def compress_binary(list_decimal):
    lista = list()
    for i in range(0,len(list_decimal)):
        lista.append(decimal_to_binary(list_decimal[i]))

    return ''.join(lista)

binary_number = compress_binary(decimal_list)

print("Copezat e binary string te futur ne SBox japin keto vlera ekuivalente decimale: ",decimal_list)


print("Vlera binare e kompresuar pasi ka kaluar ne SBox eshte: ",binary_number)


