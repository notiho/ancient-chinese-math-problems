"""
假今天正十一月朔夜半，日在鬥十度七百分度之四百八十。以章歲為母，朔月行定分九千，朔日定小余一萬，日法二萬，章歲七百，亦名行分法。今不取加時日度。問：天正朔夜半之時月在何處？
術曰：以章歲減朔月行定分，余以乘朔日定小余，滿日法而一，為先行分。不盡者，半法已上收成一，已下者棄之。若先行分滿日行分而一，為度分，以減朔日夜半日所在度分，若度分不足減，加往宿度；其分不足減者，退一度為行分而減之，余即朔日夜半月行所在度及分也。
答曰：在鬥 a度 。
"""

"""
To solve this problem, we will follow the procedure step by step and translate it into Python code.


"""


from fractions import Fraction

# Given values
章歲 = 700  # 章歲 (also called 行分法)
朔月行定分 = 9000  # 朔月行定分
朔日定小余 = 10000  # 朔日定小余
日法 = 20000  # 日法
朔日夜半日所在度分 = Fraction(480, 1)  # 日在鬥十度七百分度之四百八十

# Step 1: 以章歲減朔月行定分
step1余 = 章歲 - 朔月行定分

# Step 2: 余以乘朔日定小余
step2乘積 = step1余 * 朔日定小余

# Step 3: 滿日法而一，為先行分
先行分 = step2乘積 // 日法
先行分余 = step2乘積 % 日法

# Step 4: 不盡者，半法已上收成一，已下者棄之
if 先行分余 >= 日法 / 2:
    先行分 += 1

# Step 5: 若先行分滿日行分而一，為度分
度分 = 先行分
日行分 = 10000  # 日行分 (derived from the problem context)
度 = 度分 // 日行分
分 = 度分 % 日行分

# Step 6: 以減朔日夜半日所在度分
月所在度分 = Fraction(度 * 日行分 + 分, 1) - 朔日夜半日所在度分

# Step 7: 若度分不足減，加往宿度
if 月所在度分 < 0:
    月所在度分 += 日法

# Step 8: 其分不足減者，退一度為行分而減之
月所在度 = 月所在度分 // 日行分
月所在分 = 月所在度分 % 日行分

# Final result
a = 月所在度 + Fraction(月所在分, 日行分)
print(f"在鬥 {a} 度。")


"""


### Explanation of the Code:
1. **Step 1:** Subtract `朔月行定分` from `章歲` to get the remainder.
2. **Step 2:** Multiply the remainder by `朔日定小余`.
3. **Step 3:** Divide the product by `日法` to get the integer part (`先行分`) and the remainder.
4. **Step 4:** If the remainder is greater than or equal to half of `日法`, increment `先行分` by 1.
5. **Step 5:** Convert `先行分` into degrees (`度`) and fractions (`分`) using `日行分`.
6. **Step 6:** Subtract the given `朔日夜半日所在度分` from the calculated degree and fraction.
7. **Step 7:** If the result is negative, add `日法` to adjust.
8. **Step 8:** If the fraction is insufficient, adjust by reducing one degree and recalculating.

This will give the location of the moon at the specified time.
"""


"""
Variable 'a' has wrong value. Expected: 333/70, Actual: 1537/1000"""
