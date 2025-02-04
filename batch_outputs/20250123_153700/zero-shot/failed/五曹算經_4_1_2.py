"""
今有官田九百畝凡一步收粟三升二合。問：計㡬何？
術曰：列田九百畝以二百四十步乘之得二十一萬六千步以三升二合乘之即得。
答曰： a斛 。
"""

"""
To solve this problem, we will calculate the total amount of grain harvested from the given area of land. Here's the Python code to compute the value of "a" (the total amount of grain in "斛"):


"""


from fractions import Fraction

# Given values
田 = 900  # 畝
每畝步 = 240  # 每畝有240步
每步收粟 = Fraction(3, 1) + Fraction(2, 10)  # 每步收粟3升2合 (2合 = 2/10升)

# Total steps in the field
總步數 = 田 * 每畝步

# Total grain harvested in 升
總收粟 = 總步數 * 每步收粟

# Convert 升 to 斛 (1斛 = 10升)
a = 總收粟 / 10

# The result is stored in variable "a"


"""


### Explanation:
1. **田**: The total area of land is 900 畝.
2. **每畝步**: Each 畝 contains 240 steps.
3. **每步收粟**: Each step yields 3 升 and 2 合. Since 1 合 = 1/10 升, this is represented as `3 + 2/10 = 3.2 升`.
4. **總步數**: The total number of steps is calculated as `田 * 每畝步`.
5. **總收粟**: The total grain harvested in 升 is `總步數 * 每步收粟`.
6. **a**: The total grain in 斛 is obtained by dividing the total grain in 升 by 10 (since 1 斛 = 10 升).

The variable `a` will contain the final answer in 斛.
"""


"""
Variable 'a' has wrong value. Expected: 6912, Actual: 69120"""
