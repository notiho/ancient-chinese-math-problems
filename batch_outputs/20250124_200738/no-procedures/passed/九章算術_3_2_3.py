"""
今有甲持錢五百六十，乙持錢三百五十，丙持錢一百八十，凡三人俱出關，關稅百錢。欲以錢數多少衰出之，問︰各幾何？
荅曰：甲出 a錢 。乙出 b錢 。丙出 c錢 。
"""

#----- content starts here -----
"""
Suppose there are three people: Jia, Yi, and Bing. Jia has 560 qian, Yi has 350 qian, and Bing has 180 qian. 
Together, they need to pay a toll of 100 qian. The toll is to be divided proportionally based on how much money each person has.

Question: how much does each person pay?

Answer: Jia pays *a* qian, Yi pays *b* qian, and Bing pays *c* qian.
"""

# Total money held by each person
甲 = 560
乙 = 350
丙 = 180

# Total money
總錢 = 甲 + 乙 + 丙

# Total toll
關稅 = 100

# Calculate the proportional contribution for each person
a = Fraction(甲 * 關稅, 總錢)
b = Fraction(乙 * 關稅, 總錢)
c = Fraction(丙 * 關稅, 總錢)

# Results
a, b, c#----- content ends here -----

"""
"""
