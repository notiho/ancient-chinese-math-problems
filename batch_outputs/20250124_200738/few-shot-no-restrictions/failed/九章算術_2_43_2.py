"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤銖率之，問︰各幾何？
反其率術曰：以錢數為法，所率為實，實如法而一。不滿法者反以實減法，法少，實多。二物各以所得多少之數乘法實，即物數。
荅曰：其 a鈞 ， b銖 一錢。 其 c石 ， d銖 一錢。
"""

"""
This problem involves calculating the price per unit weight (in this case, per "銖") for a given amount of money and a total weight of silk. Let's break it down step by step and encode the solution in Python.

### Problem Breakdown:
- **Given:**
  - Total money: 13,970 (錢)
  - Total weight: 1 石, 2 鈞, 28 斤, 3 兩, 5 銖
- **Goal:**
  - Calculate the price per 銖 (smallest unit of weight).

- **Procedure:**
  - Convert the total weight into 銖 (the smallest unit of weight).
  - Divide the total money by the total weight in 銖 to get the price per 銖.

### Conversion Factors:
1 石 = 4 鈞  
1 鈞 = 30 斤  
1 斤 = 16 兩  
1 兩 = 24 銖  

### Python Code:

"""

#----- content starts here -----

from fractions import Fraction

# Total money
total_money = 13970  # in 錢

# Total weight: 1 石, 2 鈞, 28 斤, 3 兩, 5 銖
石 = 1
鈞 = 2
斤 = 28
兩 = 3
銖 = 5

# Conversion factors
石_to_鈖 = 4 * 30 * 16 * 24
鈞_to_鈖 = 30 * 16 * 24
斤_to_鈖 = 16 * 24
兩_to_銖 = 24

# Convert total weight to 銖
total_weight_in_銖 = (
    石 * 石_to_鈖 +
    鈞 * 鈞_to_鈖 +
    斤 * 斤_to_銖 +
    兩 * 兩_to_銖 +
    銖
)

# Calculate price per 銖
price_per_銖 = Fraction(total_money, total_weight_in_銖)

# Convert price per 銖 back into 鈞 and 錢
銖_to_鈞 = 鈞_to_鈖  # 1 鈞 = 30 斤 * 16 兩 * 24 銖
price_in_鈞 = price_per_銖 * 銖_to_鈞

# Extract integer part (鈞) and fractional part (錢)
a = price_in_鈞.numerator // price_in_鈞.denominator  # Integer part (鈞)
b = price_in_鈞.numerator % price_in_鈞.denominator  # Fractional part (錢)

# Convert price per 銖 back into 石 and 錢
銖_to_石 = 石_to_鈖  # 1 石 = 4 鈞 * 30 斤 * 16 兩 * 24 銖
price_in_石 = price_per_銖 * 銖_to_石

# Extract integer part (石) and fractional part (錢)
c = price_in_石.numerator // price_in_石.denominator  # Integer part (石)
d = price_in_石.numerator % price_in_石.denominator  # Fractional part (錢)

# Output the results
print(f"其 {a} 鈞, {b} 銖 一錢。其 {c} 石, {d} 銖 一錢。")
#----- content ends here -----


"""


### Explanation:
1. **Weight Conversion:** Convert the total weight into the smallest unit (銖) using the given conversion factors.
2. **Price per 銖:** Divide the total money by the total weight in 銖 to get the price per 銖.
3. **Convert Back:** Convert the price per 銖 into larger units (鈞 and 石) for the final answer.

### Output:
The program will calculate and display the price per 鈞 and per 石 in terms of 銖 and 錢.
"""


"""
Code error: name '斤_to_銖' is not defined"""
