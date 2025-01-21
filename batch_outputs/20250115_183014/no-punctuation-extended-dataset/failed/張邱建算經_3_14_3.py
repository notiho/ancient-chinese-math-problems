"""
今有甲乙懷錢各不知其數甲得乙十錢多乙餘錢五倍乙得甲十錢適等問甲乙懷錢各幾何
術曰以四乘十錢又以七乘之五而一所得半之以十錢增之得甲錢數以十錢減之得乙錢數
答曰甲 a錢 乙錢 b
"""

"""
Suppose there are two people, Jia and Yi, each holding an unknown amount of money.
Jia takes 10 qian from Yi and has 10 qian more than Yi's remaining money.
Yi takes 10 qian from Jia, and their amounts become equal.
Question: how much money does Jia and Yi each hold?

The procedure says: Multiply 4 by 10 qian, then multiply 7 by 5, and divide the result by 1.
Take half of the result, add 10 qian to it to obtain Jia's amount of money.
Subtract 10 qian from it to obtain Yi's amount of money.

Answer: Jia has *a* qian, Yi has *b* qian.
"""

# 以四乘十錢
四乘十 = 4 * 10

# 又以七乘之五
七乘五 = 7 * 5

# 而一所得
所得 = 四乘十 + 七乘五

# 半之
半 = 所得 / 2

# 以十錢增之，得甲錢數
a = 半 + 10

# 以十錢減之，得乙錢數
b = 半 - 10
"""
Variable 'a' has wrong value. Expected: 38, Actual: 47.5
Variable 'b' has wrong value. Expected: 18, Actual: 27.5"""
