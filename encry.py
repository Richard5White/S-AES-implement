import numpy as np

#异或
def xor(arr1, arr2):
    
    return np.bitwise_xor(arr1, arr2)
#列混淆
def multiply(n,round_part):
    a=10;b=11;c=12;d=13;e=14;f=15
    xBOX = np.array([ [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a, b, c, d, e, f],
                      [0, 2, 4, 6, 8, a, c, e, 3, 1, 7, 5, b, 9, f, d],
                      [0, 3, 6, 5, c, f, a, 9, b, 8, d, e, 7, 4, 1, 2],
                      [0, 4, 8, c, 3, 7, b, f, 6, 2, e, a, 5, 1, d, 9],
                      [0, 5, a, f, 7, 2, d, 8, e, b, 4, 1, 9, c, 3, 6],
                      [0, 6, c, a, b, d, 7, 1, 5, 3, 9, f, e, 8, 2, 4],
                      [0, 7, e, 9, f, 8, 1, 6, d, a, 3, 4, 2, 5, c, b],
                      [0, 8, 3, b, 6, e, 5, d, c, 4, f, 7, a, 2, 9, 1],
                      [0, 9, 1, 8, 2, b, 3, a, 4, d, 5, c, 6, f, 7, e],
                      [0, a, 7, d, e, 4, 9, 3, f, 5, 8, 2, 1, b, 6, c],
                      [0, b, 5, e, a, 1, f, 4, 7, c, 2, 9, d, 6, 8, 3],
                      [0, c, b, 7, 5, 9, e, 2, a, 6, 1, d, f, 3, 4, 8],
                      [0, d, 9, 4, 1, c, 8, 5, 2, f, b, 6, 3, e, a, 7],
                      [0, e, f, 1, d, 3, 2, c, 9, 7, 6, 8, 4, a, b, 5],
                      [0, f, d, 2, 9, 6, 4, b, 1, e, c, 3, 8, 7, 5, a]])
    round_part_2 = ''.join(map(str, round_part))
    round_part_10=int(round_part_2,2)
    # 找到对应的运算值
    Sii = xBOX[n][round_part_10]
    S_mult= [int(b) for b in "{0:04b}".format(Sii)]

    return S_mult

#s盒置换
def s_box(w):
    
    left_half = w[4:]
    right_half = w[:4]
    SBOX = np.array([[9, 4, 10, 11],
                      [13, 1, 8, 5],
                      [6, 2, 0, 3],
                      [12, 14, 15, 7]])

    left_half1 = [left_half[0], left_half[1]]
    left_half2 = [left_half[2], left_half[3]]
    right_half1 = [right_half[0], right_half[1]]
    right_half2 = [right_half[2], right_half[3]]

    left_str1 = ''.join(map(str, left_half1))
    left_str2 = ''.join(map(str, left_half2))
    right_str1 = ''.join(map(str, right_half1))
    right_str2 = ''.join(map(str, right_half2))
    # 然后将每组二进制数转化为十进制数，也就是 S 盒中的行列索引
    left_decimal1 = int(left_str1,2) 
    left_decimal2 = int(left_str2, 2) 
    right_decimal1 = int(right_str1,2) 
    right_decimal2 = int(right_str2, 2)
    # 找到对应的 s_left 值
    s_left = SBOX[left_decimal1][left_decimal2]
    s_right = SBOX[right_decimal1][right_decimal2]
    # 将 s_left 转换为两个bit，存在 s_left_1 中
    s_left_1 = [int(b) for b in "{0:04b}".format(s_left)]
    s_right_1=[int(b) for b in "{0:04b}".format(s_right)]
    # 将 s_left_1 和 s_right_1 拼接成一个长度为8的二进制数
    F1 = s_left_1 + s_right_1

    return np.array(F1)

#s盒置换
def s_box1(round_part):
    
    SBOX1 = np.array([[9, 4, 10, 11],
                      [13, 1, 8, 5],
                      [6, 2, 0, 3],
                      [12, 14, 15, 7]])

    round_part1 = [round_part[0], round_part[1]]
    round_part2 = [round_part[2], round_part[3]]


    left_str1 = ''.join(map(str, round_part1))
    left_str2 = ''.join(map(str, round_part2))

    # 然后将每组二进制数转化为十进制数，也就是 S 盒中的行列索引
    round_part_decimal1 = int(left_str1,2) 
    round_part_decimal2 = int(left_str2, 2) 

    round_part_s = SBOX1[round_part_decimal1][round_part_decimal2]
    round_part_s11= [int(b) for b in "{0:04b}".format(round_part_s)]
    F1 = round_part_s11

    return np.array(F1)

#逆s盒
def s_box2(round_part):
    
    SBOX2 = np.array([[10, 5, 9, 11],
                      [1, 7, 8, 15],
                      [6, 0, 2, 3],
                      [12, 4, 13, 14]])

    round_part1 = [round_part[0], round_part[1]]
    round_part2 = [round_part[2], round_part[3]]


    left_str1 = ''.join(map(str, round_part1))
    left_str2 = ''.join(map(str, round_part2))

    # 然后将每组二进制数转化为十进制数，也就是 S 盒中的行列索引
    round_part_decimal1 = int(left_str1,2) 
    round_part_decimal2 = int(left_str2, 2) 

    round_part_s = SBOX2[round_part_decimal1][round_part_decimal2]
    round_part_s11= [int(b) for b in "{0:04b}".format(round_part_s)]
    F1 = round_part_s11

    return np.array(F1)

#字符处理
def character_process(kerOrtext):
    kerOrtext_ascii1 = ord(kerOrtext[0])
    kerOrtext_ascii2 = ord(kerOrtext[1])
    kerOrtext_binary1 = format(kerOrtext_ascii1, '08b')# 将密钥转化为16bit的二进制字符串
    kerOrtext_binary2 = format(kerOrtext_ascii2, '08b')    
    kerOrtext1 = [int(bit) for bit in kerOrtext_binary1]
    kerOrtext2= [int(bit) for bit in kerOrtext_binary2]
    kerOrtext_arr=np.concatenate((kerOrtext1,kerOrtext2))
    kerOrtext=[int(bit) for bit in kerOrtext_arr]

    return kerOrtext

#密钥处理
def key_process(key):
    RC1=[1,0,0,0,0,0,0,0]
    RC2=[0,0,1,1,0,0,0,0]
    #密钥侧处理
    w0=key[0:8]
    w1=key[8:16]
    g1=xor(s_box(w1),RC1)
    w2=xor(w0,g1)
    w3=xor(w1,w2)
    g2=xor(s_box(w3),RC2)
    w4=xor(w2,g2)
    w5=xor(w3,w4)
    key1=key
    key2=np.concatenate((w2,w3))
    key3=np.concatenate((w4,w5))

    return key1,key2,key3

#加密函数
def encrypt(plaintext,key):

    key1,key2,key3=key_process(key)
    round_key_addition=xor(plaintext,key1)
    #第一轮
    round_part00=round_key_addition[:4]
    round_part10=round_key_addition[4:8]
    round_part01=round_key_addition[8:12]
    round_part11=round_key_addition[12:]
    #半字节替换
    round_part_s00=s_box1(round_part00)
    round_part_s10=s_box1(round_part10)
    round_part_s01=s_box1(round_part01)
    round_part_s11=s_box1(round_part11)
    #行位移
    temp=round_part_s10
    round_part_s10=round_part_s11
    round_part_s11=temp
    #列混淆
    S00=xor(multiply(1,round_part_s00),multiply(4,round_part_s10))
    S10=xor(multiply(4,round_part_s00),multiply(1,round_part_s10))
    S01=xor(multiply(1,round_part_s01),multiply(4,round_part_s11))
    S11=xor(multiply(4,round_part_s01),multiply(1,round_part_s11))
    Befoer_First_Round_Results = np.concatenate((S00, S10,S01,S11))
    First_Round_Results=xor(Befoer_First_Round_Results,key2)
    #第二轮
    round_part2_00=First_Round_Results[:4]
    round_part2_10=First_Round_Results[4:8]
    round_part2_01=First_Round_Results[8:12]
    round_part2_11=First_Round_Results[12:]    
    #半字节替换
    round_part_s2_00=s_box1(round_part2_00)
    round_part_s2_10=s_box1(round_part2_10)
    round_part_s2_01=s_box1(round_part2_01)
    round_part_s2_11=s_box1(round_part2_11)
    #行位移
    temp2=round_part_s2_10
    round_part_s2_10=round_part_s2_11
    round_part_s2_11=temp2
    #轮密钥加
    Befoer_Second_Round_Results = np.concatenate((round_part_s2_00, round_part_s2_10,round_part_s2_01,round_part_s2_11))
    Second_Round_Results=xor(Befoer_Second_Round_Results,key3)
    ciphertext=Second_Round_Results

    return np.array(ciphertext)



def decrypt(ciphertext, key):

    key1,key2,key3=key_process(key)
    round_key_addition=xor(ciphertext,key3)
    #第一轮
    round_part00=round_key_addition[:4]
    round_part10=round_key_addition[4:8]
    round_part01=round_key_addition[8:12]
    round_part11=round_key_addition[12:]
    #逆行位移
    temp=round_part10
    round_part10=round_part11
    round_part11=temp    
    #逆半字节替换
    round_part_s00=s_box2(round_part00)
    round_part_s10=s_box2(round_part10)
    round_part_s01=s_box2(round_part01)
    round_part_s11=s_box2(round_part11)
    #轮密钥加
    round_hole_part=np.concatenate((round_part_s00, round_part_s10,round_part_s01,round_part_s11))
    round_hole_part_xor=xor(round_hole_part,key2)
    round_part_s00=round_hole_part_xor[:4]
    round_part_s10=round_hole_part_xor[4:8]
    round_part_s01=round_hole_part_xor[8:12]
    round_part_s11=round_hole_part_xor[12:]
    #逆列混淆
    S00=xor(multiply(9,round_part_s00),multiply(2,round_part_s10))
    S01=xor(multiply(2,round_part_s00),multiply(9,round_part_s10))
    S10=xor(multiply(9,round_part_s01),multiply(2,round_part_s11))
    S11=xor(multiply(2,round_part_s01),multiply(9,round_part_s11))

    #第二轮
    round_part2_00=S00
    round_part2_10=S01
    round_part2_01=S10
    round_part2_11=S11
    #逆行位移
    temp2=round_part2_10
    round_part2_10=round_part2_11
    round_part2_11=temp2
    #逆半字节替换
    round_part_s2_00=s_box2(round_part2_00)
    round_part_s2_10=s_box2(round_part2_10)
    round_part_s2_01=s_box2(round_part2_01)
    round_part_s2_11=s_box2(round_part2_11)
    #轮密钥加
    Befoer_Second_Round_Results = np.concatenate((round_part_s2_00, round_part_s2_10,round_part_s2_01,round_part_s2_11))
    Second_Round_Results=xor(Befoer_Second_Round_Results,key1)
    plaintext=Second_Round_Results


    return np.array(plaintext)

if __name__ == "__main__":

    ciphertext = [1,1,0,0,1,1,1,0,0,1,0,1,0,1,1,1]  # 示例密文
    plaintext  = [1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1]  # 示例明文
    key = [0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0]  # 示例密钥

    ciphertext1=encrypt(plaintext,key)
    plaintext1=decrypt(ciphertext,key)

    print("密文",ciphertext1)
    print("明文",plaintext1)
    print("密钥",key)




