"""
今有出錢六百一十，買羽二千一百翭。欲其貴賤率之，問︰各幾何？
反其率術曰：以錢數為法，所率為實，實如法而一。不滿法者反以實減法，法少，實多。二物各以所得多少之數乘法實，即物數。
荅曰：其 a翭 ， b翭 一錢 其 c翭 ， d翭 一錢
"""

"""
To solve this problem, we need to determine the rates (貴賤率) for the two types of 羽 (feathers). Let's follow the procedure step by step:


"""


from fractions import Fraction

# 出錢六百一十
錢數 = 610

# 買羽二千一百翭
羽數 = 2100

# 貴賤率術：以錢數為法
法 = 錢數

# 假設兩種羽的貴賤率分別為 x 和 y
# x + y = 羽數
# x * 法 + y * 法 = 錢數

# 解釋：
# 假設 x 為貴羽的數量，y 為賤羽的數量
# 貴羽的價格為 a翭 一錢，賤羽的價格為 b翭 一錢

# 設定貴羽的價格為 1翭 一錢，賤羽的價格為 2翭 一錢
貴羽價格 = 1
賤羽價格 = 2

# 計算貴羽和賤羽的數量
貴羽數 = Fraction(法 - 羽數 * 賤羽價格, 貴羽價格 - 賤羽價格)
賤羽數 = 羽數 - 貴羽數

# 計算貴羽和賤羽的價格
a = 貴羽數
b = 貴羽價格
c = 賤羽數
d = 賤羽價格

# 結果
print(f"其 {a}翭 ， {b}翭 一錢 其 {c}翭 ， {d}翭 一錢")


"""
 

This code calculates the number of expensive and cheap feathers based on their rates and total money spent.
"""


"""
Variable 'a' has wrong value. Expected: 1140, Actual: 3590
Variable 'b' has wrong value. Expected: 3, Actual: 1
Variable 'c' has wrong value. Expected: 960, Actual: -1490
Variable 'd' has wrong value. Expected: 4, Actual: 2"""
