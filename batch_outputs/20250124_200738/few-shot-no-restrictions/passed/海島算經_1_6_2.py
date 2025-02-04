"""
今有望清淵，淵下有白石。偃矩岸上，令句高三尺。斜望水岸，入下股四尺五寸。望白石，入下股二尺四寸。又設重矩于上，其間相去四尺。更從句端斜望水岸，入上股四尺。以望白石，入上股二尺二寸。問水深幾何？
術曰：置望水上下股相減，餘以乘望石上股為上率。又以望石上下股相減，餘以乘望水上股為下率。兩率相減，餘以乘矩間為實；以二差相乘為法。實如法而一，得水深。
答曰： a丈 。
"""

"""
This is a classic problem involving geometry and proportional reasoning to calculate the depth of water based on observations using a measuring tool (矩). Let's translate the problem and solution into Python code.

---

### Problem Description:
Suppose you are observing a clear deep pool (淵) with a white stone at the bottom. Using a measuring tool (矩), the following observations are made:
1. The tool is placed on the bank, with the vertical leg (句) set to 3 chi.
2. Looking diagonally at the water's edge, the lower horizontal leg (股) extends 4 chi 5 cun.
3. Looking at the white stone, the lower horizontal leg (股) extends 2 chi 4 cun.
4. Another measuring tool is placed above the first one, with a vertical separation of 4 chi.
5. From the top tool, looking diagonally at the water's edge, the upper horizontal leg (股) extends 4 chi.
6. Looking at the white stone from the top tool, the upper horizontal leg (股) extends 2 chi 2 cun.

**Question**: What is the depth of the water?

---

### Procedure:
1. Subtract the upper and lower horizontal legs (股) when observing the water's edge. Multiply the result by the upper horizontal leg when observing the white stone to get the numerator for the upper ratio (上率).
2. Subtract the upper and lower horizontal legs (股) when observing the white stone. Multiply the result by the upper horizontal leg when observing the water's edge to get the numerator for the lower ratio (下率).
3. Subtract the two ratios. Multiply the result by the vertical separation of the two tools (矩間) to get the numerator for the depth.
4. Multiply the differences of the two observations (水岸 and 白石) to get the denominator.
5. Divide the numerator by the denominator to get the depth of the water.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Measurements in chi and cun
句高 = 3  # Vertical leg (句) in chi
矩間 = 4  # Vertical separation between the two tools in chi

# Lower tool observations
水岸下股 = 4 + Fraction(5, 10)  # 4 chi 5 cun
白石下股 = 2 + Fraction(4, 10)  # 2 chi 4 cun

# Upper tool observations
水岸上股 = 4  # 4 chi
白石上股 = 2 + Fraction(2, 10)  # 2 chi 2 cun

# Step 1: Calculate the upper ratio (上率)
水岸股差 = 水岸下股 - 水岸上股  # Difference in 水岸股
上率 = 水岸股差 * 白石上股  # Multiply by 白石上股

# Step 2: Calculate the lower ratio (下率)
白石股差 = 白石下股 - 白石上股  # Difference in 白石股
下率 = 白石股差 * 水岸上股  # Multiply by 水岸上股

# Step 3: Calculate the numerator for the depth
率差 = 上率 - 下率  # Difference between the two ratios
實 = 率差 * 矩間  # Multiply by the vertical separation

# Step 4: Calculate the denominator
法 = 水岸股差 * 白石股差  # Multiply the differences

# Step 5: Calculate the depth of the water
水深 = Fraction(實, 法)

# Convert to zhang (1 zhang = 10 chi)
水深丈 = 水深 / 10

# Output the result
a = 水深丈
print(f"水深為 {a} 丈")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Input Measurements**: All measurements are converted into fractions of chi and cun for precision.
2. **Upper and Lower Ratios**: The differences in horizontal legs (股) are used to calculate the ratios for water's edge and the white stone.
3. **Numerator and Denominator**: The numerator is calculated by multiplying the difference in ratios by the vertical separation. The denominator is the product of the differences in observations.
4. **Final Depth**: The depth is calculated as the fraction of the numerator and denominator, then converted to zhang (丈).

---

### Example Output:
If you run the code, it will calculate the depth of the water in zhang (丈). For this specific problem, the result will be:

```
水深為 a 丈
```

Where `a` is the calculated depth of the water.
"""


"""
"""
