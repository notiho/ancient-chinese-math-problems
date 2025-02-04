"""
今有城不知大小去人逺近於城西北隅而立四表相去各六丈令左兩表與城西北隅南北望參相直從右後表望城西北隅入右前表一尺二寸又望西南隅亦入右前表四寸又望東北隅亦入左後表二丈四尺問城去左後表及大小各㡬何
術曰置表相去自乗以望城西北隅入數而一得城去表又以望城西南隅入數而一所得減城去表餘為城之南北以望城東北隅入左後表數減城去表餘以乗表相去又以入左後表數而一即得城之東西
答曰城去左後表 a里 東西 b里 南北 c里
"""

"""
This problem is a complex geometric problem involving the use of ancient Chinese surveying techniques to determine the size and distance of a city based on observations from specific points. Translating this into Python code requires careful adherence to the procedure described in the text.

Let's break down the problem and encode it step by step:

### Problem Breakdown:
1. **Given Data:**
   - Four markers are placed, each 6 zhang apart.
   - Observations are made from the right rear marker to the northwest corner of the city wall, the southwest corner, and the northeast corner.
   - The observations indicate how much the city wall "enters" (is offset from) the markers:
     - Northwest corner: 1 zhang 2 chi (1.2 zhang).
     - Southwest corner: 0.4 zhang.
     - Northeast corner: 2 zhang 4 chi (2.4 zhang).

2. **Questions:**
   - Distance from the left rear marker to the city.
   - The east-west length of the city.
   - The north-south length of the city.

3. **Procedure:**
   - Use the distances between markers and the offsets to calculate the required dimensions using geometric relationships.

### Python Code:

"""


from fractions import Fraction

# Given data
表相去 = 6  # Distance between markers in zhang
望城西北隅入數 = Fraction(1, 1) + Fraction(2, 10)  # 1 zhang 2 chi = 1.2 zhang
望城西南隅入數 = Fraction(4, 10)  # 0.4 zhang
望城東北隅入數 = Fraction(2, 1) + Fraction(4, 10)  # 2 zhang 4 chi = 2.4 zhang

# 城去左後表 (Distance from the left rear marker to the city)
城去表 = 表相去**2 / 望城西北隅入數

# 城之南北 (North-south length of the city)
城南北 = (望城西北隅入數 - 望城西南隅入數) * 城去表 / 表相去

# 城之東西 (East-west length of the city)
城東西 = (望城東北隅入數 - 城去表) * 表相去 / 望城東北隅入數

# Final answers
a = 城去表 / 100  # Convert zhang to li (1 li = 100 zhang)
b = 城東西 / 100  # Convert zhang to li
c = 城南北 / 100  # Convert zhang to li

# Output results
a, b, c


"""


### Explanation of the Code:
1. **城去左後表 (Distance to the city):**
   - Use the square of the distance between markers divided by the offset for the northwest corner.

2. **城之南北 (North-south length):**
   - Subtract the offset for the southwest corner from the northwest corner, multiply by the distance to the city, and divide by the distance between markers.

3. **城之東西 (East-west length):**
   - Subtract the distance to the city from the offset for the northeast corner, multiply by the distance between markers, and divide by the offset for the northeast corner.

4. **Conversion to li:**
   - Since the problem asks for the answers in li, convert zhang to li by dividing by 100.

### Final Answer:
- `a`: Distance from the left rear marker to the city in li.
- `b`: East-west length of the city in li.
- `c`: North-south length of the city in li.
"""


"""
Variable 'a' has wrong value. Expected: 5/3, Actual: 3/10
Variable 'b' has wrong value. Expected: 62/15, Actual: -69/100
Variable 'c' has wrong value. Expected: 10/3, Actual: 1/25"""
