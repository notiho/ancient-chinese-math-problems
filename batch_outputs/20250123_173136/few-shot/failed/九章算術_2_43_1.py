"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤銖率之，問︰各幾何？
反其率術曰：以錢數為法，所率為實，實如法而一。不滿法者反以實減法，法少，實多。二物各以所得多少之數乘法實，即物數。
荅曰：其 a鈞 ， b銖 一錢。 其 c石 ， d銖 一錢。
"""

"""
This problem is quite complex and involves ancient Chinese units of measurement and monetary calculations. Let's break it down step by step and translate it into Python code.

### Problem Breakdown:
- You have **13,970 coins** and are buying **1 shi, 2 jun, 28 jin, 3 liang, and 5 zhu** of silk.
- The goal is to calculate the price per zhu (smallest unit of weight) and determine the rate of cost for the silk.

### Procedure:
The procedure ("反其率術") involves reversing the rate:
1. Use the total money as the divisor (法, "the law").
2. Use the total weight as the dividend (實, "the reality").
3. Divide the total weight by the total money to get the rate per zhu.
4. If the result is not exact, adjust by subtracting the remainder from the divisor.

Finally, calculate the cost per unit of weight based on the derived rate.

---

### Python Code Implementation:


"""


from fractions import Fraction

# 出錢一萬三千九百七十
錢數 = 13970

# 買絲一石二鈞二十八斤三兩五銖
# Convert all units to 銖 (zhu), the smallest unit:
# 1 石 = 120 斤, 1 斤 = 16 兩, 1 兩 = 24 銖
石 = 1
鈞 = 2
斤 = 28
兩 = 3
銖 = 5

# Total weight in 銖
總銖數 = (石 * 120 * 16 * 24) + (鈞 * 16 * 24) + (斤 * 24) + (兩 * 24) + 銖

# 反其率術: Calculate the rate per 銖
# 以錢數為法
法 = 錢數

# 所率為實
實 = 總銖數

# 實如法而一
銖率 = Fraction(實, 法)

# Output the rate per 銖
a = 銖率.numerator  # 鈞 part of the rate
b = 銖率.denominator  # 銖 part of the rate

# Convert the rate back to 石 and 銖 for the final answer
c = a // (120 * 16 * 24)  # 石
d = a % (120 * 16 * 24)  # Remaining 銖

print(f"其 {a} 鈞, {b} 銖 一錢。其 {c} 石, {d} 銖 一錢。")


"""


---

### Explanation of the Code:
1. **Unit Conversion**: All units are converted to the smallest unit, `銖`, for easier calculation.
2. **Rate Calculation**: The total weight (`實`) is divided by the total money (`法`) to get the rate per `銖`.
3. **Output**: The rate is expressed in terms of `石` and `銖` for clarity.

### Final Answer:
The output will provide the rate of silk in terms of `石` and `銖` per coin.
"""


"""
Variable 'a' has wrong value. Expected: 3871/2304, Actual: 4327
Variable 'b' has wrong value. Expected: 5, Actual: 1270
Variable 'c' has wrong value. Expected: 10099/7680, Actual: 0
Variable 'd' has wrong value. Expected: 6, Actual: 4327"""
