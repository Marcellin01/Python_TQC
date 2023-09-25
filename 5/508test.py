'''
TQC+ 程式語言Python 508 最大公因數

1. 題目說明:
請開啟PYD508.py檔案，依下列題意進行作答，計算兩個正整數的最大公因數，使輸出值符合題意要求。作答完成請另存新檔為PYA508.py再進行評分。。

2. 設計說明：
請撰寫一程式，讓使用者輸入兩個正整數x、y，並將x與y傳遞給名為compute()的函式，此函式回傳x和y的最大公因數。

3. 輸入輸出：
輸入說明
兩個正整數（以半形逗號分隔）

x,y

輸出說明
最大公因數

範例輸入1
12,8
範例輸出1
4

範例輸入2
4,6
範例輸出2
2
'''
a = eval(input())
b = eval(input())

def compute(a,b):
    both = 1
    for i in range(2,a):
        if a % i == 0:
            a_ = i
        if b % i == 0:
            b_ = i
        if a_ == b_:
            both = a_
    print(both)

compute(a,b)