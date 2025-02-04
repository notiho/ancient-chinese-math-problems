"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤鈞率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a斤 ，鈞 b錢 。其 c石 ，鈞 d錢 。
"""

"""
This problem involves calculating the price per unit weight (jin and jun) for a given amount of money spent on silk. Let's translate the procedure into Python code step by step.

### Problem Breakdown:
- Total money spent: 13,970 (in some currency).
- Total silk purchased: 1 shi, 2 jun, 28 jin, 3 liang, and 5 zhu.
- The goal is to calculate the price per jin and per jun.

### Procedure:
1. Place the quantities of shi, jun, jin, liang, and zhu as the divisor (法).
2. Multiply the total money by the respective unit rate to get the dividend (實).
3. Divide the dividend by the divisor to get the unit price.
4. If the divisor is not fully divisible, adjust the calculation as described.

Now, let's implement this in Python.


"""


from fractions import Fraction

# 出錢一萬三千九百七十
錢數 = 13970

# 買絲一石二鈞二十八斤三兩五銖
石 = 1
鈞 = 2
斤 = 28
兩 = 3
銖 = 5

# 將所有單位轉換為銖 (1 石 = 120 鈞, 1 鈞 = 30 斤, 1 斤 = 16 兩, 1 兩 = 24 銖)
總銖 = (
    石 * 120 * 30 * 16 * 24 +
    鈞 * 30 * 16 * 24 +
    斤 * 16 * 24 +
    兩 * 24 +
    銖
)

# 計算每銖的價格
每銖價格 = Fraction(錢數, 總銖)

# 計算每斤的價格 (1 斤 = 16 兩 = 384 銖)
每斤價格 = 每銖價格 * 384

# 計算每鈞的價格 (1 鈞 = 30 斤 = 11520 銖)
每鈞價格 = 每銖價格 * 11520

# 輸出結果
a = 每斤價格
b = 每鈞價格

print(f"其 {a} 錢 / 斤 ，鈞 {b} 錢 / 鈞 。")


"""


### Explanation:
1. Convert all units of weight into the smallest unit (zhu) for consistent calculations.
2. Use the total money and total weight (in zhu) to calculate the price per zhu.
3. Convert the price per zhu into the price per jin and per jun using their respective conversion factors.
4. Use the `Fraction` class to ensure precise calculations without floating-point errors.

### Answer:
- `a` is the price per jin.
- `b` is the price per jun.
"""


"""
Variable 'a' has wrong value. Expected: 979/128, Actual: 5364480/1416269
Variable 'b' has wrong value. Expected: 2012, Actual: 160934400/1416269
Missing variable in output: 'c'
Missing variable in output: 'd'"""
