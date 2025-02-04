"""
今有城不知大小去人逺近於城西北隅而立四表相去各六丈令左兩表與城西北隅南北望參相直從右後表望城西北隅入右前表一尺二寸又望西南隅亦入右前表四寸又望東北隅亦入左後表二丈四尺問城去左後表及大小各㡬何
術曰置表相去自乗以望城西北隅入數而一得城去表又以望城西南隅入數而一所得減城去表餘為城之南北以望城東北隅入左後表數減城去表餘以乗表相去又以入左後表數而一即得城之東西
答曰城去左後表 a里 東西 b里 南北 c里
"""

"""
This problem involves a complex geometric calculation based on ancient Chinese surveying techniques. The problem describes a situation where a city is observed from specific points, and the goal is to determine the distance to the city and its dimensions (east-west and north-south). Here's how we can translate the procedure into Python code:


"""


"""
Suppose there is a city of unknown size. A person stands at the northwest corner of the city, observing from four markers, each 6 zhang apart.
From the right rear marker, the northwest corner of the city is observed to enter the right front marker by 1 chi 2 cun.
The southwest corner of the city is observed to enter the right front marker by 4 cun.
The northeast corner of the city is observed to enter the left rear marker by 2 zhang 4 chi.
Question: What is the distance from the city to the left rear marker, and what are the dimensions of the city (east-west and north-south)?

The procedure says:
1. Place the distance between the markers and square it.
2. Divide by the amount the northwest corner enters to find the distance from the city to the marker.
3. Divide by the amount the southwest corner enters to find the city's north-south dimension.
4. Subtract the distance to the marker from the result to get the city's north-south dimension.
5. Subtract the amount the northeast corner enters the left rear marker from the distance to the marker.
6. Multiply the result by the distance between the markers.
7. Divide by the amount the northeast corner enters the left rear marker to find the city's east-west dimension.

Answer: The city is *a* li from the left rear marker, *b* li east-west, and *c* li north-south.
"""

from fractions import Fraction

# Constants
表距 = 6  # Distance between markers in zhang
入西北隅 = Fraction(1, 10) + Fraction(2, 100)  # Northwest corner enters right front marker (1 chi 2 cun)
入西南隅 = Fraction(4, 100)  # Southwest corner enters right front marker (4 cun)
入東北隅 = 2 + Fraction(4, 10)  # Northeast corner enters left rear marker (2 zhang 4 chi)

# Step 1: Place the distance between the markers and square it
表距平方 = 表距 ** 2

# Step 2: Divide by the amount the northwest corner enters to find the distance from the city to the marker
城去表 = Fraction(表距平方, 入西北隅)

# Step 3: Divide by the amount the southwest corner enters to find the city's north-south dimension
南北距 = Fraction(表距平方, 入西南隅)

# Step 4: Subtract the distance to the marker from the result to get the city's north-south dimension
南北距 -= 城去表

# Step 5: Subtract the amount the northeast corner enters the left rear marker from the distance to the marker
東西距 = 城去表 - 入東北隅

# Step 6: Multiply the result by the distance between the markers
東西距 *= 表距

# Step 7: Divide by the amount the northeast corner enters the left rear marker to find the city's east-west dimension
東西距 = Fraction(東西距, 入東北隅)

# Convert results to li (1 zhang = 1/300 li)
城去表_里 = 城去表 / 300
東西距_里 = 東西距 / 300
南北距_里 = 南北距 / 300

# Final results
a = 城去表_里
b = 東西距_里
c = 南北距_里


"""


### Explanation of the Code:
1. **表距平方**: The square of the distance between the markers is calculated.
2. **城去表**: The distance from the city to the marker is calculated by dividing the squared distance by the amount the northwest corner enters.
3. **南北距**: The north-south dimension is calculated by dividing the squared distance by the amount the southwest corner enters, then subtracting the distance to the marker.
4. **東西距**: The east-west dimension is calculated by subtracting the amount the northeast corner enters from the distance to the marker, multiplying by the distance between the markers, and dividing by the amount the northeast corner enters.
5. **Conversion to li**: Since the original measurements are in zhang, they are converted to li (1 zhang = 1/300 li).

### Final Answer:
- The city is `a` li from the left rear marker.
- The city is `b` li east-west.
- The city is `c` li north-south.
"""


"""
Variable 'a' has wrong value. Expected: 5/3, Actual: 1
Variable 'b' has wrong value. Expected: 62/15, Actual: 62/25
Variable 'c' has wrong value. Expected: 10/3, Actual: 2"""
