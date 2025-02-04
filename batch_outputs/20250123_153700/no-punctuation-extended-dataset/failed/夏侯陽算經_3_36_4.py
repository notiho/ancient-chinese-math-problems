"""
今有米三千四百六十三斛四斗四升七合一勺毎斗身内抽三合充腳問正腳各幾何
術曰先置米數以一斗三合除之得正米以三因之得腳米
答曰正 a斛 腳 b斛
"""

"""
Suppose there are 3463 hu, 4 dou, 4 sheng, 7 ge, and 1 jue of rice.
For every dou, 3 ge are taken out to form the "foot rice" (extra rice).
Question: how much is the "proper rice" and how much is the "foot rice"?

The procedure says: First, place the total amount of rice.
Divide it by 1 dou and 3 ge to obtain the proper rice.
Multiply it by 3 to obtain the foot rice.

Answer: the proper rice is *a* hu, and the foot rice is *b* hu.
"""

# 米數：3463斛4斗4升7合1勺
# Convert everything to ge (smallest unit for calculation)
米數 = (
    3463 * 10 * 10 * 10 * 10  # Convert hu to ge
    + 4 * 10 * 10 * 10  # Convert dou to ge
    + 4 * 10 * 10  # Convert sheng to ge
    + 7 * 10  # Convert ge
    + 1  # Add jue
)

# 每斗身內抽3合 (1斗 = 1000合, so 1斗3合 = 1003合)
一斗三合 = 10 * 10 * 10 + 3 * 10  # Convert 1斗3合 to ge

# 以一斗三合除之，得正米
正米 = Fraction(米數, 一斗三合)

# 以三因之，得腳米
腳米 = Fraction(3 * 正米, 1)

# Convert results back to hu, dou, sheng, ge, jue
def convert_to_units(total_ge):
    hu = total_ge // (10 * 10 * 10 * 10)
    remaining = total_ge % (10 * 10 * 10 * 10)
    dou = remaining // (10 * 10 * 10)
    remaining %= (10 * 10 * 10)
    sheng = remaining // (10 * 10)
    remaining %= (10 * 10)
    ge = remaining // 10
    jue = remaining % 10
    return hu, dou, sheng, ge, jue

# Convert 正米 and 腳米 to hu, dou, sheng, ge, jue
a = convert_to_units(正米.numerator // 正米.denominator)
b = convert_to_units(腳米.numerator // 腳米.denominator)
"""
Variable 'a' has wrong value. Expected: 336257/100, Actual: (3, 3, 6, 2, 5)
Variable 'b' has wrong value. Expected: 1008771/10000, Actual: (10, 0, 8, 7, 7)"""
