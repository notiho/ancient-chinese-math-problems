"""
今有登山臨邑，邑在山南。偃矩山上，令句高三尺五寸。令句端與邑東南隅及東北隅參相直。從句端遙望東北隅，入下股一丈二尺。又施橫句于入股之會，從立句端望西北隅，入橫句五尺。望東南隅，入下股一丈八尺。又設重矩于上，令矩間相去四丈。更從立句端望東南隅，入上股一丈七尺五寸。問邑廣長各幾何？
術曰：以句高乘東南隅入下股，如上股而一，所得減句高，餘為法；以東北隅下股減東南隅下股，餘以乘矩間為實。實如法而一，得邑南北長也。求邑廣：以入橫句乘矩間為實。實如法而一，即得邑東西廣。
答曰：南北長 a里 ；東西廣 b里 。
"""

"""
This is a classic ancient Chinese surveying problem involving geometry and trigonometry to determine the dimensions of a city (邑) observed from a mountain. Let's break it down step by step and implement it in Python.

### Problem Breakdown:
1. **Given Data:**
   - Height of the mountain (句高): 3 尺 5 寸 = \(3 + \frac{5}{10} = 3.5\) 尺.
   - Distance from the observation point to the eastern edges of the city:
     - 东北隅 (Northeast corner): 入下股 1 丈 2 尺 = \(10 + 2 = 12\) 尺.
     - 东南隅 (Southeast corner): 入下股 1 丈 8 尺 = \(10 + 8 = 18\) 尺.
   - Horizontal offset (入横句): 5 尺.
   - Distance between the two levels of the surveying tools (矩间): 4 丈 = \(4 \times 10 = 40\) 尺.
   - Upper-level observation:
     - 东南隅 (Southeast corner): 入上股 1 丈 7 尺 5 寸 = \(10 + 7 + \frac{5}{10} = 17.5\) 尺.

2. **Goal:**
   - Calculate the **north-south length** (南北长) of the city.
   - Calculate the **east-west width** (东西广) of the city.

3. **Procedure:**
   - **南北长 (North-South Length):**
     - Use the formula:
       \[
       \text{法} = \text{句高} \times \text{东南隅入下股} / \text{入上股} - \text{句高}
       \]
       \[
       \text{实} = (\text{东北隅入下股} - \text{东南隅入下股}) \times \text{矩间}
       \]
       \[
       \text{南北长} = \text{实} / \text{法}
       \]
   - **东西广 (East-West Width):**
     - Use the formula:
       \[
       \text{实} = \text{入横句} \times \text{矩间}
       \]
       \[
       \text{东西广} = \text{实} / \text{法}
       \]

---

### Python Implementation:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
句高 = Fraction(3, 1) + Fraction(5, 10)  # 3 尺 5 寸 = 3.5 尺
东南隅入下股 = Fraction(10, 1) + Fraction(8, 1)  # 1 丈 8 尺 = 18 尺
东北隅入下股 = Fraction(10, 1) + Fraction(2, 1)  # 1 丈 2 尺 = 12 尺
入横句 = Fraction(5, 1)  # 5 尺
矩间 = Fraction(4, 1) * 10  # 4 丈 = 40 尺
入上股 = Fraction(10, 1) + Fraction(7, 1) + Fraction(5, 10)  # 1 丈 7 尺 5 寸 = 17.5 尺

# 南北长 calculation
法_南北 = (句高 * 东南隅入下股 / 入上股) - 句高
实_南北 = (东北隅入下股 - 东南隅入下股) * 矩间
南北长 = 实_南北 / 法_南北

# 东西广 calculation
实_东西 = 入横句 * 矩间
东西广 = 实_东西 / 法_南北

# Convert results to li (1 丈 = 10 尺, 1 里 = 300 尺)
南北长_里 = 南北长 / 300
东西广_里 = 东西广 / 300

# Output results
a = 南北长_里
b = 东西广_里

print(f"南北长: {a} 里")
print(f"东西广: {b} 里")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Units Conversion:**
   - All measurements are converted to 尺 (chi) for consistency.
   - Final results are converted to 里 (li), where \(1 里 = 300 尺\).

2. **Fractions:**
   - The `Fraction` class is used to ensure precise calculations, as ancient Chinese mathematics often dealt with fractional values.

3. **Formulas:**
   - The formulas provided in the problem are directly implemented step by step.

---

### Output:
The program will compute the north-south length (\(a\)) and east-west width (\(b\)) of the city in 里.
"""


"""
Variable 'a' has wrong value. Expected: 4/3, Actual: -8
Variable 'b' has wrong value. Expected: 10/9, Actual: 20/3"""
