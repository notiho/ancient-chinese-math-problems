"""
今有粟一十二萬八千九百四十斛九斗三合，出與人買絹一匹，直粟三斛五斗七升。問：絹幾何？
術曰：置粟一十二萬八千九百四十斛九斗三合為實，以三斛五斗七升為法，除之，得匹餘四十之所得，又以法除之，即得。
答曰： a匹 。
"""

"""
To solve this problem, we need to calculate how many pieces of silk ("絹") can be bought with the given amount of grain ("粟"). The total amount of grain is 128,940斛9斗3合, and the price of one piece of silk is 3斛5斗7升. We will compute the number of silk pieces (`a`) using the given values.

Here is the Python code:


"""


from fractions import Fraction

# Convert all units to the smallest unit (合)
# 1 斛 = 10 斗, 1 斗 = 10 升, 1 升 = 10 合
total_grain = 128940 * 10 * 10 + 9 * 10 + 3  # Convert 128,940斛9斗3合 to 合
price_per_silk = 3 * 10 * 10 + 5 * 10 + 7  # Convert 3斛5斗7升 to 合

# Calculate the number of silk pieces
a = Fraction(total_grain, price_per_silk)

# The result is in terms of silk pieces
print(f"a = {a} pieces of silk")


"""


### Explanation of the Code:
1. **Unit Conversion**: We first convert all the given quantities into the smallest unit, 合, for consistent calculations:
   - 1 斛 = 10 斗, 1 斗 = 10 升, 1 升 = 10 合.
   - Total grain is converted to 合: \( 128,940 \times 10 \times 10 + 9 \times 10 + 3 \).
   - Price per silk is converted to 合: \( 3 \times 10 \times 10 + 5 \times 10 + 7 \).

2. **Division**: We divide the total grain by the price per silk to determine how many pieces of silk can be bought.

3. **Fraction Representation**: The `Fraction` class ensures that the result is represented as an exact fraction if the division does not result in an integer.

### Final Answer:
The variable `a` will store the number of silk pieces that can be bought.
"""


"""
Variable 'a' has wrong value. Expected: 361179/10, Actual: 4298031/119"""
