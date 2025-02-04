"""
今有圓田周七十八步徑二十六步。問：為田㡬何？
術曰：先列周七十八步半之得三十九步又列徑二十六步半之得一十三步二位相乘得五百七步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

"""
To solve this problem, we need to calculate the area of a circular field given its circumference (周) and diameter (徑). The formula for the area of a circle is:

\[
\text{Area} = \pi \times r^2
\]

However, the ancient Chinese method approximates the area of a circle using the formula:

\[
\text{Area} = \frac{\text{Circumference} \times \text{Diameter}}{4}
\]

Here, the circumference is 78 steps, and the diameter is 26 steps. The result is expressed in terms of 畝 (mu) and 步 (bu), where 1 畝 = 240 步.

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
circumference = 78  # in steps
diameter = 26       # in steps

# Step 1: Calculate the area using the ancient formula
area_in_bu = Fraction(circumference, 2) * Fraction(diameter, 2)  # 半周乘半徑

# Step 2: Convert the area from 步 (bu) to 畝 (mu) and 步 (bu)
a = area_in_bu // 240  # Number of 畝
b = area_in_bu % 240   # Remaining 步

# Results
a = int(a)  # Convert to integer for 畝
b = int(b)  # Convert to integer for 步
#----- content ends here -----


"""


### Explanation:
1. The circumference is halved to get \( \frac{78}{2} = 39 \) steps.
2. The diameter is halved to get \( \frac{26}{2} = 13 \) steps.
3. Multiply the two halves: \( 39 \times 13 = 507 \) 步².
4. Convert the area into 畝 and 步:
   - \( 507 \div 240 = 2 \) 畝 (quotient)
   - \( 507 \mod 240 = 27 \) 步 (remainder).

### Final Answer:
\[
\text{答曰：} a = 2 \, \text{畝}, \, b = 27 \, \text{步}.
\]
"""


"""
"""
