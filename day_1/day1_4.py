# # coding:utf-8
# rows = int(input('输入列数： '))
# i = j = k = 1  # 声明变量，i用于控制外层循环（图形行数），j用于控制空格的个数，k用于控制*的个数
# # 等腰直角三角形1
# print("等腰直角三角形1")
# for i in range(0, rows):
#     for k in range(0, rows - i):
#         print(" * "),
#         # 注意这里的","，一定不能省略，可以起到不换行的作用
#         k += 1
#     i += 1

# coding:utf-8
rows = int(input('输入行数： '))

# --- 修正后的等腰直角三角形 ---
print("\n等腰直角三角形")
for i in range(rows):
    for _ in range(i + 1):
        print("* ", end='')
    # print("\n")  # 换行,这种写法是错误的，print 默认换行了，在写一个\n,再一次换行
    print()#这种写法是对的
    #也可以将print()省略，也是对的

# --- 实心等边三角形 ---
print("\n实心等边三角形")
for i in range(rows):
    # 打印空格
    for _ in range(rows - i - 1):
        print(" ", end='')
    # 打印星号
    for _ in range(2 * i + 1):
        print("*", end='')
    print()

