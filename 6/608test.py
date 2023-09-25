'''
TQC+ 程式語言Python 608 最大最小值索引

1. 題目說明:
請開啟PYD608.py檔案，依下列題意進行作答，建立3*3矩陣並輸出矩陣最大值與最小值的索引，使輸出值符合題意要求。作答完成請另存新檔為PYA608.py再進行評分。

2. 設計說明：
請撰寫一程式，讓使用者建立一個3*3的矩陣，其內容為從鍵盤輸入的整數（不重複），接著輸出矩陣最大值與最小值的索引。

3. 輸入輸出：
輸入說明
九個整數

輸出說明
矩陣最大值及其索引
矩陣最小值及其索引

範例輸入
6
4
8
39
12
3
-3
49
33
範例輸出
Index of the largest number 49 is: (2, 1)
Index of the smallest number -3 is: (2, 0)
'''
first_l = []
second_l = []
third_l = []
for i in range(9):
    n = eval(input())
    if i < 3:
        first_l.append(n)
    elif i < 6:
        second_l.append(n)
    else:
        third_l.append(n)

all_l =[first_l, second_l, third_l]

max_value = float('-inf')
index_of_max = (-1, -1)

min_value = float('inf')
index_of_min = (-1, -1) 

for i in range(len(all_l)):
    for j in range(len(all_l[i])):
        if all_l[i][j] > max_value:
            max_value = all_l[i][j]
            index_of_max = (i, j)
        if all_l[i][j] < min_value:
            min_value = all_l[i][j]
            index_of_min = (i, j)

print(f"Index of the largest number {max_value} is: {index_of_max}")

print(f"Index of the smallest number {min_value} is: {index_of_min}")
