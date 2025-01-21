"""
今有粟一十二萬八千九百四十斛九斗三合，出與人買絹一匹，直粟三斛五斗七升。問：絹幾何？
術曰：置粟一十二萬八千九百四十斛九斗三合為實，以三斛五斗七升為法，除之，得匹餘四十之所得，又以法除之，即得。
答曰： a匹 b丈 。
"""

"""
To solve this problem, we need to calculate how many pieces of silk ("絹") can be purchased with the given amount of grain ("粟"). The total amount of grain is 128,940斛9斗3合, and the price of one piece of silk is 3斛5斗7升. We will compute the number of silk pieces (`a`) and the remaining fraction of a silk piece in terms of "丈" (`b`).

### Definitions:
1 斛 = 10 斗  
1 斗 = 10 升  
1 升 = 10 合  

### Conversion of units:
We first convert all quantities into the smallest unit, 合, to simplify calculations.

### Python Code:

"""


from fractions import Fraction

# Total grain in 合
total_grain = (128940 * 10 * 10) + (9 * 10) + 3  # Convert 128,940斛9斗3合 to 合

# Price of one piece of silk in 合
price_per_silk = (3 * 10 * 10) + (5 * 10) + 7  # Convert 3斛5斗7升 to 合

# Calculate the number of silk pieces (a) and the remainder in 合
a = total_grain // price_per_silk  # Integer division to get the number of full silk pieces
remainder = total_grain % price_per_silk  # Remainder in 合

# Convert the remainder to 丈 (fraction of a silk piece)
b = Fraction(remainder, price_per_silk)

# Results
print(f"a = {a} 匹")
print(f"b = {b} 丈")


"""


### Explanation:
1. `total_grain` converts the total amount of grain into 合.
2. `price_per_silk` converts the price of one silk piece into 合.
3. `a` is the integer division of `total_grain` by `price_per_silk`, representing the number of full silk pieces.
4. `remainder` is the leftover grain after buying `a` silk pieces.
5. `b` is the fraction of a silk piece that can be bought with the remaining grain.

### Output:
The variables `a` and `b` will contain the solution:
- `a` is the number of full silk pieces.
- `b` is the fractional part of a silk piece in terms of "丈".
"""


"""
Variable 'b' has wrong value. Expected: 18/5, Actual: 108/119"""
