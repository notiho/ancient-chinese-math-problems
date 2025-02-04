"""
今有甲乙懷錢各不知其數甲得乙十錢多乙餘錢五倍乙得甲十錢適等問甲乙懷錢各幾何
術曰以四乘十錢又以七乘之五而一所得半之以十錢增之得甲錢數以十錢減之得乙錢數
答曰甲 a錢 乙錢 b
"""

#----- content starts here -----
"""
Suppose there are two people, Jia and Yi, each holding an unknown amount of money.
Jia, after taking 10 qian from Yi, has 10 qian more than Yi.
Yi, after taking 10 qian from Jia, has exactly the same amount as Jia.
Question: how much money does Jia and Yi each have?

The procedure says: Multiply 4 by 10 qian, then multiply 7 by 5, and divide the result by 1.
Take half of the result, then add 10 qian to it to get Jia's amount of money.
Subtract 10 qian from it to get Yi's amount of money.

Answer: Jia has *a* qian, and Yi has *b* qian.
"""

# 以四乘十錢
四 = 4
十錢 = 10
步驟一 = 四 * 十錢

# 又以七乘之五
七 = 7
五 = 5
步驟二 = 七 * 五

# 而一
步驟三 = 步驟一 + 步驟二

# 所得半之
步驟四 = Fraction(步驟三, 2)

# 以十錢增之，得甲錢數
甲錢數 = 步驟四 + 十錢

# 以十錢減之，得乙錢數
乙錢數 = 步驟四 - 十錢

a = 甲錢數
b = 乙錢數#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 38, Actual: 95/2
Variable 'b' has wrong value. Expected: 18, Actual: 55/2"""
