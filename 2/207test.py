'''
TQC+ 程式語言Python 207 折扣方案

1. 題目說明:
請開啟PYD207.py檔案，依下列題意進行作答，判斷輸入值之折扣並計算實付金額，使輸出值符合題意要求。作答完成請另存新檔為PYA207.py再進行評分。

2. 設計說明：
請使用選擇敘述撰寫一程式，要求使用者輸入購物金額，購物金額需大於8,000（含）以上，並顯示折扣優惠後的實付金額。購物金額折扣方案如下表所示：

金　　額	折　扣
8,000（含）以上	9.5折
18,000（含）以上	9折
28,000（含）以上	8折
38,000（含）以上	7折
3. 輸入輸出：
輸入說明
一個數值，需大於8,000（含）以上

輸出說明
顯示折扣優惠後的實付金額（輸出不需指定小數點位數）

範例輸入
12000
範例輸出
11400.0
'''
p = eval(input())

if p >= 38000:
    print(p*0.7)
elif p >= 28000 :
    print(p*0.8)
elif p >= 18000 :
    print(p*0.9)
elif p >= 8000 :
    print(p*0.95)
else:
    print(p)
