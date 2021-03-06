Sbox = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)

InvSbox = (
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,
)

Rcon = (
    0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40,
    0x80, 0x1B, 0x36, 0x6C, 0xD8, 0xAB, 0x4D, 0x9A,
    0x2F, 0x5E, 0xBC, 0x63, 0xC6, 0x97, 0x35, 0x6A,
    0xD4, 0xB3, 0x7D, 0xFA, 0xEF, 0xC5, 0x91, 0x39,
)

#convert plaintext to 4x4 matrix form
def plaintext_to_matrix(plaintext):
    matrix = [[0 for x in range(4)] for x in range(4)]
    index_x = 0
    index_y = 0
    for i in range(16):
        if(index_y%4 == 0 and index_y != 0):
            index_y = 0
            index_x += 1
        byte = (plaintext >> (8 * (15 - i))) & 0xFF
        matrix[index_x][index_y]= byte
        index_y += 1
    return matrix

#convert hex matrix to text
def matrix2text(matrix):
    text = 0
    for i in range(4):
        for j in range(4):
            calc = (120 - 8 * (4 * i + j))
            text |= (matrix[i][j] << calc)
    return text

#AES byte substitution step
def byte_substitution(plain_matrix):
    for i in range(4):
        for j in range(4):
            plain_matrix[i][j] = Sbox[plain_matrix[i][j]]

#Aes inverse byte substitution step
def inv_byte_substitution(plain_matrix):
    for i in range(4):
        for j in range(4):
            plain_matrix[i][j] = InvSbox[plain_matrix[i][j]]



#AES shift row step
#First row not shifted
#second row shifted left 1 times
#third row shifted left 2 times
#fourth row shifted left 3 times
def shift_rows(matrix):
    
    temp1 = matrix[1][0]
    temp2 = matrix[1][1]
    temp3 = matrix[1][2]
    temp4 = matrix[1][3]

    matrix[1][0] = temp2
    matrix[1][1] = temp3
    matrix[1][2] = temp4
    matrix[1][3] = temp1


    temp1 = matrix[2][0]
    temp2 = matrix[2][1]
    temp3 = matrix[2][2]
    temp4 = matrix[2][3]

    matrix[2][0] = temp3
    matrix[2][1] = temp4
    matrix[2][2] = temp1
    matrix[2][3] = temp2


    temp1 = matrix[3][0]
    temp2 = matrix[3][1]
    temp3 = matrix[3][2]
    temp4 = matrix[3][3]

    matrix[3][0] = temp4
    matrix[3][1] = temp1
    matrix[3][2] = temp2
    matrix[3][3] = temp3

#AES inverse shift
#Same as shift rows just shift right instead of left
def inv_shift_rows(matrix):
    temp1 = matrix[1][0]
    temp2 = matrix[1][1]
    temp3 = matrix[1][2]
    temp4 = matrix[1][3]

    matrix[1][0] = temp4
    matrix[1][1] = temp1
    matrix[1][2] = temp2
    matrix[1][3] = temp3


    temp1 = matrix[2][0]
    temp2 = matrix[2][1]
    temp3 = matrix[2][2]
    temp4 = matrix[2][3]

    matrix[2][0] = temp3
    matrix[2][1] = temp4
    matrix[2][2] = temp1
    matrix[2][3] = temp2


    temp1 = matrix[3][0]
    temp2 = matrix[3][1]
    temp3 = matrix[3][2]
    temp4 = matrix[3][3]

    matrix[3][0] = temp2
    matrix[3][1] = temp3
    matrix[3][2] = temp4
    matrix[3][3] = temp1



# a helper function that I use in mix colm step
def helper_func(a):
    if(a & 0x80):
        return (((a << 1) ^ 0x1B) & 0xFF)
    else:
        return (a << 1)        

# mix colum Xor
def mix_colm(plain_matrix):
    for i in range(4):
        temp1 = plain_matrix[i][0] ^ plain_matrix[i][1] ^ plain_matrix[i][2] ^ plain_matrix[i][3]
        temp2 = plain_matrix[i][0]
        plain_matrix[i][0] ^= temp1 ^ helper_func(plain_matrix[i][0] ^ plain_matrix[i][1])
        plain_matrix[i][1] ^= temp1 ^ helper_func(plain_matrix[i][1] ^ plain_matrix[i][2])
        plain_matrix[i][2] ^= temp1 ^ helper_func(plain_matrix[i][2] ^ plain_matrix[i][3])
        plain_matrix[i][3] ^= temp1 ^ helper_func(plain_matrix[i][3] ^ temp2)


#inverse mix column
def inv_mix_column(plain_matrix):
    for i in range(4):
        u = helper_func(helper_func(plain_matrix[i][0] ^ plain_matrix[i][2]))
        v = helper_func(helper_func(plain_matrix[i][1] ^ plain_matrix[i][3]))
        plain_matrix[i][0] ^= u
        plain_matrix[i][1] ^= v
        plain_matrix[i][2] ^= u
        plain_matrix[i][3] ^= v
    mix_colm(plain_matrix)        


#AES add round key step
# just xor text to corresponding key
def add_round_key(text,key):
    for i in range(4):
        for j in range(4):
            text[i][j] ^= key[i][j]


# expand key to 4*11 element matrix
def key_expand(key_matrix):
    for i in range(4, 4 * 11):
        key_matrix.append([])
        if i % 4 == 0:
            byte = key_matrix[i - 4][0] ^ Sbox[key_matrix[i - 1][1]]  ^ Rcon[int(i / 4)]
            key_matrix[i].append(byte)

            for j in range(1, 4):
                byte = key_matrix[i - 4][j] ^ Sbox[key_matrix[i - 1][(j + 1) % 4]]
                key_matrix[i].append(byte)
        else:
            for j in range(4):
                byte = key_matrix[i - 4][j] ^ key_matrix[i - 1][j]
                key_matrix[i].append(byte)


#encrtyption text by using key
def encryption(text,key):
    text = plaintext_to_matrix(text)
    key_matrix = plaintext_to_matrix(key)
    key_expand(key_matrix)

    add_round_key(text,key_matrix[:4])

    for i in range(1,10):
        byte_substitution(text)
        shift_rows(text)
        mix_colm(text)
        add_round_key(text,key_matrix[4 * i : 4 * i + 4])
    
    byte_substitution(text)
    shift_rows(text)
    add_round_key(text,key_matrix[40:])
    #print(text)
    return matrix2text(text)


#decryption text by using same key that used in encryption step
def decryption(text,key):
    text = plaintext_to_matrix(text)
    key_matrix = plaintext_to_matrix(key)
    key_expand(key_matrix)

    add_round_key(text,key_matrix[40:])
    inv_shift_rows(text)
    inv_byte_substitution(text)

    for i in range(9,0,-1):
        add_round_key(text,key_matrix[4*i:4*i+4])
        inv_mix_column(text)
        inv_shift_rows(text)
        inv_byte_substitution(text)
        
    add_round_key(text,key_matrix[:4])
    return matrix2text(text)


#
def aes_cbc(plaintext,key,initial_vec):
    length = len(str(hex(plaintext)))
    liste = []
    i = 2
    m = 1
    while (i<=(length-32)):
        plaintext_tostr =str(hex(plaintext))[i:(i+32)]
        plaintext_toint = int(plaintext_tostr,16)
        plaintext_toint ^= initial_vec 
        encryption_data = encryption(plaintext_toint,key)
        liste.append(encryption_data)
        

        decryption_data = decryption(encryption_data,key)
        decryption_data ^= initial_vec
        initial_vec = decryption_data
        i += 32
        m += 1

    if(length > i):
            plaintext_tostr =str(hex(plaintext))[i:]
            plaintext_toint = int(plaintext_tostr,16)
            plaintext_toint ^= initial_vec 
            encryption_data = encryption(plaintext_toint,key)
            liste.append(encryption_data)
            

            decryption_data = decryption(encryption_data,key)
            decryption_data ^= initial_vec
            initial_vec = decryption_data
    return liste

def read_file(file):
    with open(file,'rb') as f:
        read_byte = f.read(65536)
        print('Dosya icerigi = {}'.format(read_byte))
        return read_byte
        
def hashing(input):
    val = aes_cbc(input,0x14198a7602f15d45888bc33804cc0578,0x20d57181b656e57d2c578ca494d69b20)
    return val[len(val)-1]


#aes_cbc(plaintext,key,initial_vec)
file = read_file('hash.txt')
file = file[:-34]

converted_hash = int(file.hex(),16)

hash_val = hashing(converted_hash)


print('Hesaplanan Hash value = {}'.format(str(hex(hash_val))))


readf =""
with open('hash.txt','r') as f:
    readf = f.read(65536)


value = int(readf[-34:],16)
print('Dosya sonundaki Hash = {}'.format(str(readf[-34:])))
if(str(hex(hash_val)) == str(readf[-34:])):
    print('Hashler esit.')
else:
    print('Hash degerleri farkli.')