"""
今有登山臨邑，邑在山南。偃矩山上，令句高三尺五寸。令句端與邑東南隅及東北隅參相直。從句端遙望東北隅，入下股一丈二尺。又施橫句于入股之會，從立句端望西北隅，入橫句五尺。望東南隅，入下股一丈八尺。又設重矩于上，令矩間相去四丈。更從立句端望東南隅，入上股一丈七尺五寸。問邑廣長各幾何？
術曰：以句高乘東南隅入下股，如上股而一，所得減句高，餘為法；以東北隅下股減東南隅下股，餘以乘矩間為實。實如法而一，得邑南北長也。求邑廣：以入橫句乘矩間為實。實如法而一，即得邑東西廣。
答曰：南北長 a里 ；東西廣 b里 。
"""

"""
This is a complex ancient Chinese surveying problem involving geometry and proportional reasoning. Let's translate the problem and procedure into Python code step by step.

### Problem Description:
There is a mountain, and a city (邑) lies to the south of the mountain. A carpenter's square (矩) is used to measure the city's dimensions from the mountain. The following measurements are given:
1. The height of the vertical leg (句高) of the carpenter's square is 3 chi 5 cun (3.5 chi).
2. From the endpoint of the vertical leg, looking toward the northeast corner of the city, the lower leg (下股) is entered by 1 zhang 2 chi (12 chi).
3. A horizontal leg (橫句) is placed at the intersection of the lower leg, and from the endpoint of the vertical leg, looking toward the northwest corner of the city, the horizontal leg is entered by 5 chi.
4. Looking toward the southeast corner of the city, the lower leg is entered by 1 zhang 8 chi (18 chi).
5. A second carpenter's square is set up above the first, with the distance between the two squares being 4 zhang (40 chi).
6. From the endpoint of the vertical leg of the upper square, looking toward the southeast corner of the city, the upper leg (上股) is entered by 1 zhang 7 chi 5 cun (17.5 chi).

The task is to calculate the city's north-south length and east-west width.

### Procedure:
1. To calculate the north-south length:
   - Multiply the vertical leg height (句高) by the southeast corner's lower leg entry (東南隅入下股).
   - Divide the result by the upper leg entry (上股), then subtract the vertical leg height (句高). The remainder is the divisor (法).
   - Subtract the southeast corner's lower leg entry (東南隅下股) from the northeast corner's lower leg entry (東北隅下股). Multiply the result by the distance between the two carpenter's squares (矩間). This is the dividend (實).
   - Divide the dividend by the divisor to get the city's north-south length.

2. To calculate the east-west width:
   - Multiply the horizontal leg entry (入橫句) by the distance between the two carpenter's squares (矩間). This is the dividend (實).
   - Divide the dividend by the divisor to get the city's east-west width.

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Measurements
句高 = Fraction(35, 10)  # 3 chi 5 cun = 3.5 chi
東北隅入下股 = 12       # 1 zhang 2 chi = 12 chi
東南隅入下股 = 18       # 1 zhang 8 chi = 18 chi
入橫句 = 5             # 5 chi
矩間 = 40              # 4 zhang = 40 chi
上股 = Fraction(175, 10)  # 1 zhang 7 chi 5 cun = 17.5 chi

# Step 1: Calculate the north-south length
# 法 = (句高 * 東南隅入下股) / 上股 - 句高
法 = Fraction(句高 * 東南隅入下股, 上股) - 句高

# 實 = (東北隅入下股 - 東南隅入下股) * 矩間
實_南北 = (東北隅入下股 - 東南隅入下股) * 矩間

# 南北長 = 實 / 法
南北長 = Fraction(實_南北, 法)

# Step 2: Calculate the east-west width
# 實 = 入橫句 * 矩間
實_東西 = 入橫句 * 矩間

# 東西廣 = 實 / 法
東西廣 = Fraction(實_東西, 法)

# Convert results to li (1 li = 180 chi)
a = 南北長 / 180
b = 東西廣 / 180

# Output results
print(f"南北長 {a} 里；東西廣 {b} 里。")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Measurements**: All given measurements are converted into chi (Chinese feet) and represented as fractions where necessary.
2. **North-South Length Calculation**:
   - The divisor (`法`) is calculated using the formula provided in the procedure.
   - The dividend (`實_南北`) is calculated by multiplying the difference in lower leg entries by the distance between the two carpenter's squares.
   - The north-south length is obtained by dividing the dividend by the divisor.
3. **East-West Width Calculation**:
   - The dividend (`實_東西`) is calculated by multiplying the horizontal leg entry by the distance between the two carpenter's squares.
   - The east-west width is obtained by dividing the dividend by the divisor.
4. **Conversion to Li**: Since 1 li = 180 chi, the results are converted to li for the final answer.

### Final Output:
The program will output the city's north-south length and east-west width in li.
"""


"""
Variable 'a' has wrong value. Expected: 4/3, Actual: -40/3
Variable 'b' has wrong value. Expected: 10/9, Actual: 100/9"""
