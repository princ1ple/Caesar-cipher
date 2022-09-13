str = input("设置加密密文：")
result = ""
k = input("设置开始数值：")
k = int(k)
for i in str:
    result += chr(ord(i)+k)
    k += 1
print(result)