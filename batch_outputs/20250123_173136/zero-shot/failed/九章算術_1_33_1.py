"""
又有宛田，下周九十九步，徑五十一步。問：為田幾何？
術曰：以徑乘周，四而一。
荅曰： a畝 。
"""

"""
To solve this problem, we need to calculate the area of a circular field (宛田). The problem provides the circumference (周) as 99 steps and the diameter (徑) as 51 steps. The formula provided in the problem is:

```
Area = (Diameter × Circumference) ÷ 4
```

The unit of the result is in 畝 (a traditional Chinese unit of area). Let's translate this into Python code:


"""


from fractions import Fraction

# Given values
circumference = 99  # 周 (steps)
diameter = 51       # 徑 (steps)

# Calculate the area
a = Fraction(diameter * circumference, 4)

# The area in 畝
a


"""


The variable `a` will contain the area of the field in 畝 as a fraction.
"""


"""
Variable 'a' has wrong value. Expected: 1683/320, Actual: 5049/4"""
