'''
TQC+ 程式語言Python 603 數字排序

1. 題目說明:
請開啟PYD603.py檔案，依下列題意進行作答，顯示最大的三個數字，使輸出值符合題意要求。作答完成請另存新檔為PYA603.py再進行評分。

2. 設計說明：
請撰寫一程式，要求使用者輸入十個數字並存放在串列中。接著由大到小的順序顯示最大的3個數字。

3. 輸入輸出：
輸入說明
十個數字

輸出說明
由大到小排序，顯示最大的3個數字

範例輸入1
40
32
12
29
20
19
38
48
57
44
範例輸出1
57 48 44

範例輸入2
139
246
15
38
77
122
42
30
100
1
範例輸出2
246 139 122
'''

l = []
for i in range(10):
    l.append(int(input()))

for j in range(3):
    one = max(l)
    print(one, end=" ")
    l.remove(one)

