"""
今有兩稅錢四萬三千六百七十五貫二百文抽身内充腳每貫二百文問正及腳各幾何
術曰先置原錢折半六除是正錢數将正錢二因即得腳
答曰正 a貫 文腳 b貫
"""

#----- content starts here -----
"""
Suppose there is a total of 43,675 guan and 200 wen of tax money. 
It is desired to calculate the principal (正) and the surplus (腳), where each guan is 200 wen.
Question: how much is the principal and how much is the surplus?

The procedure says: First, take the original money, halve it, and divide by 6. This gives the amount of principal money.
Then, multiply the principal money by 2 to obtain the surplus.

Answer: the principal is *a* guan and *b* wen, and the surplus is *b* guan.
"""

# 兩稅錢四萬三千六百七十五貫二百文
總錢_貫 = 43675
總錢_文 = 200

# 每貫二百文
每貫文 = 200

# 將總錢轉換為文
總錢 = 總錢_貫 * 每貫文 + 總錢_文

# 先置原錢，折半，六除，是正錢數
正錢數_文 = Fraction(總錢, 2 * 6)

# 將正錢轉換為貫與文
正_貫 = 正錢數_文 // 每貫文
正_文 = 正錢數_文 % 每貫文

# 将正錢二因，即得腳
腳_文 = 2 * 正錢數_文

# 將腳轉換為貫與文
腳_貫 = 腳_文 // 每貫文

# 答案
a = 正_貫
b = 腳_貫#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 36396, Actual: 3639
Variable 'b' has wrong value. Expected: 36396/5, Actual: 7279"""
