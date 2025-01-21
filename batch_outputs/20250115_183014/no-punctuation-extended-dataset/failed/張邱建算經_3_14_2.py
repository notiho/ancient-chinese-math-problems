"""
今有甲乙懷錢各不知其數甲得乙十錢多乙餘錢五倍乙得甲十錢適等問甲乙懷錢各幾何
術曰以四乘十錢又以七乘之五而一所得半之以十錢增之得甲錢數以十錢減之得乙錢數
答曰甲 a錢 乙錢 b
"""

"""
Suppose there are two people, Jia and Yi, each holding an unknown amount of money.
Jia takes 10 qian from Yi and has 10 qian more than Yi's remaining money, which is 5 times Yi's leftover money.
Yi takes 10 qian from Jia, and their amounts become equal.
Question: how much money does Jia and Yi each hold?

The procedure says: Multiply 4 by 10 qian, then multiply 7 by 5 and divide by 1.
Take half of the result, then add 10 qian to obtain Jia's amount of money.
Subtract 10 qian to obtain Yi's amount of money.

Answer: Jia has *a* qian, Yi has *b* qian.
"""

# 以四乘十錢
step1 = 4 * 10

# 又以七乘之五而一
step2 = 7 * 5

# 所得半之
step3 = (step1 + step2) / 2

# 以十錢增之，得甲錢數
a = step3 + 10

# 以十錢減之，得乙錢數
b = step3 - 10
"""
Variable 'a' has wrong value. Expected: 38, Actual: 47.5
Variable 'b' has wrong value. Expected: 18, Actual: 27.5"""
