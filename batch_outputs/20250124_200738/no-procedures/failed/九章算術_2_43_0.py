"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤銖率之，問︰各幾何？
荅曰：其 a鈞 ， b銖 一錢。 其 c石 ， d銖 一錢。
"""

"""
This problem involves calculating the price per unit weight of silk based on the total cost and the total weight. Let's break it down step by step.

### Problem:
- Total money spent: 13,970 (in some monetary unit).
- Total weight of silk: 1 shi, 2 jun, 28 jin, 3 liang, 5 zhu.
- Question: What is the price per zhu for each unit (jun and shi)?

---

### Solution in Python:


"""

#----- content starts here -----

from fractions import Fraction

# Total money spent
total_money = 13970

# Total weight of silk in zhu
# 1 shi = 4 jun, 1 jun = 30 jin, 1 jin = 16 liang, 1 liang = 24 zhu
shi = 1
jun = 2
jin = 28
liang = 3
zhu = 5

# Convert everything to zhu
total_weight_in_zhu = (
    shi * 4 * 30 * 16 * 24 +
    jun * 30 * 16 * 24 +
    jin * 16 * 24 +
    liang * 24 +
    zhu
)

# Price per zhu
price_per_zhu = Fraction(total_money, total_weight_in_zhu)

# Price per jun (1 jun = 30 jin = 30 * 16 * 24 zhu)
price_per_jun = price_per_zhu * (30 * 16 * 24)

# Price per shi (1 shi = 4 jun = 4 * 30 * 16 * 24 zhu)
price_per_shi = price_per_zhu * (4 * 30 * 16 * 24)

# Convert price per jun and price per shi into "zhu per qian" format
# 1 qian = 10 zhu
a = price_per_jun.numerator // price_per_jun.denominator  # Whole qian for jun
b = price_per_jun.numerator % price_per_jun.denominator   # Remaining zhu for jun

c = price_per_shi.numerator // price_per_shi.denominator  # Whole qian for shi
d = price_per_shi.numerator % price_per_shi.denominator   # Remaining zhu for shi

# Output results
print(f"Price per jun: {a} qian, {b} zhu")
print(f"Price per shi: {c} qian, {d} zhu")
#----- content ends here -----


"""


---

### Explanation:
1. **Weight Conversion**: Convert the total weight into the smallest unit (zhu) for precision.
2. **Price per Zhu**: Divide the total money by the total weight in zhu to get the price per zhu.
3. **Price per Jun and Shi**: Multiply the price per zhu by the number of zhu in a jun and a shi, respectively.
4. **Formatting**: Convert the price into "qian and zhu" format, where 1 qian = 10 zhu.

---

### Final Answer:
- Price per jun: `a qian, b zhu`.
- Price per shi: `c qian, d zhu`.
"""


"""
Variable 'a' has wrong value. Expected: 3871/2304, Actual: 2012
Variable 'b' has wrong value. Expected: 5, Actual: 77012
Variable 'c' has wrong value. Expected: 10099/7680, Actual: 8051
Variable 'd' has wrong value. Expected: 6, Actual: 68201"""
