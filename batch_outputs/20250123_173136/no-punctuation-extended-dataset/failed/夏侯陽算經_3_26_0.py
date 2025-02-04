"""
今有兩稅錢四萬三千六百七十五貫二百文抽身内充腳每貫二百文問正及腳各幾何
術曰先置原錢折半六除是正錢數将正錢二因即得腳
答曰正 a貫 文腳 b貫
"""

"""
Suppose there is a total tax amount of 43,675 guan and 200 wen. 
The tax is divided into the principal (正) and the surcharge (腳), where each guan is 200 wen.
Question: how much is the principal (正) and how much is the surcharge (腳)?

The procedure says: First, take the original amount of money, halve it, and divide by 6. This gives the principal amount.
Then, multiply the principal by 2 to obtain the surcharge.

Answer: the principal is *a* guan and *b* wen, and the surcharge is *c* guan.
"""

# 兩稅錢四萬三千六百七十五貫二百文
總錢_貫 = 43675
總錢_文 = 200

# 每貫二百文
每貫文 = 200

# 將總錢轉換為文
總錢_文 += 總錢_貫 * 每貫文

# 折半六除，是正錢數
正錢_文 = Fraction(總錢_文, 2 * 6)

# 将正錢轉換為貫和文
正錢_貫 = 正錢_文 // 每貫文
正錢_餘文 = 正錢_文 % 每貫文

# 將正錢二因，即得腳
腳錢_文 = 2 * 正錢_文

# 将腳錢轉換為貫
腳錢_貫 = Fraction(腳錢_文, 每貫文)

# 答案
a = 正錢_貫
b = 正錢_餘文
c = 腳錢_貫
"""
Variable 'a' has wrong value. Expected: 36396, Actual: 3639
Variable 'b' has wrong value. Expected: 36396/5, Actual: 400/3"""
