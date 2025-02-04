"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤鈞率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a斤 ，鈞 b錢 。其 c石 ，鈞 d錢 。
"""

"""
This problem involves calculating the price per unit weight (jin and jun) for silk based on the total cost and the total weight purchased. Let's break this down step by step and encode it in Python.

### Problem Breakdown:
- **Total money spent**: 13,970 (in qian).
- **Total weight purchased**: 1 shi, 2 jun, 28 jin, 3 liang, 5 zhu.
- **Goal**: Calculate the price per jin and the price per jun.

### Conversion Factors:
1 shi = 4 jun  
1 jun = 30 jin  
1 jin = 16 liang  
1 liang = 24 zhu  

### Procedure:
1. Convert the total weight into a single unit (jin).
2. Calculate the price per jin by dividing the total money by the total weight in jin.
3. Convert the price per jin into the price per jun.

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Total money spent (in qian)
total_money = 13970

# Total weight purchased: 1 shi, 2 jun, 28 jin, 3 liang, 5 zhu
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

# Step 1: Convert total weight to jin
total_jin = (
    shi * shi_to_jun * jun_to_jin +
    jun * jun_to_jin +
    jin +
    Fraction(liang, jin_to_liang) +
    Fraction(zhu, jin_to_liang * liang_to_zhu)
)

# Step 2: Calculate price per jin
price_per_jin = Fraction(total_money, total_jin)

# Step 3: Calculate price per jun
price_per_jun = price_per_jin * jun_to_jin

# Results
a = price_per_jin  # Price per jin
b = price_per_jun  # Price per jun

# Output results
print(f"Price per jin: {a} qian")
print(f"Price per jun: {b} qian")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Weight Conversion**: The total weight is converted into jin using the provided conversion factors. Fractions are used to ensure precision when dealing with smaller units like liang and zhu.
2. **Price Calculation**: The price per jin is calculated by dividing the total money by the total weight in jin. The price per jun is then derived by multiplying the price per jin by the number of jin in a jun.
3. **Output**: The results are stored in variables `a` (price per jin) and `b` (price per jun).

### Example Output:
If you run the code, it will calculate the price per jin and per jun based on the given data. The results will be expressed as fractions for precision.
"""


"""
Variable 'a' has wrong value. Expected: 979/128, Actual: 5364480/79949
Variable 'b' has wrong value. Expected: 2012, Actual: 160934400/79949
Missing variable in output: 'c'
Missing variable in output: 'd'"""
