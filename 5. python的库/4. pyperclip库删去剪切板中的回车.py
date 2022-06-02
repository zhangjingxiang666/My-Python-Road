import pyperclip
text=pyperclip.paste()
text2=text.replace("\r\n", " ")#win下面的换行符为\r\n,linux下面的为\n。换行符也需要放在引号里面。
text2=text2.replace("-", " ")
#print(text)
pyperclip.copy(text2)
print(text2)