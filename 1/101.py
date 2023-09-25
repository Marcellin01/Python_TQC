'''
TQC+ 程式語言Python 101 整數格式化輸出

1. 題目說明:
請開啟PYD101.py檔案，依下列題意進行作答，輸入整數及進行格式化輸出，使輸出值符合題意要求。作答完成請另存新檔為PYA101.py再進行評分。

2. 設計說明：
請撰寫一程式，輸入四個整數，然後將這四個整數以欄寬為5、欄與欄間隔一個空白字元，再以每列印兩個的方式，先列印向右靠齊，再列印向左靠齊，左右皆以直線 |（Vertical bar）作為邊界。

3. 輸入輸出：
輸入說明
四個整數

輸出說明
格式化輸出

範例輸入
85
4
299
478

範例輸出
|   85     4|
|  299   478|
|85    4    |
|299   478  |
'''
a = eval(input())
b = eval(input())
c = eval(input())
d = eval(input())
print(f'|{a:>5} {b:>5}|')
print(f'|{c:>5} {d:>5}|')
print(f'|{a:<5} {b:<5}|')
print(f'|{c:<5} {d:<5}|')