"""
今有豆八百四十九斛，凡豆九斗易麻七斗。問：得麻㡬何？
術曰：列豆八百四十九斛，以七十乘之得五萬九千四百三十斛，以九十除之即得。
答曰： a斛 奇 b升 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves converting 849斛 of beans into 麻 (hemp) based on the exchange rate provided: 9斗 of beans can be exchanged for 7斗 of hemp. We need to calculate how much hemp (麻) can be obtained.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
beans = 849  # in 斛
exchange_rate_beans = 9  # 斗 of beans
exchange_rate_hemp = 7  # 斗 of hemp

# Convert 斛 to 斗 (1 斛 = 10 斗)
beans_in_dou = beans * 10  # Total beans in 斗

# Calculate total hemp in 斗
hemp_in_dou = Fraction(beans_in_dou * exchange_rate_hemp, exchange_rate_beans)

# Convert hemp back to 斛 and 升
a = hemp_in_dou // 10  # Whole 斛
b = hemp_in_dou % 10  # Remaining 升

# Results
a = int(a)  # Whole 斛
b = int(b)  # Remaining 升
#----- content ends here -----


"""


### Explanation:
1. **Conversion of units**: Since 1斛 = 10斗, we first convert the total beans from 斛 to 斗.
2. **Exchange calculation**: Using the exchange rate (9斗 of beans for 7斗 of hemp), we calculate the total amount of hemp in 斗.
3. **Convert back to 斛 and 升**: Since 1斛 = 10斗, we calculate how many whole 斛 (a) and remaining 升 (b) of hemp can be obtained.

### Final Answer:
The variables `a` and `b` will contain the result in 斛 and 升, respectively.
"""


"""
Variable 'a' has wrong value. Expected: 660333/1000, Actual: 660"""
