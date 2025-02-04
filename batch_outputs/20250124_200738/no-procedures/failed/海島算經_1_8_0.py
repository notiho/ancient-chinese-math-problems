"""
今有登山臨邑，邑在山南。偃矩山上，令句高三尺五寸。令句端與邑東南隅及東北隅參相直。從句端遙望東北隅，入下股一丈二尺。又施橫句于入股之會，從立句端望西北隅，入橫句五尺。望東南隅，入下股一丈八尺。又設重矩于上，令矩間相去四丈。更從立句端望東南隅，入上股一丈七尺五寸。問邑廣長各幾何？
答曰：南北長 a里 ；東西廣 b里 。
"""

"""
This is a classic ancient Chinese surveying problem involving geometry and trigonometry. The problem describes a scenario where a person is using a surveying tool (a "矩", or carpenter's square) to measure the dimensions of a town (邑) from a mountain. The problem involves multiple measurements and requires calculating the north-south length and east-west width of the town.

To solve this problem, we need to carefully analyze the given measurements and use geometric relationships to calculate the dimensions of the town. Here's how we can translate this into Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
句高 = Fraction(3, 1) + Fraction(5, 10)  # 3尺5寸 = 3.5尺
入下股_東北隅 = Fraction(12, 1)  # 1丈2尺 = 12尺
入橫句 = Fraction(5, 1)  # 5尺
入下股_東南隅 = Fraction(18, 1)  # 1丈8尺 = 18尺
矩間距離 = Fraction(40, 1)  # 4丈 = 40尺
入上股_東南隅 = Fraction(17, 1) + Fraction(5, 10)  # 1丈7尺5寸 = 17.5尺

# Step 1: Calculate the north-south length (南北長)
南北長 = (入下股_東南隅 + 入上股_東南隅) / 2  # Average of lower and upper measurements

# Step 2: Calculate the east-west width (東西廣)
東西廣 = (入下股_東北隅 + 入橫句) / 2  # Average of lower and horizontal measurements

# Convert results to li (1里 = 300尺)
南北長_里 = 南北長 / 300
東西廣_里 = 東西廣 / 300

# Output the results
a = 南北長_里
b = 東西廣_里

print(f"南北長: {a} 里")
print(f"東西廣: {b} 里")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Input Data**: The given measurements are converted into fractions to ensure precision.
2. **North-South Length**: The north-south length of the town is calculated as the average of the lower and upper measurements of the south corner.
3. **East-West Width**: The east-west width is calculated as the average of the lower and horizontal measurements of the east corner.
4. **Conversion to Li**: Since 1 li = 300 chi, the results are converted from chi to li.

### Final Answer:
The north-south length (`a`) and the east-west width (`b`) are calculated in li. You can run the code to get the exact values.
"""


"""
Variable 'a' has wrong value. Expected: 4/3, Actual: 71/1200
Variable 'b' has wrong value. Expected: 10/9, Actual: 17/600"""
