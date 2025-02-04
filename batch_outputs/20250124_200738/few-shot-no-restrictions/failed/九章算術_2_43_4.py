"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤銖率之，問︰各幾何？
反其率術曰：以錢數為法，所率為實，實如法而一。不滿法者反以實減法，法少，實多。二物各以所得多少之數乘法實，即物數。
荅曰：其 a鈞 ， b銖 一錢。 其 c石 ， d銖 一錢。
"""

"""
This problem involves calculating the unit price (per *zhu*) for silk based on the total cost and total weight. Let's break it down step by step and implement the solution in Python.

### Problem Breakdown:
- **Total money spent**: 13,970 (in some unit of currency).
- **Total weight of silk**: 1 *shi*, 2 *jun*, 28 *jin*, 3 *liang*, and 5 *zhu*.
- The goal is to calculate the price per *zhu* (smallest unit of weight).

### Conversion of weights:
1 *shi* = 4 *jun*  
1 *jun* = 30 *jin*  
1 *jin* = 16 *liang*  
1 *liang* = 24 *zhu*  

Thus, we first convert the total weight into *zhu*.

---

### Python Implementation:


"""

#----- content starts here -----

from fractions import Fraction

# Total money spent
total_money = 13970

# Total weight in various units
shi = 1
jun = 2
jin = 28
liang = 3
zhu = 5

# Conversion factors
shi_to_jun = 4
jun_to_jin = 30
jin_to_liang = 16
liang_to_zhu = 24

# Convert total weight to zhu
total_zhu = (
    shi * shi_to_jun * jun_to_jin * jin_to_liang * liang_to_zhu +
    jun * jun_to_jin * jin_to_liang * liang_to_zhu +
    jin * jin_to_liang * liang_to_zhu +
    liang * liang_to_zhu +
    zhu
)

# Calculate the price per zhu
price_per_zhu = Fraction(total_money, total_zhu)

# Convert the price per zhu back into larger units (jun and zhu)
price_per_jun = price_per_zhu * jun_to_jin * jin_to_liang * liang_to_zhu
price_per_jun_whole = price_per_jun.numerator // price_per_jun.denominator
price_per_jun_remainder = price_per_jun - price_per_jun_whole

price_per_zhu_remainder = price_per_jun_remainder * liang_to_zhu

# Output the results
a = price_per_jun_whole  # Price in jun
b = price_per_zhu_remainder  # Remaining price in zhu

print(f"The price is {a} jun and {b} zhu per unit.")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Weight Conversion**: The total weight is converted into the smallest unit (*zhu*) for easier calculation.
2. **Price Calculation**: The total money is divided by the total weight in *zhu* to get the price per *zhu*.
3. **Unit Conversion**: The price per *zhu* is converted back into larger units (*jun* and *zhu*) for a more interpretable answer.

---

### Final Answer:
The price per unit is expressed in terms of *jun* and *zhu*. Let me know if you need further clarification or adjustments!
"""


"""
Variable 'a' has wrong value. Expected: 3871/2304, Actual: 2012
Variable 'b' has wrong value. Expected: 5, Actual: 1848288/79949
Missing variable in output: 'c'
Missing variable in output: 'd'"""
