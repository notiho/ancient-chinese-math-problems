"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤石率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a鈞 ，石 b錢 。其 c石 ，石 d錢 。
"""

"""
This problem involves calculating the price per unit weight (stone, *shi*) of silk based on the total cost and the total weight. Let's break it down step by step and encode it in Python.

### Problem Breakdown:
1. **Total cost**: 13,970 (in money units).
2. **Total weight**: 1 *shi* 2 *jun* 28 *jin* 3 *liang* 5 *zhu*.
3. **Goal**: Calculate the price per *shi* (stone) and the price per *jin* (catty).

### Conversion of weights:
- 1 *shi* = 4 *jun*.
- 1 *jun* = 30 *jin*.
- 1 *jin* = 16 *liang*.
- 1 *liang* = 24 *zhu*.

### Procedure:
1. Convert the total weight into a single unit (e.g., *zhu*).
2. Calculate the price per *shi* and per *jin* by dividing the total cost by the total weight in the respective units.
3. If there is a remainder, adjust the calculation as described in the problem.

Here is the Python implementation:


"""

#----- content starts here -----

from fractions import Fraction

# Total cost
total_cost = 13970

# Total weight in various units
shi = 1
jun = 2
jin = 28
liang = 3
zhu = 5

# Conversion factors
shi_to_jin = 4 * 30  # 1 shi = 4 jun, 1 jun = 30 jin
jin_to_liang = 16    # 1 jin = 16 liang
liang_to_zhu = 24    # 1 liang = 24 zhu

# Convert total weight to zhu
total_weight_in_zhu = (
    shi * shi_to_jin * jin_to_liang * liang_to_zhu +
    jun * 30 * jin_to_liang * liang_to_zhu +
    jin * jin_to_liang * liang_to_zhu +
    liang * liang_to_zhu +
    zhu
)

# Convert total weight to jin (for price per jin)
total_weight_in_jin = (
    shi * shi_to_jin +
    jun * 30 +
    jin +
    liang / jin_to_liang +
    zhu / (jin_to_liang * liang_to_zhu)
)

# Calculate price per shi (stone)
price_per_shi = Fraction(total_cost, shi + jun / 4 + jin / shi_to_jin + liang / (shi_to_jin * jin_to_liang) + zhu / (shi_to_jin * jin_to_liang * liang_to_zhu))

# Calculate price per jin (catty)
price_per_jin = Fraction(total_cost, total_weight_in_jin)

# Results
a = price_per_jin  # Price per jin
b = price_per_shi  # Price per shi

print(f"Price per jin: {a} money units")
print(f"Price per shi: {b} money units")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Weight Conversion**: The total weight is converted into the smallest unit (*zhu*) for precise calculations. This ensures that all units are accounted for.
2. **Price Calculation**: The price per *shi* and per *jin* is calculated using the total cost divided by the total weight in the respective units.
3. **Fraction Handling**: The `Fraction` class is used to ensure exact results without floating-point errors.

### Output:
The program will output the price per *jin* and per *shi* in terms of money units.
"""


"""
Code error: both arguments should be Rational instances"""
