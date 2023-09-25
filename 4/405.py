'''
TQC+ 程式語言Python 405 不定數迴圈-分數等級

1. 題目說明:
請開啟PYD405.py檔案，依下列題意進行作答，使輸出值符合題意要求。作答完成請另存新檔為PYA405.py再進行評分。

2. 設計說明：
請撰寫一程式，以不定數迴圈的方式輸入一個正整數（代表分數），之後根據以下分數與GPA的對照表，印出其所對應的GPA。假設此不定數迴圈輸入-9999則會結束此迴圈。標準如下表所示：

分　數	GPA
90 ~ 100	A
80 ~ 89	B
70 ~ 79	C
60 ~ 69	D
0 ~ 59	E

3. 輸入輸出：
輸入說明
一個正整數，直至-9999結束輸入

輸出說明
依輸入值，輸出對應的GPA

輸入與輸出會交雜如下，輸出的部份以粗體字表示
75
C
39
E
100
A
85
B
65
D
-9999
'''
while True:
    n = eval(input())
    if n == -9999: break
    if n >= 90 and n <= 100: print('A')
    elif n >= 80 and n <= 89: print('B')
    elif n >= 70 and n <= 79: print('C')
    elif n >= 60 and n <= 69: print('D')
    else: print('E')