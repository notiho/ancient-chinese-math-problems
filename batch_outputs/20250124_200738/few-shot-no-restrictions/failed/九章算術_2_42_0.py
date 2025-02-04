"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤兩率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a石 ，兩 b錢 。其 c鈞 ，兩 d錢 。
"""

"""
This problem involves calculating the price per unit weight (stone, jin, etc.) of silk based on the total cost and the total weight. Let's break it down step by step and encode the procedure in Python.

### Problem Breakdown:
- Total money spent: 13,970 (in qian).
- Total weight of silk: 1 stone, 2 jin, 28 jin, 3 liang, 5 zhu.
- The task is to calculate the price per stone and per jin.

### Procedure:
1. Convert the total weight into a single unit (e.g., zhu).
2. Calculate the price per unit weight for both stones and jins.
3. Use the given procedure to handle cases where the weight does not perfectly divide into the total cost.

Below is the Python implementation:


"""

#----- content starts here -----

from fractions import Fraction

# Total money spent (in qian)
total_money = 13970

# Total weight of silk
stones = 1
jins = 2
jin = 28
liang = 3
zhu = 5

# Conversion factors
jin_per_stone = 120  # 1 stone = 120 jin
liang_per_jin = 16   # 1 jin = 16 liang
zhu_per_liang = 24   # 1 liang = 24 zhu

# Convert total weight to zhu
total_weight_in_zhu = (
    stones * jin_per_stone * liang_per_jin * zhu_per_liang +
    jins * liang_per_jin * zhu_per_liang +
    jin * zhu_per_liang +
    liang * zhu_per_liang +
    zhu
)

# Calculate price per zhu
price_per_zhu = Fraction(total_money, total_weight_in_zhu)

# Calculate price per stone
price_per_stone = price_per_zhu * jin_per_stone * liang_per_jin * zhu_per_liang

# Calculate price per jin
price_per_jin = price_per_zhu * liang_per_jin * zhu_per_liang

# Output results
a = price_per_stone.numerator // price_per_stone.denominator  # Integer part of price per stone
b = price_per_stone - a  # Fractional part of price per stone

c = price_per_jin.numerator // price_per_jin.denominator  # Integer part of price per jin
d = price_per_jin - c  # Fractional part of price per jin

print(f"Price per stone: {a} stones, {b} qian")
print(f"Price per jin: {c} jins, {d} qian")
#----- content ends here -----


"""


### Explanation:
1. **Weight Conversion**: The total weight is converted into the smallest unit (zhu) for precise calculations.
2. **Price Calculation**: The price per zhu is calculated by dividing the total money by the total weight in zhu. This is then scaled up to calculate the price per stone and per jin.
3. **Output**: The results are presented as integer and fractional parts for clarity.

### Example Output:
If you run the code, it will calculate the price per stone and per jin based on the given inputs. Let me know if you'd like me to run through the calculations manually!
"""


"""
Variable 'a' has wrong value. Expected: 12893/9216, Actual: 13524
Variable 'b' has wrong value. Expected: 4, Actual: 3252/4327
Variable 'c' has wrong value. Expected: 3871/2880, Actual: 112
Variable 'd' has wrong value. Expected: 5, Actual: 3056/4327"""
