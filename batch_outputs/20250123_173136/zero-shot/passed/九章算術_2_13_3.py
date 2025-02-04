"""
今有粟一十斗八升、五分升之二，欲為麥。問︰得幾何？
術曰：以粟求菽、答、麻、麥，皆九之，十而一。
荅曰：為麥 a斗 。
"""

"""
To solve this problem, we need to convert the given amount of 粟 (millet) into 麥 (wheat). The rule provided states that to convert 粟 into 麥, we multiply by 9/10.

The given amount of 粟 is 10斗8升 and 2/5升. First, we convert everything into a single unit (升). Since 1斗 = 10升, the total amount in 升 is:

10斗 = 100升  
8升 = 8升  
2/5升 = 2/5升  

Thus, the total amount of 粟 in 升 is:  
100 + 8 + 2/5 = 108 + 2/5升.

Now, we apply the conversion ratio (9/10) to find the equivalent amount of 麥 in 升. Finally, we convert the result back into 斗.

Here is the Python code to compute the answer:


"""


from fractions import Fraction

# Given data
粟_in_斗 = 10
粟_in_升 = 8
粟_in_分升 = Fraction(2, 5)

# Convert everything to 升
total_粟_in_升 = (粟_in_斗 * 10) + 粟_in_升 + 粟_in_分升

# Conversion ratio from 粟 to 麥
conversion_ratio = Fraction(9, 10)

# Calculate 麥 in 升
total_麥_in_升 = total_粟_in_升 * conversion_ratio

# Convert 麥 back to 斗 and 升
a = total_麥_in_升 / 10  # Convert 升 to 斗

# The answer is stored in variable 'a'
a


"""


The variable `a` will contain the result in 斗 (including fractional parts).
"""


"""
"""
