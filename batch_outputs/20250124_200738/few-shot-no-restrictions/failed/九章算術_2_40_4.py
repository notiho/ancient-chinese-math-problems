"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤鈞率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a斤 ，鈞 b錢 。其 c石 ，鈞 d錢 。
"""

"""
This problem involves calculating the price per unit weight (jin and jun) for a given amount of money and silk. Let's break it down step by step and translate it into Python code.

### Problem Breakdown:
- **Total money spent**: 13,970 (in some monetary unit).
- **Total weight of silk purchased**: 1 shi, 2 jun, 28 jin, 3 liang, and 5 zhu.
- **Goal**: Calculate the price per jin and per jun.

### Procedure:
1. Convert the total weight into a single unit (e.g., zhu, the smallest unit).
   - 1 shi = 4 jun
   - 1 jun = 30 jin
   - 1 jin = 16 liang
   - 1 liang = 24 zhu
2. Use the total weight to calculate the price per unit (jin and jun).
3. The formula for the price per unit is:
   - Multiply the total money by the unit conversion factor to get the "real value."
   - Divide the real value by the total weight in the chosen unit.

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Total money spent
total_money = 13970

# Conversion factors
shi_to_jun = 4
jun_to_jin = 30
jin_to_liang = 16
liang_to_zhu = 24

# Total weight in various units
shi = 1
jun = 2
jin = 28
liang = 3
zhu = 5

# Convert total weight to zhu (smallest unit)
total_weight_in_zhu = (
    shi * shi_to_jun * jun_to_jin * jin_to_liang * liang_to_zhu +
    jun * jun_to_jin * jin_to_liang * liang_to_zhu +
    jin * jin_to_liang * liang_to_zhu +
    liang * liang_to_zhu +
    zhu
)

# Convert total weight to jin and jun
total_weight_in_jin = total_weight_in_zhu / (jin_to_liang * liang_to_zhu)
total_weight_in_jun = total_weight_in_zhu / (jun_to_jin * jin_to_liang * liang_to_zhu)

# Calculate price per jin and per jun
price_per_jin = Fraction(total_money, total_weight_in_jin)
price_per_jun = Fraction(total_money, total_weight_in_jun)

# Results
a = price_per_jin
b = price_per_jun

print(f"Price per jin: {a} money")
print(f"Price per jun: {b} money")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Weight Conversion**: The total weight is converted into the smallest unit (zhu) for precise calculations.
2. **Price Calculation**: The price per jin and per jun is calculated by dividing the total money by the total weight in the respective unit.
3. **Fraction Module**: The `Fraction` class is used to ensure exact results without floating-point errors.

### Answer:
- `a`: Price per jin (in money).
- `b`: Price per jun (in money).
"""


"""
Code error: both arguments should be Rational instances"""
