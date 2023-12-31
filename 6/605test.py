'''
TQC+ 程式語言Python 605 成績計算

1. 題目說明:
請開啟PYD605.py檔案，依下列題意進行作答，去除最高最低分後加總其餘成績，使輸出值符合題意要求。作答完成請另存新檔為PYA605.py再進行評分。

2. 設計說明：
請撰寫一程式，讓使用者輸入十個成績，接下來將十個成績中最小和最大值（最小、最大值不重複）以外的成績作加總及平均，並輸出結果。

提示：平均值輸出到小數點後第二位。

3. 輸入輸出：
輸入說明
十個數字

輸出說明
總和
平均

範例輸入
89
78
67
80
75
98
77
89
76
60
範例輸出
631
78.88
'''

score_list = []
sum = 0
for i in range(10):
    score = eval(input())
    score_list.append(score)
max_score = max(score_list)
min_score = min(score_list)
score_list.remove(max_score)
score_list.remove(min_score)
for s in score_list:
    sum += s
avg = sum / len(score_list)
print(sum)
print(f'{avg:.2f}')