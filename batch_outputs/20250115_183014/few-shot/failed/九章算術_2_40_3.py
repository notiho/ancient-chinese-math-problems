"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤鈞率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a斤 ，鈞 b錢 。其 c石 ，鈞 d錢 。
"""

"""
This problem involves calculating the price per unit weight (e.g., per jin, per jun, per shi) based on the total cost and the total weight of silk purchased. Let's translate the procedure into Python code step by step.

### Problem Breakdown:
- Total money spent: 13,970 (in some unit of currency).
- Total weight of silk purchased: 1 shi, 2 jun, 28 jin, 3 liang, 5 zhu.
- The goal is to calculate the price per unit weight (e.g., per jin, per jun, per shi).

### Procedure:
1. Use the total weight (in shi, jun, jin, liang, zhu) as the divisor (法).
2. Multiply the total money (錢數) by the unit weight to get the dividend (實).
3. Divide the dividend by the divisor to get the price per unit weight.
4. If the divisor is not a whole number, adjust the calculation accordingly.

### Conversion Factors:
- 1 shi = 4 jun
- 1 jun = 30 jin
- 1 jin = 16 liang
- 1 liang = 24 zhu

Now, let's implement the procedure in Python:


"""


from fractions import Fraction

# Total money spent
錢數 = 13970

# Total weight in shi, jun, jin, liang, zhu
石 = 1
鈞 = 2
斤 = 28
兩 = 3
銖 = 5

# Conversion factors
鈞每石 = 4
斤每鈞 = 30
兩每斤 = 16
銖每兩 = 24

# Convert total weight to zhu (smallest unit)
總銖 = (
    石 * 鈞每石 * 斤每鈞 * 兩每斤 * 銖每兩 +
    鈞 * 斤每鈞 * 兩每斤 * 銖每兩 +
    斤 * 兩每斤 * 銖每兩 +
    兩 * 銖每兩 +
    銖
)

# Calculate price per zhu
每銖錢 = Fraction(錢數, 總銖)

# Convert price per zhu to price per jin and per shi
每斤錢 = 每銖錢 * 銖每兩 * 兩每斤
每石錢 = 每斤錢 * 斤每鈞 * 鈞每石

# Results
a = 每斤錢  # Price per jin
b = 每銖錢 * 銖每兩 * 兩每斤 * 鈞每石


"""

"""


"""
Variable 'a' has wrong value. Expected: 979/128, Actual: 5364480/79949
Variable 'b' has wrong value. Expected: 2012, Actual: 21457920/79949
Missing variable in output: 'c'
Missing variable in output: 'd'"""
