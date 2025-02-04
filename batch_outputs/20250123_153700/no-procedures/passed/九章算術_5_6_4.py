"""
今有溝上廣一丈五尺，下廣一丈，深五尺，袤七丈。問︰積幾何？
荅曰：四千三百七十五尺。
春程人功七百六十六尺，并出土功五分之一，定功六百一十二尺、五分尺之四。問︰用徒幾何？
荅曰： a人 。
"""

"""
### Problem Breakdown:

1. **First Part: Calculating the Volume of the Trapezoidal Ditch**
   - The ditch has:
     - Top width: 1 丈 5 尺 = 15 尺
     - Bottom width: 1 丈 = 10 尺
     - Depth: 5 尺
     - Length: 7 丈 = 70 尺
   - The formula for the volume of a trapezoidal prism is:
     \[
     V = \frac{(上廣 + 下廣) \times 深 \times 袤}{2}
     \]

2. **Second Part: Determining the Number of Workers**
   - The total volume of the ditch is 4375 尺.
   - Each worker can excavate 612 尺 \( \frac{4}{5} \) (including the adjustment for the extra work of moving soil, which is 1/5 of the digging effort).
   - To find the number of workers, divide the total volume by the adjusted work per worker.

---

### Python Code:


"""


from fractions import Fraction

# Dimensions of the ditch
上廣 = 15  # Top width in 尺
下廣 = 10  # Bottom width in 尺
深 = 5     # Depth in 尺
袤 = 70    # Length in 尺

# Calculate the volume of the ditch
積 = Fraction((上廣 + 下廣) * 深 * 袤, 2)

# Total volume of the ditch
print(f"Volume of the ditch: {積} 尺")  # Should be 4375 尺

# Worker efficiency
定功 = Fraction(612) + Fraction(4, 5)  # Work per worker in 尺

# Calculate the number of workers needed
a = 積 / 定功

# Output the number of workers
print(f"Number of workers needed: {a} 人")


"""


---

### Explanation of Results:
1. **Volume of the Ditch**:
   - Using the formula:
     \[
     V = \frac{(15 + 10) \times 5 \times 70}{2} = 4375 \, 尺
     \]

2. **Worker Efficiency**:
   - Each worker can excavate \( 612 \, 尺 \, \frac{4}{5} \), which is:
     \[
     612 + \frac{4}{5} = 612.8 \, 尺
     \]

3. **Number of Workers**:
   - Divide the total volume by the work per worker:
     \[
     a = \frac{4375}{612.8} \approx 7.14 \, 人
     \]
   - Since the number of workers must be an integer, round up to 8 workers.


"""


"""
"""
