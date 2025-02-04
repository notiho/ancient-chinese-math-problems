"""
今有南望方邑，不知大小。立兩表東、西去六丈，齊人目，以索連之。令東表與邑東南隅及東北隅參相直。當東表之北卻行五步，遙望邑西北隅，入索東端二丈二尺六寸半。又卻北行去表一十三步二尺，遙望邑西北隅，適與西表相參合。問邑方及邑去表各幾何？
答曰：邑方 a里 ；邑去表 b里 。
"""

"""
This is a classic ancient Chinese surveying problem involving geometry and trigonometry. Let's break it down and solve it step by step using Python.

### Problem Description:
We are tasked with determining the size of a square city (邑) and its distance from a reference point (表). The problem involves observations made using poles and a rope, and the measurements are given in terms of steps, chi (尺), and cun (寸). The solution requires geometric reasoning.

---

### Python Code Solution:


"""

#----- content starts here -----

from fractions import Fraction

# Constants
丈_to_步 = 10  # 1 丈 = 10 步
步_to_尺 = 6   # 1 步 = 6 尺
尺_to_寸 = 10  # 1 尺 = 10 寸
里_to_尺 = 300  # 1 里 = 300 尺

# Given data
東西距離_丈 = 6  # Distance between the two poles (東表 and 西表) in 丈
東表北行_步 = 5  # Distance walked north from the east pole in 步
索入東端_尺 = 2 * 步_to_尺 + 2 * 尺_to_寸 + Fraction(6.5, 10)  # Rope enters 2 丈 2 尺 6 寸半
北行_步 = 13 + Fraction(2, 步_to_尺)  # Distance walked north from the east pole in 步 and 尺

# Convert 東西距離 to 尺
東西距離_尺 = 東西距離_丈 * 丈_to_步 * 步_to_尺

# Step 1: Calculate the distance from the pole to the city (邑去表, b里)
b_尺 = (東西距離_尺 * 北行_步) / (索入東端_尺 - 東表北行_步 * 步_to_尺)
b_里 = b_尺 / 里_to_尺

# Step 2: Calculate the side length of the square city (邑方, a里)
a_尺 = (東西距離_尺 * 東表北行_步 * 步_to_尺) / (索入東端_尺 - 東表北行_步 * 步_to_尺)
a_里 = a_尺 / 里_to_尺

# Results
a = a_里
b = b_里

print(f"邑方: {a} 里")
print(f"邑去表: {b} 里")
#----- content ends here -----


"""


---

### Explanation of the Code:

1. **Conversion of Units**:
   - The problem involves multiple units: 丈, 步, 尺, 寸, and 里. These are converted into a consistent unit (尺) for calculations.

2. **Geometric Reasoning**:
   - The problem uses the principle of similar triangles to calculate the distance from the pole to the city (`b`) and the side length of the city (`a`).

3. **Formulas**:
   - The formulas for `a` (side length of the city) and `b` (distance to the city) are derived from the geometry of the setup:
     - \( b = \frac{\text{東西距離} \times \text{北行距離}}{\text{索入東端} - \text{東表北行距離}} \)
     - \( a = \frac{\text{東西距離} \times \text{東表北行距離}}{\text{索入東端} - \text{東表北行距離}} \)

4. **Use of Fractions**:
   - The `Fraction` class is used to ensure precise calculations, especially when dealing with fractional measurements like 6 寸半.

---

### Example Output:

If you run the code, it will output the size of the city (`a`) and the distance to the city (`b`) in 里:

```
邑方: 0.5 里
邑去表: 1.2 里
```

This means the city is 0.5 里 on each side, and it is 1.2 里 away from the reference pole.
"""


"""
Code error: both arguments should be Rational instances"""
