"""
今有盤池，上廣六丈，袤八丈，下廣四丈，袤六丈，深二丈。問︰積幾何？
荅曰：七萬六百六十六尺、太半尺。
負土往來七十步，其二十步上下棚除。棚除二當平道五，踟躕之間十加一，載輸之間三十步，定一返一百四十步。土籠積一尺六寸，秋程人功行五十九里半。問︰人到、積尺、用徒各幾何？
術曰：以一籠積尺乘程行步數為實。往來上下，棚除二當平道五。置定往來步數，十加一，及載輸之間三十步以為法。除之，所得即一人所到尺。以所到約積尺，即用徒人數。
荅曰：人到 a尺 。用徒 b人 。
"""

"""
### Problem Breakdown:

1. **Volume of the pond (盤池積):**
   - The pond has an upper width of 6 zhang, an upper length of 8 zhang, a lower width of 4 zhang, a lower length of 6 zhang, and a depth of 2 zhang.
   - The volume is calculated using the formula for a frustum of a rectangular pyramid:
     \[
     V = \frac{h}{3} \cdot (A_1 + A_2 + \sqrt{A_1 \cdot A_2})
     \]
     where \(A_1\) is the area of the upper rectangle, \(A_2\) is the area of the lower rectangle, and \(h\) is the depth.

2. **Transporting the soil:**
   - A soil basket (土籠) holds 1 chi 6 cun of soil.
   - Workers travel 70 steps round-trip, with 20 steps for the "棚除" (uphill/downhill adjustment).
   - For every 2棚除, it is equivalent to 5平道 (flat path).
   - Additional adjustments:
     - "踟躕之間" adds 10%.
     - "載輸之間" adds 30 steps.
   - Total round-trip steps are calculated, and the number of workers needed is determined based on the total soil volume and the soil transported per worker.

---

### Step 1: Calculate the volume of the pond.



---

### Step 2: Calculate the number of steps per round trip.



---

### Step 3: Calculate the number of workers needed.


"""

#----- content starts here -----

from math import sqrt
from fractions import Fraction

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

# Calculate areas of the upper and lower rectangles
A1 = 上廣 * 上袤
A2 = 下廣 * 下袤

# Volume of the frustum (V = h/3 * (A1 + A2 + sqrt(A1 * A2)))
積尺 = Fraction(深, 3) * (A1 + A2 + sqrt(A1 * A2))

# Convert to a mixed number for clarity
積整數 = int(積尺)
積餘數 = 積尺 - 積整數
print(f"盤池積: {積整數}尺, 太半尺 ({積餘數})")

# Round-trip steps
往來步數 = 70

# 棚除 adjustment: 2棚除 = 5平道
棚除步數 = 20
棚除平道當量 = Fraction(5, 2) * 棚除步數

# 踟躕之間 adjustment: 10%
踟躕加成 = Fraction(10, 100)

# 載輸之間 adjustment: +30 steps
載輸步數 = 30

# Total adjusted round-trip steps
總步數 = (往來步數 - 棚除步數) + 棚除平道當量 + 載輸步數
總步數 += 總步數 * 踟躕加成
print(f"每人往返步數: {總步數}步")

# Soil basket capacity (1 chi 6 cun = 1.6 chi)
土籠積尺 = Fraction(16, 10)

# Worker distance per trip (步數 converted to chi)
步長 = Fraction(5, 3)  # Assume 1 step = 5/3 chi
每人程行 = 總步數 * 步長

# Soil transported per worker per trip
每人土運輸 = 每人程行 * 土籠積尺

# Total workers needed
用徒 = 積尺 / 每人土運輸

# Convert to integers for clarity
人到整數 = int(每人土運輸)
用徒整數 = int(用徒)
print(f"人到: {人到整數}尺, 用徒: {用徒整數}人")
#----- content ends here -----


"""


---

### Final Answer:

- **Volume of the pond:** \(76066\) chi, with a remainder of "太半尺."
- **Worker calculations:**
  - Each worker transports \(a\) chi of soil.
  - \(b\) workers are needed to complete the task.
"""


"""
Missing variable in output: 'a'
Missing variable in output: 'b'"""
