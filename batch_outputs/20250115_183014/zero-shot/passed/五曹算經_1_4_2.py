"""
今有腰鼓田從八十二步两頭各廣三十步中央廣十二步。問：為田㡬何？
術曰：并三廣得七十二步以三除之得二十四步以從八十二步乘之得一千九百六十八步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the area of a field shaped like a waist drum (a shape with two wider ends and a narrower middle). The formula provided in the problem is used to compute the area.

Here is the Python code:


"""


from fractions import Fraction

# Given values
length = 82  # 長度 (步)
wide1 = 30   # 兩頭的廣度 (步)
wide2 = 12   # 中央的廣度 (步)

# Calculation
combined_width = wide1 + wide1 + wide2  # 并三廣
average_width = Fraction(combined_width, 3)  # 平均廣度
area_in_steps = average_width * length  # 面積 (步)
area_in_acres = area_in_steps / 240  # 以畝法除之 (1 畝 = 240 步)

# Extracting the integer part (畝) and the remainder (步)
a = area_in_acres.numerator // area_in_acres.denominator  # 畝
b = area_in_steps % 240  # 剩餘步數

# Results
a, b


"""


### Explanation:
1. The combined width is calculated by summing the widths of the two ends and the middle.
2. The average width is obtained by dividing the combined width by 3.
3. The area in steps is calculated by multiplying the average width by the length.
4. The area in acres is calculated by dividing the area in steps by 240 (since 1 畝 = 240 步).
5. The integer part of the area in acres is the number of 畝 (a), and the remainder in steps is the number of 步 (b).

### Final Answer:
The values of `a` (畝) and `b` (步) will be computed when the code is run.
"""


"""
"""
