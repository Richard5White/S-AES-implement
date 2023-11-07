import numpy as np
import encry

#异或
def xor(arr1, arr2):
    
    return np.bitwise_xor(arr1, arr2)

#明、密文切割
def text_cut(text):
    text1=text[:16]
    text2=text[16:32]
    text3=text[32:48]
    text4=text[48:]

    return text1,text2,text3,text4

#CFB加密
def cbc_encrypt(plaintext,i_v,key):
    plaintext1,plaintext2,plaintext3,plaintext4=text_cut(plaintext)#切割
    k1=encry.encrypt(i_v,key)#初始向量和密钥加密得到k1
    ciphertext1=xor(plaintext1,k1)#异或得到第一段加密文，并作为下一段的向量
    #以此类推
    k2=encry.encrypt(ciphertext1,key)
    ciphertext2=xor(plaintext2,k2)

    k3=encry.encrypt(ciphertext2,key)
    ciphertext3=xor(plaintext3,k3)

    k4=encry.encrypt(ciphertext3,key)
    ciphertext4=xor(plaintext4,k4)

    ciphertext=np.concatenate((ciphertext1,ciphertext2,ciphertext3,ciphertext4))


    return ciphertext

#CFB解密
def cbc_decrypt(ciphertext,i_v,key):
    ciphertext1,ciphertext2,ciphertext3,ciphertext4=text_cut(ciphertext)#解密安装相同顺序一段一段解就好
    k1=encry.decrypt(i_v,key)
    plaintext1=xor(ciphertext1,k1)

    k2=encry.decrypt(plaintext1,key)
    plaintext2=xor(ciphertext2,k2)

    k3=encry.decrypt(plaintext2,key)
    plaintext3=xor(ciphertext3,k3)

    k4=encry.decrypt(plaintext3,key)
    plaintext4=xor(ciphertext4,k4)

    ciphertext=np.concatenate((plaintext1,plaintext2,plaintext3,plaintext4))


    return plaintext

if __name__ == "__main__":

    ciphertext =  [1,1,1,0,1,1,0,1,0,1,0,1,1,1,0,0,
                   0,1,1,1,0,0,1,1,1,1,1,1,0,0,1,1,
                   1,1,0,0,0,0,0,1,1,0,1,1,1,0,0,1,
                   0,1,0,0,0,1,0,1,0,0,1,1,0,0,1,0]  # 示例密文
    plaintext =   [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,
                   1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,
                   1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,
                   1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]  # 示例明文
    
    key = [0,0,1,0,1,1,0,1,0,1,0,1,0,1,0,1]  # 示例密钥
    i_v=[1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1]#初始向量


    ciphertext1=cbc_encrypt(plaintext,i_v,key)
    plaintext1=cbc_decrypt(ciphertext,i_v,key)

    print(ciphertext1)
    print(plaintext1)
