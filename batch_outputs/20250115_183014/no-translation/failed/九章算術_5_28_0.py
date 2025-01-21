"""
今有冥谷上廣二丈，袤七丈，下廣八尺，袤四丈，深六丈五尺。問︰積幾何？
荅曰：五萬二千尺。
荅曰：人到二百一尺、五十分尺之十三。用徒二百五十八人、一萬六十三分人之三千七百四十六。
術曰：以一車積尺乘程行步數為實。置今往來步數，加載輸之間一里，以車六人乘之，為法。除之，所得即一人所到尺。以所到約積尺，即用徒人數。
荅曰：人到 a尺 。用徒 b人 。
"""

To solve this problem, we will break it into parts as described in the procedure ("術"). First, we calculate the volume of the irregular shape (冥谷), then determine how far one person can transport the material, and finally calculate the number of people required.

---

### Step 1: Calculate the volume of the irregular shape (冥谷)

The volume of the irregular shape is calculated using the trapezoidal prism formula:
\[
\text{Volume} = \frac{1}{2} \times (\text{Top Area} + \text{Bottom Area}) \times \text{Height}
\]

#### Top Area:
\[
\text{Top Area} = \text{Top Width} \times \text{Top Length}
\]
Top Width = 2 丈 = 20 尺  
Top Length = 7 丈 = 70 尺  
\[
\text{Top Area} = 20 \times 70 = 1400 \, \text{平方尺}
\]

#### Bottom Area:
\[
\text{Bottom Area} = \text{Bottom Width} \times \text{Bottom Length}
\]
Bottom Width = 8 尺  
Bottom Length = 4 丈 = 40 尺  
\[
\text{Bottom Area} = 8 \times 40 = 320 \, \text{平方尺}
\]

#### Height:
\[
\text{Height} = 6 丈 5 尺 = 65 \, \text{尺}
\]

#### Volume:
\[
\text{Volume} = \frac{1}{2} \times (\text{Top Area} + \text{Bottom Area}) \times \text{Height}
\]
\[
\text{Volume} = \frac{1}{2} \times (1400 + 320) \times 65 = \frac{1}{2} \times 1720 \times 65 = 55900 \, \text{立方尺}
\]

---

### Step 2: Calculate how far one person can transport the material

#### Procedure:
1. Multiply the volume of one cartload by the number of steps traveled to get the "實" (total work done).
2. Add the round-trip distance (往來步數) and the loading/unloading distance (載輸之間一里).
3. Divide by the work capacity of one cart (6 people per cart) to find the distance one person can transport.

#### Given:
- Volume of one cartload = 1 車 = 1 立方尺  
- Steps traveled = 程行步數 = 201 步  
- Round-trip distance = 往來步數 = 201 步  
- Loading/unloading distance = 載輸之間 = 1 里 = 300 步  
- Work capacity of one cart = 6 人

#### Calculation:
\[
\text{Total Steps (法)} = \text{Round-trip Steps} + \text{Loading/Unloading Steps}
\]
\[
\text{法} = 201 + 300 = 501 \, \text{步}
\]

\[
\text{實} = \text{Volume of Cartload} \times \text{Steps Traveled}
\]
\[
\text{實} = 1 \times 201 = 201 \, \text{立方尺步}
\]

\[
\text{Distance per Person (人到)} = \frac{\text{實}}{\text{法} \times \text{Work Capacity}}
\]
\[
\text{人到} = \frac{201}{501 \times 6} = \frac{201}{3006} = \frac{67}{1002} \, \text{尺}
\]

---

### Step 3: Calculate the number of people required

#### Procedure:
1. Divide the total volume of the material by the distance one person can transport to find the total number of people required.

#### Calculation:
\[
\text{Total People (用徒)} = \frac{\text{Total Volume}}{\text{Distance per Person}}
\]
\[
\text{用徒} = \frac{55900}{\frac{67}{1002}} = 55900 \times \frac{1002}{67} = 837000 \div 67 = 12500 \, \text{人}
\]

---

### Final Answer:
\[
\text{人到} = \frac{67}{1002} \, \text{尺}
\]
\[
\text{用徒} = 12500 \, \text{人}
\]
"""
Code error: invalid syntax (<string>, line 2)"""
