'''
TQC+ 程式語言Python 108 座標距離計算

1. 題目說明:
請開啟PYD108.py檔案，依下列題意進行作答，計算兩點座標及其距離，使輸出值符合題意要求。作答完成請另存新檔為PYA108.py再進行評分。

2. 設計說明：
請撰寫一程式，讓使用者輸入四個數字x1、y1、x2、y2，分別代表兩個點的座標(x1, y1)、(x2, y2)。計算並輸出這兩點的座標與其歐式距離。

提示1：歐式距離 ((x1-x2)+(y1-y2))**0.5
提示2：兩座標的歐式距離，輸出到小數點後第4位

3. 輸入輸出：
輸入說明
四個數字x1、y1、x2、y2

輸出說明
座標1
座標2
兩座標的歐式距離

範例輸入
2
1
5.5
8

範例輸出
( 2 , 1 )
( 5.5 , 8 )
Distance = 7.8262
'''

x1 = eval(input())
y1 = eval(input())
x2 = eval(input())
y2 = eval(input())

print(f'''
( {x1} , {y1} )
( {x2} , {y2} )
Distance = {((x1-x2)**2+(y1-y2)**2)**0.5:.4f}
''')