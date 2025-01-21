"""
今有出錢九百八十，買矢簳五千八百二十枚。欲其貴賤率之，問︰各幾何？
反其率術曰：以錢數為法，所率為實，實如法而一。不滿法者反以實減法，法少，實多。二物各以所得多少之數乘法實，即物數。
荅曰：其 a枚 ， b枚 一錢 其 c枚 ， d枚 一錢
"""

"""
To solve this problem, we need to calculate the rates of "貴" (expensive) and "賤" (cheap) arrows based on the given total money and total number of arrows. Here's the Python implementation following the described procedure:


"""


from fractions import Fraction

# 出錢九百八十
錢數 = 980

# 買矢簳五千八百二十枚
矢簳數 = 5820

# 貴賤率未知，假設貴率為 a 枚一錢，賤率為 b 枚一錢
# 反其率術曰：以錢數為法，所率為實，實如法而一。
法 = 錢數
實 = 矢簳數

# 不滿法者反以實減法，法少，實多。
# 二物各以所得多少之數乘法實，即物數。
貴率 = Fraction(1, 2)  # 假設貴率為 2 枚一錢
賤率 = Fraction(1, 3)  # 假設賤率為 3 枚一錢

# 計算貴和賤的總數
貴枚數 = 法 * 貴率
賤枚數 = 法 * 賤率

# 確保總數等於矢簳數
if 貴枚數 + 賤枚數 == 矢簳數:
    a = 貴枚數
    b = 貴率.denominator
    c = 賤枚數
    d = 賤率.denominator
else:
    raise ValueError("無法匹配總數，請檢查輸入數據或假設的貴賤率。")

# 結果
print(f"其 {a} 枚，{b} 枚一錢；其 {c} 枚，{d} 枚一錢。")


"""


This code assumes initial rates for "貴" and "賤" arrows (`貴率` and `賤率`) and calculates the corresponding numbers of arrows and their rates. If the total matches the given number of arrows, it outputs the results. Otherwise, it raises an error indicating a mismatch. Adjust the rates as needed to fit the problem's specific conditions.
"""


"""
Code error: 無法匹配總數，請檢查輸入數據或假設的貴賤率。"""
