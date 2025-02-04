"""
今有竹九節，下三節容四升，上四節容三升。問︰中間二節欲均容各多少？
術曰：以下三節分四升為下率，以上四節分三升為上率。上下率以少減多，餘為實。置四節、三節，各半之，以減九節，餘為法。實如法得一升，即衰相去也。下率，一升、少半升者，下第二節容也。
荅曰：下初， a升 ，次 b升 ，次 c升 ，次 d升 ，次 e升 ，次 f升 ，次 g升 ，次 h升 ，次 i升 。
"""

"""
This problem involves distributing liquid volumes across nine sections of a bamboo, with specific constraints for the lower three sections, upper four sections, and the middle two sections. Let's break it down step by step and encode the solution in Python.

---

### Problem Breakdown:
1. **Given:**
   - The lower 3 sections (下三節) hold 4 sheng (升) in total.
   - The upper 4 sections (上四節) hold 3 sheng (升) in total.
   - The middle 2 sections (中間二節) need to be evenly distributed.

2. **Procedure:**
   - Calculate the "rate" (rate of volume per section) for the lower and upper sections:
     - Lower rate = \( \frac{4}{3} \) sheng per section.
     - Upper rate = \( \frac{3}{4} \) sheng per section.
   - Find the difference between the two rates (少減多, subtract the smaller from the larger).
   - Use the difference to calculate the adjustment for the middle two sections.
   - Distribute the volumes across all nine sections accordingly.

3. **Answer:**
   - Output the volume for each of the nine sections.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
lower_sections = 3  # 下三節
upper_sections = 4  # 上四節
middle_sections = 2  # 中間二節
total_sections = 9  # 總共九節

lower_total_volume = 4  # 下三節容四升
upper_total_volume = 3  # 上四節容三升

# Step 1: Calculate rates for lower and upper sections
lower_rate = Fraction(lower_total_volume, lower_sections)  # 下率
upper_rate = Fraction(upper_total_volume, upper_sections)  # 上率

# Step 2: Calculate the difference between the rates
rate_difference = lower_rate - upper_rate  # 少減多，餘為實

# Step 3: Calculate the adjustment for the middle sections
# 置四節、三節，各半之，以減九節，餘為法
law = total_sections - (Fraction(lower_sections, 2) + Fraction(upper_sections, 2))

# 實如法得一升，即衰相去也
adjustment = rate_difference / law

# Step 4: Calculate the volumes for each section
# 下初，a升，次b升，次c升
volumes = []

# Lower 3 sections
for i in range(lower_sections):
    volumes.append(lower_rate - (i * adjustment))

# Middle 2 sections (均容)
middle_volume = lower_rate - (lower_sections * adjustment)
for i in range(middle_sections):
    volumes.append(middle_volume)

# Upper 4 sections
for i in range(upper_sections):
    volumes.append(upper_rate + (i * adjustment))

# Output results
a, b, c, d, e, f, g, h, i = volumes
print(f"下初，{a}升，次{b}升，次{c}升，次{d}升，次{e}升，次{f}升，次{g}升，次{h}升，次{i}升。")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Rates Calculation:**
   - The lower rate is \( \frac{4}{3} \) sheng per section.
   - The upper rate is \( \frac{3}{4} \) sheng per section.

2. **Adjustment Calculation:**
   - The difference between the rates is used to adjust the middle sections.
   - The "law" is calculated based on the total sections minus the contributions of the lower and upper sections.

3. **Volume Distribution:**
   - The lower sections decrease by the adjustment factor.
   - The middle sections are evenly distributed.
   - The upper sections increase by the adjustment factor.

4. **Output:**
   - The volumes for all nine sections are printed in order.

---

### Example Output:
If you run the code, it will calculate and display the volumes for each of the nine sections in terms of fractions (sheng).
"""


"""
Variable 'a' has wrong value. Expected: 95/66, Actual: 4/3
Variable 'b' has wrong value. Expected: 4/3, Actual: 27/22
Variable 'c' has wrong value. Expected: 27/22, Actual: 37/33
Variable 'd' has wrong value. Expected: 37/33, Actual: 67/66
Variable 'f' has wrong value. Expected: 10/11, Actual: 3/4
Variable 'g' has wrong value. Expected: 53/66, Actual: 113/132
Variable 'h' has wrong value. Expected: 23/33, Actual: 127/132
Variable 'i' has wrong value. Expected: 13/22, Actual: 47/44"""
