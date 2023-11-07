import tkinter as tk
from tkinter import messagebox
import encry
import numpy as np

# 加密按钮点击事件处理函数
def encrypt_button_clicked():
    plaintext = plaintext_entry.get()
    key = key_entry.get()

    # 判断传入明文是16bit且密钥是16bit
    if len(plaintext) == 16 and len(key) == 16:
        plaintext_binary = [int(bit) for bit in plaintext]
        key_binary = [int(bit) for bit in key]

        # 检查明文、密钥是否只由0和1构成
        if set(plaintext) <= {'0', '1'} and set(key) <= {'0', '1'}:
            # 调用加密函数
            ciphertext = encry.encrypt(plaintext_binary, key_binary)
            ciphertext_entry.delete(0, tk.END)
            ciphertext_entry.insert(0, "".join(str(bit) for bit in ciphertext))
        else:
            messagebox.showerror("错误", "请注意输入是否正确")

    # 判断传入明文是16it且密钥是字符（2字节）
    elif len(plaintext) == 16 and len(key) == 2:
        key_ascii1 = ord(key[0])
        key_ascii2 = ord(key[1])
        # 判断如果密钥的ascii码不大于1023或者明文只由0和1构成，则将密钥的ascii码转化为16bit的二进制字符串，然后调用加密函数
        if key_ascii1 > 255 and set(plaintext) <= {'0', '1'} and key_ascii2 > 255 :
            messagebox.showerror("错误", "请输入正确的ascii码")
        else:
            plaintext=[int(bit) for bit in plaintext]
            key=encry.character_process(key)
            ciphertext = encry.encrypt(plaintext, key)

            ciphertext1=ciphertext[:8]
            ciphertext2=ciphertext[8:]
            ciphertext_chars = ""
            for i in range(0, len(ciphertext1), 8):
                binary1 = ciphertext1[i:i+8]
                binary2 = ciphertext2[i:i+8]
                decimal1 = int("".join(str(bit) for bit in binary1), 2)
                decimal2 = int("".join(str(bit) for bit in binary2), 2)
                if decimal1 > 255 or decimal2>255:
                    # 如果超出了ascii码能表示的范围，直接显示二进制形式的密文
                    ciphertext_entry.delete(0, tk.END)
                    ciphertext_entry.insert(0, "".join(
                        str(bit) for bit in ciphertext))
                    return
                character1 = chr(decimal1)
                character2 = chr(decimal2)
                ciphertext_chars += character1+character2
            ciphertext_entry.delete(0, tk.END)
            ciphertext_entry.insert(0, ciphertext_chars)


    # 判断传入明文是字符（2字节）且密钥是16bit
    elif len(plaintext) == 2 and len(key) == 16:
        plaintext_ascii1 = ord(plaintext[0])
        plaintext_ascii2 = ord(plaintext[1])
        # 判断如果明文的ascii码不大于255且密钥只由0和1构成，则将明文的ascii码转化为8bit的二进制字符串，再调用加密函数
        if plaintext_ascii1 > 255 or plaintext_ascii2 > 255:
            messagebox.showerror("错误", "请输入正确的ascii码")
        else:

            plaintext=encry.character_process(plaintext)
            key = [int(bit) for bit in key]
            ciphertext = encry.encrypt(plaintext, key)

            ciphertext1=ciphertext[:8]
            ciphertext2=ciphertext[8:]
            ciphertext_chars = ""
            for i in range(0, len(ciphertext1), 8):
                binary1 = ciphertext1[i:i+8]
                binary2 = ciphertext2[i:i+8]
                decimal1 = int("".join(str(bit) for bit in binary1), 2)
                decimal2 = int("".join(str(bit) for bit in binary2), 2)
                if decimal1 > 255 or decimal2>255:
                    # 如果超出了ascii码能表示的范围，直接显示二进制形式的密文
                    ciphertext_entry.delete(0, tk.END)
                    ciphertext_entry.insert(0, "".join(
                        str(bit) for bit in ciphertext))
                    return
                character1 = chr(decimal1)
                character2 = chr(decimal2)
                ciphertext_chars += character1+character2
            ciphertext_entry.delete(0, tk.END)
            ciphertext_entry.insert(0, ciphertext_chars)

    # 判断传入明文是字符（2字节）且密钥是字符
    elif len(plaintext) == 2 and len(key) == 2:
        plaintext_ascii1 = ord(plaintext[0])
        plaintext_ascii2 = ord(plaintext[1])
        key_ascii1 = ord(key[0])
        key_ascii2 = ord(key[1])

        # 判断如果明文的ascii码不大于255且密钥只由0和1构成，则将明文的ascii码转化为8bit的二进制字符串，再调用加密函数
        if plaintext_ascii1 > 255 or plaintext_ascii2 > 255:
            messagebox.showerror("错误", "请输入正确的ascii码")
        else:
            plaintext=encry.character_process(plaintext)
            key=encry.character_process(key)
            ciphertext = encry.encrypt(plaintext, key)
            ciphertext1=ciphertext[:8]
            ciphertext2=ciphertext[8:]
            ciphertext_chars = ""
            for i in range(0, len(ciphertext1), 8):
                binary1 = ciphertext1[i:i+8]
                binary2 = ciphertext2[i:i+8]
                decimal1 = int("".join(str(bit) for bit in binary1), 2)
                decimal2 = int("".join(str(bit) for bit in binary2), 2)
                if decimal1 > 255 or decimal2>255:
                    # 如果超出了ascii码能表示的范围，直接显示二进制形式的密文
                    ciphertext_entry.delete(0, tk.END)
                    ciphertext_entry.insert(0, "".join(
                        str(bit) for bit in ciphertext))
                    return
                character1 = chr(decimal1)
                character2 = chr(decimal2)
                ciphertext_chars += character1+character2
            ciphertext_entry.delete(0, tk.END)
            ciphertext_entry.insert(0, ciphertext_chars)



    # 其他输入情况则提示“请注意输入是否正确”
    else:
        messagebox.showerror("错误", "请注意输入是否正确")


def decrypt_button_clicked():
    ciphertext = ciphertext_entry.get()
    key = key_entry.get()

    # 判断传入明文和密钥是否都是字符（2字节）
    if len(ciphertext) == 2 and len(key) == 2:
        ciphertext_ascii1 = ord(ciphertext[0])
        ciphertext_ascii2 = ord(ciphertext[1])
        key_ascii1 = ord(key[0])
        key_ascii2 = ord(key[1])

        # 判断如果明密文的ascii码大于255，则提示“请输入正确的ascii码”
        if ciphertext_ascii1 > 255 or key_ascii1 > 255 or key_ascii2 > 255 or ciphertext_ascii2 > 255:
            messagebox.showerror("错误", "请输入正确的ascii码")
        else:
            key=encry.character_process(key)
            ciphertext=encry.character_process(ciphertext)
            plaintext = encry.decrypt(ciphertext, key)

            plaintext1=plaintext[:8]
            plaintext2=plaintext[8:]
            plaintext_chars = ""
            for i in range(0, len(plaintext1), 8):
                binary1 = plaintext1[i:i+8]
                binary2 = plaintext2[i:i+8]
                decimal1 = int("".join(str(bit) for bit in binary1), 2)
                decimal2 = int("".join(str(bit) for bit in binary2), 2)
                if decimal1 > 255 or decimal2>255:
                    # 如果超出了ascii码能表示的范围，直接显示二进制形式的密文
                    plaintext_entry.delete(0, tk.END)
                    plaintext_entry.insert(0, "".join(
                        str(bit) for bit in plaintext))
                    return
                character1 = chr(decimal1)
                character2 = chr(decimal2)
                plaintext_chars += character1+character2

            plaintext_entry.delete(0, tk.END)
            #plaintext_entry.insert(0, "".join(str(bit) for bit in plaintext))
            plaintext_entry.insert(0, plaintext_chars)

    # 判断传入明文是16bit且密钥是16bit
    elif len(ciphertext) == 16 and len(key) == 16:
        ciphertext_binary = [int(bit) for bit in ciphertext]
        key_binary = [int(bit) for bit in key]

        # 检查密文、密钥是否只由0和1构成
        if set(ciphertext) <= {'0', '1'} and set(key) <= {'0', '1'}:
            # 调用解密函数
            plaintext = encry.decrypt(ciphertext_binary, key_binary)
            plaintext_entry.delete(0, tk.END)
            plaintext_entry.insert(0, "".join(str(bit) for bit in plaintext))
        else:
            messagebox.showerror("错误", "请注意输入是否正确")

    # 判断传入密文是16bit且密钥是字符（2字节）
    elif len(ciphertext) == 16 and len(key) == 2:
        key_ascii1 = ord(key[0])
        key_ascii2 = ord(key[1])

        # 判断如果密钥的ascii码不大于1023或者明文只由0和1构成，则将密钥的ascii码转化为10bit的二进制字符串，然后调用加密函数
        if key_ascii1 > 255 or  key_ascii2 > 255:
            messagebox.showerror("错误", "请输入正确的ascii码")
        else:
            ciphertext=[int(bit) for bit in ciphertext]
            key=encry.character_process(key)

            # 调用解密函数
            plaintext = encry.decrypt(ciphertext, key)
            plaintext1=plaintext[:8]
            plaintext2=plaintext[8:]
            plaintext_chars = ""
            for i in range(0, len(plaintext1), 8):
                binary1 = plaintext1[i:i+8]
                binary2 = plaintext2[i:i+8]
                decimal1 = int("".join(str(bit) for bit in binary1), 2)
                decimal2 = int("".join(str(bit) for bit in binary2), 2)
                if decimal1 > 255 or decimal2>255:
                    # 如果超出了ascii码能表示的范围，直接显示二进制形式的密文
                    plaintext_entry.delete(0, tk.END)
                    plaintext_entry.insert(0, "".join(
                        str(bit) for bit in plaintext))
                    return
                character1 = chr(decimal1)
                character2 = chr(decimal2)
                plaintext_chars += character1+character2

            plaintext_entry.delete(0, tk.END)
            plaintext_entry.insert(0, plaintext_chars)
            #plaintext_entry.insert(0, "".join(str(bit) for bit in plaintext))

    # 判断传入密文是字符（2字节）且密钥是16bit
    elif len(ciphertext) == 2 and len(key) == 16:
        ciphertext_ascii1 = ord(ciphertext[0])
        ciphertext_ascii2 = ord(ciphertext[1])
        # 判断如果密文的ascii码不大于255且密钥只由0和1构成，则将明文的ascii码转化为8bit的二进制字符串，再调用加密函数
        if ciphertext_ascii1 > 255 or ciphertext_ascii2 > 255:  # or set(key) <= {'0', '1'}:
            messagebox.showerror("错误", "请输入正确的ascii码")
        else:

            key = [int(bit) for bit in key]
            ciphertext=encry.character_process(ciphertext)
            plaintext = encry.decrypt(ciphertext, key)
            
            plaintext1=plaintext[:8]
            plaintext2=plaintext[8:]
            plaintext_chars = ""
            for i in range(0, len(plaintext1), 8):
                binary1 = plaintext1[i:i+8]
                binary2 = plaintext2[i:i+8]
                decimal1 = int("".join(str(bit) for bit in binary1), 2)
                decimal2 = int("".join(str(bit) for bit in binary2), 2)
                if decimal1 > 255 or decimal2>255:
                    # 如果超出了ascii码能表示的范围，直接显示二进制形式的密文
                    plaintext_entry.delete(0, tk.END)
                    plaintext_entry.insert(0, "".join(
                        str(bit) for bit in plaintext))
                    return
                character1 = chr(decimal1)
                character2 = chr(decimal2)
                plaintext_chars += character1+character2

            plaintext_entry.delete(0, tk.END)
            plaintext_entry.insert(0, plaintext_chars)
            #plaintext_entry.insert(0, "".join(str(bit) for bit in plaintext))
    # 其他输入情况则提示“请注意输入是否正确”
    else:
        messagebox.showerror("错误", "请注意输入是否正确")


# 创建主窗口
window = tk.Tk()
window.title("AES加解密工具")

# 设置窗口大小和背景颜色
window.geometry("380x200")
window.configure(bg="#F9F9F9")

# 创建输入框和标签
plaintext_label = tk.Label(window, text="明文（16位）：",
                           font=("微软雅黑", 12), bg="#F9F9F9")
plaintext_entry = tk.Entry(window, font=("微软雅黑", 12), width=20, bd=2)

ciphertext_label = tk.Label(window, text="密文（16位）：",
                            font=("微软雅黑", 12), bg="#F9F9F9")
ciphertext_entry = tk.Entry(window, font=("微软雅黑", 12), width=20, bd=2)

key_label = tk.Label(window, text="密钥（16位）：", font=("微软雅黑", 12), bg="#F9F9F9")
key_entry = tk.Entry(window, font=("微软雅黑", 12), width=20, bd=2)

# 创建按钮
encrypt_button = tk.Button(window, text="加密", font=(
    "微软雅黑", 12), bg="#4AAE9B", fg="#FFFFFF", command=encrypt_button_clicked)
decrypt_button = tk.Button(window, text="解密", font=(
    "微软雅黑", 12), bg="#DF5E88", fg="#FFFFFF", command=decrypt_button_clicked)

# 设置布局
plaintext_label.grid(row=0, column=0, padx=20, pady=10)
plaintext_entry.grid(row=0, column=1, padx=20, pady=10)

ciphertext_label.grid(row=1, column=0, padx=20, pady=10)
ciphertext_entry.grid(row=1, column=1, padx=20, pady=10)

key_label.grid(row=2, column=0, padx=20, pady=10)
key_entry.grid(row=2, column=1, padx=20, pady=10)

encrypt_button.grid(row=3, column=0, padx=20, pady=10)
decrypt_button.grid(row=3, column=1, padx=20, pady=10)


# 运行主循环
window.mainloop()
