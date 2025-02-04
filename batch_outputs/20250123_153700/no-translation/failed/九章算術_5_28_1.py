"""
今有冥谷上廣二丈，袤七丈，下廣八尺，袤四丈，深六丈五尺。問︰積幾何？
荅曰：五萬二千尺。
荅曰：人到二百一尺、五十分尺之十三。用徒二百五十八人、一萬六十三分人之三千七百四十六。
術曰：以一車積尺乘程行步數為實。置今往來步數，加載輸之間一里，以車六人乘之，為法。除之，所得即一人所到尺。以所到約積尺，即用徒人數。
荅曰：人到 a尺 。用徒 b人 。
"""

To solve this problem, we need to calculate the volume of the irregular prism (冥谷) and then determine how far one person can transport the material and how many people are required to move the entire volume. Let's break it down step by step.

---

### Step 1: Calculate the volume of the irregular prism (冥谷)

The volume of an irregular prism can be approximated using the average of the top and bottom areas multiplied by the height.

#### Top dimensions:
- 上廣 (top width) = 2 丈 = 20 尺
- 袤 (top length) = 7 丈 = 70 尺

#### Bottom dimensions:
- 下廣 (bottom width) = 8 尺
- 袤 (bottom length) = 4 丈 = 40 尺

#### Depth (height):
- 深 = 6 丈 5 尺 = 65 尺

#### Average area:
Top area = 上廣 × 袤 = 20 × 70 = 1400 尺²  
Bottom area = 下廣 × 袤 = 8 × 40 = 320 尺²  
Average area = (Top area + Bottom area) ÷ 2 = (1400 + 320) ÷ 2 = 860 尺²

#### Volume:
Volume = Average area × Depth = 860 × 65 = 55900 尺³

---

### Step 2: Calculate how far one person can transport material

#### Given:
- 一車積 = 1 丈³ = 1000 尺³
- 往來步數 = 1 里 = 300 步
- 車需 6 人

#### Procedure:
1. Calculate the total steps for one round trip:
   Total steps = 往來步數 + 載輸間步數 = 300 + 300 = 600 步

2. Calculate the "法" (denominator for the calculation):
   法 = 車需人數 × Total steps = 6 × 600 = 3600

3. Calculate how far one person can transport material:
   所到尺 = 一車積 × Total steps ÷ 法  
   所到尺 = 1000 × 600 ÷ 3600 = 1000 ÷ 6 = 166.67 尺

---

### Step 3: Calculate the number of people required

#### Procedure:
1. Use the total volume and the distance one person can transport:
   用徒人數 = 積 ÷ 所到尺  
   用徒人數 = 55900 ÷ 166.67 ≈ 335 人

---

### Final Answer:
- 人到 a = 166.67 尺 (approximately)  
- 用徒 b = 335 人 (approximately)  


"""
Code error: unterminated string literal (detected at line 2) (<string>, line 2)"""
