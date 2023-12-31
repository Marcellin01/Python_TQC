'''
TQC+ 程式語言Python 210 三角形判斷

1. 題目說明:
請開啟PYD210.py檔案，依下列題意進行作答，檢查輸入值是否可組成三角形，使輸出值符合題意要求。作答完成請另存新檔為PYA210.py再進行評分。

2. 設計說明：
請使用選擇敘述撰寫一程式，讓使用者輸入三個邊長，檢查這三個邊長是否可以組成一個三角形。若可以，則輸出該三角形之周長；否則顯示【Invalid】。

提示：檢查方法 = 任意兩個邊長之總和大於第三邊長。

3. 輸入輸出：
輸入說明
三個正整數

輸出說明
可以組成三角形則輸出周長；否則顯示Invalid

範例輸入1
5
6
13
範例輸出1
Invalid

範例輸入2
1
1
1
範例輸出2
3
'''
import statistics
a = eval(input())
b = eval(input())
c = eval(input())

n = [a, b ,c]

min = min(n)
med = statistics.median(n)
max = max(n)

if min+med>max:
    print(a+b+c)
else:
    print("Invalid")