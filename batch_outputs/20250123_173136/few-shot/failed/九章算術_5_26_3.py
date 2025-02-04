"""
今有盤池，上廣六丈，袤八丈，下廣四丈，袤六丈，深二丈。問︰積幾何？
荅曰：七萬六百六十六尺、太半尺。
負土往來七十步，其二十步上下棚除。棚除二當平道五，踟躕之間十加一，載輸之間三十步，定一返一百四十步。土籠積一尺六寸，秋程人功行五十九里半。問︰人到、積尺、用徒各幾何？
術曰：以一籠積尺乘程行步數為實。往來上下，棚除二當平道五。置定往來步數，十加一，及載輸之間三十步以為法。除之，所得即一人所到尺。以所到約積尺，即用徒人數。
荅曰：人到 a尺 。用徒 b人 。
"""

This problem involves calculating the volume of an irregularly shaped pond and determining the labor required to transport the excavated soil. Let's break it into two parts: first, calculating the volume of the pond, and second, determining the labor requirements.

---

### Part 1: Calculating the Volume of the Pond

"""
The pond has the following dimensions:
- Upper width: 6 zhang
- Upper length: 8 zhang
- Lower width: 4 zhang
- Lower length: 6 zhang
- Depth: 2 zhang

The volume is calculated as the average of the upper and lower areas, multiplied by the depth.
"""

# Dimensions of the pond
上廣 = 6  # Upper width in zhang
上袤 = 8  # Upper length in zhang
下廣 = 4  # Lower width in zhang
下袤 = 6  # Lower length in zhang
深 = 2    # Depth in zhang

# Convert zhang to chi (1 zhang = 10 chi)
上廣 *= 10
上袤 *= 10
下廣 *= 10
下袤 *= 10
深 *= 10

# Calculate the areas of the upper and lower surfaces
上積 = 上廣 * 上袤
下積 = 下廣 * 下袤

# Calculate the volume of the pond
積 = Fraction((上積 + 下積) * 深, 2)

# Convert the volume to chi and split into integer and fractional parts
積整數 = 積.numerator // 積.denominator
積餘數 = Fraction(積.numerator % 積.denominator, 積.denominator)

# Answer for the pond volume
pond_volume = f"{積整數}尺、{積餘數}尺"

---

### Part 2: Labor Requirements for Soil Transport

"""
The procedure for calculating labor requirements is as follows:
1. Multiply the volume of one soil basket (1 chi 6 cun) by the total distance traveled (59.5 li converted to steps).
2. Adjust for the difficulty of the terrain:
   - Two steps on the slope are equivalent to five steps on flat ground.
   - Add 10% for hesitation and 30 steps for loading/unloading.
3. Divide the total adjusted steps by the adjusted steps per round trip to find the number of chi transported by one person.
4. Divide the total volume by the chi transported by one person to find the number of workers required.
"""

# Constants
土籠積尺 = Fraction(16, 10)  # Volume of one soil basket in chi (1 chi 6 cun)
秋程行里 = Fraction(59.5)   # Distance traveled in li
一里步數 = 300             # Steps per li
往來步數 = 140             # Steps per round trip
棚除比例 = Fraction(2, 5)   # Slope adjustment (2 steps = 5 flat steps)
踟躕比例 = Fraction(11, 10) # Hesitation adjustment (10 + 1 = 11/10)
載輸步數 = 30              # Loading/unloading adjustment in steps

# Step 1: Calculate total steps traveled
程行步數 = 秋程行里 * 一里步數

# Step 2: Adjust for terrain
棚除步數 = 棚除比例 * 往來步數
法 = 棚除步數 + 踟躕比例 * 往來步數 + 載輸步數

# Step 3: Calculate chi transported by one person
人到尺 = Fraction(土籠積尺 * 程行步數, 法)

# Step 4: Calculate the number of workers required
用徒人數 = Fraction(積, 人到尺)

# Convert the number of workers to an integer (round up if necessary)
用徒人數整數 = 用徒人數.numerator // 用徒人數.denominator
if 用徒人數.numerator % 用徒人數.denominator != 0:
    用徒人數整數 += 1

# Answer for labor requirements
a = 人到尺
b = 用徒人數整數

---

### Final Answers

1. Pond volume: `七萬六百六十六尺、太半尺` (70666 chi and a little over half a chi)
2. Labor requirements:
   - Chi transported by one person: `a尺`
   - Number of workers required: `b人`
"""
Code error: unterminated string literal (detected at line 2) (<string>, line 2)"""
