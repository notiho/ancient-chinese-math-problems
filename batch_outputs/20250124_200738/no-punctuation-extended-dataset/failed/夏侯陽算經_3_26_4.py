"""
今有兩稅錢四萬三千六百七十五貫二百文抽身内充腳每貫二百文問正及腳各幾何
術曰先置原錢折半六除是正錢數将正錢二因即得腳
答曰正 a貫 文腳 b貫
"""

#----- content starts here -----
"""
Suppose there are 43,675 guan and 200 wen of tax money. 
It is desired to calculate the principal (正) and the surplus (腳), where each guan is 200 wen.
Question: how much is the principal (正) and how much is the surplus (腳)?

The procedure says: First, take the original money, halve it, and divide by 6. This gives the amount of principal money (正).
Then, multiply the principal money by 2 to obtain the surplus (腳).

Answer: the principal is *a* guan and *b* wen, and the surplus is *b* guan.
"""

# 兩稅錢四萬三千六百七十五貫二百文
原錢_貫 = 43675
原錢_文 = 200

# 每貫二百文
每貫文 = 200

# 將文轉為貫
原錢 = 原錢_貫 + Fraction(原錢_文, 每貫文)

# 先置原錢，折半
折半 = 原錢 / 2

# 六除，是正錢數
正錢 = 折半 / 6

# 将正錢二因，即得腳
腳錢 = 正錢 * 2

# 分解正錢為貫與文
a_貫 = int(正錢)
a_文 = (正錢 - a_貫) * 每貫文

# 分解腳錢為貫
b_貫 = 腳錢

a = f"{a_貫}貫 {int(a_文)}文"
b = f"{b_貫}貫"#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 36396, Actual: 3639貫 133文
Variable 'b' has wrong value. Expected: 36396/5, Actual: 21838/3貫"""
