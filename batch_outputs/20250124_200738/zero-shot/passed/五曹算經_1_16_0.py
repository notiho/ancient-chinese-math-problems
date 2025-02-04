"""
今有圓田周七十八步徑二十六步。問：為田㡬何？
術曰：先列周七十八步半之得三十九步又列徑二十六步半之得一十三步二位相乘得五百七步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

"""
To solve this problem, we need to calculate the area of a circular field given its circumference (周) and diameter (徑). The formula for the area of a circle is:

\[
\text{Area} = \frac{\text{Circumference} \times \text{Diameter}}{4\pi}
\]

However, the ancient Chinese method simplifies this by using an approximation for \(\pi\) (likely \(3\)) and calculating the area as:

\[
\text{Area} = \frac{\text{Circumference} \times \text{Diameter}}{4}
\]

The result is then converted into 畝 (mu) and 步 (bu), where 1 畝 = 240 步.

Here is the Python code to compute the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
circumference = 78  # 周 in 步
diameter = 26       # 徑 in 步

# Step 1: Compute half of the circumference and half of the diameter
half_circumference = Fraction(circumference, 2)
half_diameter = Fraction(diameter, 2)

# Step 2: Multiply the two halves to get the area in 步^2
area_in_bu_squared = half_circumference * half_diameter

# Step 3: Convert the area into 畝 and 步
mu = area_in_bu_squared // 240  # Integer part is in 畝
bu = area_in_bu_squared % 240   # Remainder is in 步

# Assign the results to variables
a = mu
b = bu

# Outputs
a, b
#----- content ends here -----


"""


### Explanation of the Code:
1. **Step 1**: Compute half of the circumference and half of the diameter as described in the problem.
2. **Step 2**: Multiply these two values to get the area in 步².
3. **Step 3**: Convert the area into 畝 and 步 using the conversion \(1 \text{畝} = 240 \text{步}\).

### Final Answer:
The variables `a` and `b` will contain the values of 畝 and 步, respectively.
"""


"""
"""
