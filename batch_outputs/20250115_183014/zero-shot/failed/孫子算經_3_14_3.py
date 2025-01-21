"""
今有粟一十二萬八千九百四十斛九斗三合，出與人買絹一匹，直粟三斛五斗七升。問：絹幾何？
術曰：置粟一十二萬八千九百四十斛九斗三合為實，以三斛五斗七升為法，除之，得匹餘四十之所得，又以法除之，即得。
答曰： a匹 b丈 。
"""

"""
To solve this problem, we need to calculate how many pieces of silk ("絹") can be bought with the given amount of grain ("粟"). The total amount of grain is 128,940斛9斗3合, and the price of one piece of silk is 3斛5斗7升. We will compute the number of silk pieces (a) and the remainder in terms of the price unit (b).

### Conversion of units:
1 斛 = 10 斗  
1 斗 = 10 升  
1 升 = 10 合  

### Given:
Total grain = 128,940斛9斗3合  
Price of one piece of silk = 3斛5斗7升  

### Steps:
1. Convert the total grain and the price of one piece of silk into the smallest unit (合).
2. Perform integer division to find the number of silk pieces (a).
3. Compute the remainder in terms of the price unit (b).

Here is the Python code:


"""


from fractions import Fraction

# Conversion factors
hu_to_dou = 10
dou_to_sheng = 10
sheng_to_he = 10

# Total grain in smallest unit (合)
total_grain_hu = 128940
total_grain_dou = 9
total_grain_he = 3
total_grain_in_he = (total_grain_hu * hu_to_dou * dou_to_sheng * sheng_to_he +
                     total_grain_dou * dou_to_sheng * sheng_to_he +
                     total_grain_he)

# Price of one piece of silk in smallest unit (合)
price_hu = 3
price_dou = 5
price_sheng = 7
price_in_he = (price_hu * hu_to_dou * dou_to_sheng * sheng_to_he +
               price_dou * dou_to_sheng * sheng_to_he +
               price_sheng * sheng_to_he)

# Number of silk pieces (a) and remainder in smallest unit
a = total_grain_in_he // price_in_he
remainder_in_he = total_grain_in_he % price_in_he

# Convert remainder back to the price unit (b)
b_hu = remainder_in_he // (hu_to_dou * dou_to_sheng * sheng_to_he)
remainder_in_he %= (hu_to_dou * dou_to_sheng * sheng_to_he)

b_dou = remainder_in_he // (dou_to_sheng * sheng_to_he)
remainder_in_he %= (dou_to_sheng * sheng_to_he)

b_sheng = remainder_in_he // sheng_to_he
b_he = remainder_in_he % sheng_to_he

# Final result
b = Fraction(b_hu) + Fraction(b_dou, hu_to_dou) + Fraction(b_sheng, hu_to_dou * dou_to_sheng) + Fraction(b_he, hu_to_dou * dou_to_sheng * sheng_to_he)

# Output variables
a, b


"""


### Explanation of the Output:
- `a` is the number of silk pieces that can be bought.
- `b` is the remainder in terms of the price unit (expressed as a fraction of a "piece of silk").
"""


"""
Variable 'b' has wrong value. Expected: 18/5, Actual: 3213/1000"""
