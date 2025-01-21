"""
今有長安、洛陽相去九百里，車輪一匝一丈八尺。欲自洛陽至長安。問：輪匝幾何？
術曰：置九百里以三百步乘之，得二十七萬步，又以六尺乘之，得一百六十二萬尺，以車輪一丈八尺為法，除之，即得。
答曰： a 匝。
"""

"""
To solve this problem, we need to calculate how many revolutions ("匝") the wheel makes when traveling from 洛陽 (Luoyang) to 長安 (Chang'an), which are 900 li apart. The wheel circumference is given as 1丈8尺. 

Here is the Python code to compute the answer:


"""


from fractions import Fraction

# Given values
distance_li = 900  # in li
li_to_bu = 300  # 1 li = 300 bu
bu_to_chi = 6  # 1 bu = 6 chi
wheel_circumference = 1 * 10 + 8  # 1丈8尺 = 10尺 + 8尺 = 18尺

# Convert distance from li to chi
distance_chi = distance_li * li_to_bu * bu_to_chi

# Calculate the number of revolutions
a = Fraction(distance_chi, wheel_circumference)

# The result is stored in variable 'a'


"""


### Explanation:
1. Convert the distance from li to chi:
   - \( 1 \, \text{li} = 300 \, \text{bu} \)
   - \( 1 \, \text{bu} = 6 \, \text{chi} \)
   - Total distance in chi: \( 900 \, \text{li} \times 300 \, \text{bu/li} \times 6 \, \text{chi/bu} = 1,620,000 \, \text{chi} \)

2. The wheel circumference is \( 1 \, \text{丈} + 8 \, \text{尺} = 10 \, \text{chi} + 8 \, \text{chi} = 18 \, \text{chi} \).

3. Divide the total distance in chi by the wheel circumference to find the number of revolutions:
   - \( a = \frac{\text{distance in chi}}{\text{wheel circumference}} = \frac{1,620,000}{18} = 90,000 \).

Thus, \( a = 90,000 \, \text{revolutions} \).
"""


"""
"""
