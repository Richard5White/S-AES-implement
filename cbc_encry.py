import numpy as np
import encry

# 异或
def xor(arr1, arr2):
    return np.bitwise_xor(arr1, arr2)

# 明、密文切割
def text_cut(text):
    text1 = text[:16]
    text2 = text[16:32]
    text3 = text[32:48]
    text4 = text[48:]

    return text1, text2, text3, text4

# CBC加密
def cbc_encrypt(plaintext, i_v, key):
    plaintext1, plaintext2, plaintext3, plaintext4 = text_cut(plaintext)  # 切割
    K1 = xor(plaintext1, i_v)  
    C1 = encry.encrypt(K1, key)  #
    # 以此类推
    K2 = xor(plaintext2, C1)
    C2 = encry.encrypt(K2, key)
    K3 = xor(plaintext3, C2)
    C3 = encry.encrypt(K3, key)
    K4 = xor(plaintext4, C3)
    C4=encry.encrypt(K4, key)
    
    ciphertext = np.concatenate((C1, C2, C3, C4))

    return ciphertext

# CBC解密
def cbc_decrypt(ciphertext, i_v, key):
    ciphertext1, ciphertext2, ciphertext3, ciphertext4 = text_cut(ciphertext)  # 解密按照相同顺序一段一段解密就好
    k1 = encry.decrypt(ciphertext1, key)
    plaintext1 = xor(i_v, k1)
    k2 = encry.decrypt(ciphertext2, key)
    plaintext2 = xor(ciphertext1, k2)
    k3 = encry.decrypt(ciphertext3, key)
    plaintext3 = xor(ciphertext2, k3)
    k4 = encry.decrypt(ciphertext4, key)
    plaintext4 = xor(ciphertext3, k4)
    
    plaintext = np.concatenate((plaintext1, plaintext2, plaintext3, plaintext4))

    return plaintext

if __name__ == "__main__":
    ciphertext = [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1,
                  0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1,
                  1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0,
                  0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1]  # 示例密文
    ciphertext2 = [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1,
                  0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1,
                  1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0,
                  0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1] 

    plaintext = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0,
                  1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0,
                  1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0,
                  1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]  # 示例明文
    
    key = [0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]  # 示例密钥
    i_v = [1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1]  # 初始向量

    ciphertext1 = cbc_encrypt(plaintext, i_v, key)
    plaintext1 = cbc_decrypt(ciphertext, i_v, key)

    print(ciphertext1)
    print(plaintext1)
