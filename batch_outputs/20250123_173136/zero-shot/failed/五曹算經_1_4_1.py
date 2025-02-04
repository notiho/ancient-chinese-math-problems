"""
今有腰鼓田從八十二步两頭各廣三十步中央廣十二步。問：為田㡬何？
術曰：并三廣得七十二步以三除之得二十四步以從八十二步乘之得一千九百六十八步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem describes a trapezoidal field with two parallel sides of lengths 30 steps and 12 steps, and the distance between them is 82 steps. The goal is to calculate the area of the field in terms of "畝" (mu) and "步" (steps).

We will use the formula for the area of a trapezoid:

\[
\text{Area} = \frac{\text{Sum of parallel sides} \times \text{Height}}{2}
\]

Then, we convert the area into "畝" and "步" using the conversion factor: 1 畝 = 240 步.

Here is the Python code:


"""


from fractions import Fraction

# Given values
parallel_side1 = 30  # in steps
parallel_side2 = 12  # in steps
height = 82  # in steps
conversion_factor = 240  # 1 畝 = 240 步

# Calculate the area in steps
area_in_steps = Fraction(parallel_side1 + parallel_side2, 2) * height

# Convert the area into 畝 and 步
a = area_in_steps // conversion_factor  # Whole 畝
b = area_in_steps % conversion_factor  # Remaining 步

# Results
a, b


"""


### Explanation:
1. We calculate the average of the two parallel sides: \((30 + 12) / 2 = 21\).
2. Multiply the average by the height: \(21 \times 82 = 1722\) steps.
3. Convert the total area into "畝" and "步":
   - Divide \(1722\) by \(240\) to get the whole number of 畝 (\(a\)).
   - Take the remainder to get the remaining 步 (\(b\)).

### Final Answer:
The values of \(a\) and \(b\) will be stored in the variables `a` and `b`.
"""


"""
Variable 'a' has wrong value. Expected: 8, Actual: 7
Variable 'b' has wrong value. Expected: 48, Actual: 42"""
