"""
今有望松生山上，不知高下。立兩表齊，高二丈，前後相去五十步，令後表與前表參相直。從前表卻行七步四尺，薄地遙望松末，與表端參合。又望松本，入表二尺八寸。复從後表卻行八步五尺，薄地遙望松末，亦與表端參合。問松高及山去表各幾何？
答曰：松高 a丈 ；山去表 b里 。
"""

"""
This is a classic ancient Chinese surveying problem involving similar triangles. The goal is to calculate the height of a pine tree on a mountain and the horizontal distance from the base of the mountain to the reference point (the front post). Here's how we can solve it step by step:

---

### Problem Breakdown:
1. **Setup**:
   - Two posts are erected, each 2 zhang tall.
   - The distance between the two posts is 50 bu.
   - Observations are made from two positions:
     - From the front post, stepping back 7 bu and 4 chi, the top of the pine tree aligns with the top of the front post, and the base of the pine tree aligns 2 chi 8 cun below the top of the front post.
     - From the rear post, stepping back 8 bu and 5 chi, the top of the pine tree aligns with the top of the rear post.

2. **Goal**:
   - Calculate the height of the pine tree (`a`, in zhang).
   - Calculate the horizontal distance from the base of the mountain to the front post (`b`, in li).

---

### Solution in Python Code:


"""


from fractions import Fraction

# Constants
前表高 = Fraction(2)  # Height of the front post in zhang
後表高 = Fraction(2)  # Height of the rear post in zhang
前後距離 = Fraction(50)  # Distance between the two posts in bu

# Observations
前表退步 = Fraction(7) + Fraction(4, 10)  # 7 bu 4 chi = 7.4 bu
松本入表 = Fraction(2, 10) + Fraction(8, 100)  # 2 chi 8 cun = 0.28 bu
後表退步 = Fraction(8) + Fraction(5, 10)  # 8 bu 5 chi = 8.5 bu

# Step 1: Calculate the height of the pine tree (a)
# Using similar triangles:
# 松高 / (前表退步 + 松本入表) = 前表高 / 前表退步
松高 = 前表高 * (前表退步 + 松本入表) / 前表退步

# Step 2: Calculate the horizontal distance from the base of the mountain to the front post (b)
# Using similar triangles:
# 松高 / (前後距離 + 後表退步) = 後表高 / 後表退步
山去表 = 後表高 * (前後距離 + 後表退步) / 後表退步

# Convert 山去表 from bu to li (1 li = 300 bu)
山去表_in_li = 山去表 / 300

# Results
a = 松高  # Height of the pine tree in zhang
b = 山去表_in_li  # Horizontal distance in li

# Output
a, b


"""


---

### Explanation of the Code:
1. **Similar Triangles**:
   - The height of the pine tree is proportional to the height of the posts and the distances observed.
   - Using the front post observation, we calculate the height of the pine tree.
   - Using the rear post observation, we calculate the horizontal distance from the base of the mountain to the front post.

2. **Units**:
   - All calculations are done in consistent units (bu, zhang, li).
   - The final distance is converted from bu to li (1 li = 300 bu).

---

### Final Answer:
- 松高 `a` 丈 (height of the pine tree in zhang)
- 山去表 `b` 里 (horizontal distance from the base of the mountain to the front post in li)
"""


"""
Variable 'a' has wrong value. Expected: 307/25, Actual: 384/185
Variable 'b' has wrong value. Expected: 23/21, Actual: 39/850"""
