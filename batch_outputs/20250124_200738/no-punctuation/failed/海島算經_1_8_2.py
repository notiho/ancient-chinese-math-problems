"""
今有登山臨邑邑在山南偃矩山上令句高三尺五寸令句端與邑東南隅及東北隅參相直從句端遙望東北隅入下股一丈二尺又施橫句于入股之會從立句端望西北隅入橫句五尺望東南隅入下股一丈八尺又設重矩于上令矩間相去四丈更從立句端望東南隅入上股一丈七尺五寸問邑廣長各幾何
術曰以句高乘東南隅入下股如上股而一所得減句高餘為法以東北隅下股減東南隅下股餘以乘矩間為實實如法而一得邑南北長也求邑廣以入橫句乘矩間為實實如法而一即得邑東西廣
答曰南北長 a里 東西廣 b里 
"""

"""
This problem involves a complex geometric setup with measurements and calculations to determine the length and width of a city (邑) based on observations from a mountain. Below is the translation of the problem and its solution into Python code.


"""

#----- content starts here -----

"""
Suppose there is a mountain overlooking a city. The city lies south of the mountain. 
A carpenter's square is placed on the mountain, with the vertical leg (立句) being 3 chi and 5 cun high. 
The endpoint of the vertical leg aligns with the southeast and northeast corners of the city.

From the endpoint of the vertical leg, looking toward the northeast corner, the line enters the lower horizontal leg (下股) at a distance of 1 zhang and 2 chi. 
A horizontal leg (橫句) is placed at the intersection with the lower leg. 
From the endpoint of the vertical leg, looking toward the northwest corner, the line enters the horizontal leg at 5 chi. 
Looking toward the southeast corner, the line enters the lower horizontal leg at 1 zhang and 8 chi.

A second carpenter's square is placed above the first, with the two squares separated by a distance of 4 zhang. 
From the endpoint of the vertical leg, looking toward the southeast corner, the line enters the upper horizontal leg (上股) at 1 zhang, 7 chi, and 5 cun.

Question: What are the length (north-south) and width (east-west) of the city?

Procedure:
1. To find the north-south length:
   - Multiply the height of the vertical leg by the distance the southeast corner enters the lower horizontal leg (下股入).
   - Divide by the distance the southeast corner enters the upper horizontal leg (上股入).
   - Subtract the height of the vertical leg from the result to get the divisor (法).
   - Subtract the southeast corner's lower horizontal leg entry from the northeast corner's lower horizontal leg entry.
   - Multiply the result by the distance between the two carpenter's squares (矩間) to get the dividend (實).
   - Divide the dividend by the divisor to get the north-south length.

2. To find the east-west width:
   - Multiply the distance the northwest corner enters the horizontal leg (橫句入) by the distance between the two carpenter's squares (矩間) to get the dividend (實).
   - Divide the dividend by the divisor to get the east-west width.

Answer: The north-south length is *a* li, and the east-west width is *b* li.
"""

from fractions import Fraction

# Measurements
句高 = Fraction(3, 1) + Fraction(5, 10)  # 3 chi 5 cun
東北隅下股入 = Fraction(1, 1) * 10 + Fraction(2, 1)  # 1 zhang 2 chi
東南隅下股入 = Fraction(1, 1) * 10 + Fraction(8, 1)  # 1 zhang 8 chi
上股入 = Fraction(1, 1) * 10 + Fraction(7, 1) + Fraction(5, 10)  # 1 zhang 7 chi 5 cun
矩間 = Fraction(4, 1) * 10  # 4 zhang
橫句入 = Fraction(5, 1)  # 5 chi

# Step 1: Calculate the divisor (法) for north-south length
法 = (句高 * 東南隅下股入) / 上股入 - 句高

# Step 2: Calculate the dividend (實) for north-south length
實_南北 = (東北隅下股入 - 東南隅下股入) * 矩間

# Step 3: Calculate the north-south length
南北長 = 實_南北 / 法

# Step 4: Calculate the dividend (實) for east-west width
實_東西 = 橫句入 * 矩間

# Step 5: Calculate the east-west width
東西廣 = 實_東西 / 法

# Convert to li (1 li = 180 chi)
a = 南北長 / 180
b = 東西廣 / 180

# Results
a, b
#----- content ends here -----


"""


### Explanation of the Code:
1. **Measurements**: All measurements are converted into fractions to maintain precision. For example, 3 chi 5 cun is represented as `3 + 5/10`.
2. **Divisor (法)**: Calculated using the formula provided in the procedure.
3. **Dividend (實)**: Separate calculations are performed for the north-south length and the east-west width.
4. **Conversion to li**: The final results are converted from chi to li, where 1 li = 180 chi.

### Answer:
- The north-south length is `a` li.
- The east-west width is `b` li.
"""


"""
Variable 'a' has wrong value. Expected: 4/3, Actual: -40/3
Variable 'b' has wrong value. Expected: 10/9, Actual: 100/9"""
