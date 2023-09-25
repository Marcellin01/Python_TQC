'''
TQC+ 程式語言Python 604 眾數

1. 題目說明:
請開啟PYD604.py檔案，依下列題意進行作答，計算眾數及其出現的次數，使輸出值符合題意要求。作答完成請另存新檔為PYA604.py再進行評分。

2. 設計說明：
請撰寫一程式，讓使用者輸入十個整數作為樣本數，輸出眾數（樣本中出現最多次的數字）及其出現的次數。

提示：假設樣本中只有一個眾數。

3. 輸入輸出：
輸入說明
十個整數

輸出說明
眾數
眾數出現的次數

範例輸入
34
18
22
32
18
29
30
38
42
18
範例輸出
18
3
'''

d= {}

for i in range (10):
    n = eval(input())
    if n not in d :
        d[n] = 1
    else:
        d[n] += 1
max_key = max(d, key=d.get)
max_value = d[max_key]

print(max_key)
print(max_value)
