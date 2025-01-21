"""
今有兩稅錢四萬三千六百七十五貫二百文抽身内充腳每貫二百文問正及腳各幾何
術曰先置原錢折半六除是正錢數将正錢二因即得腳
答曰正 a貫 文腳 b貫
"""

"""
Suppose there are 43,675 guan and 200 wen of tax money. 
It is desired to separate the principal (正) and the surplus (腳), where each guan is 200 wen.
Question: how much is the principal and how much is the surplus?

The procedure says: First, take the original money, halve it, and divide by 6. This gives the amount of the principal (正).
Then, multiply the principal by 2 to obtain the surplus (腳).

Answer: the principal is *a* guan and *b* wen, and the surplus is *c* guan.
"""

# 兩稅錢四萬三千六百七十五貫二百文
原錢_貫 = 43675
原錢_文 = 200

# 每貫二百文
每貫文 = 200

# Convert everything to wen for calculation
原錢_總文 = 原錢_貫 * 每貫文 + 原錢_文

# 先置原錢，折半，六除，是正錢數
正錢_總文 = Fraction(原錢_總文, 2 * 6)

# 将正錢二因，即得腳
腳_總文 = 2 * 正錢_總文

# Convert back to 貫 and 文 for 正錢
正錢_貫 = 正錢_總文 // 每貫文
正錢_文 = 正錢_總文 % 每貫文

# Convert back to 貫 for 腳
腳_貫 = Fraction(腳_總文, 每貫文)

# Assign results
a = 正錢_貫
b = 正錢_文
c = 腳_貫
"""
Variable 'a' has wrong value. Expected: 36396, Actual: 3639
Variable 'b' has wrong value. Expected: 36396/5, Actual: 400/3"""
