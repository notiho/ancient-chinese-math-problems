"""
今有盤池，上廣六丈，袤八丈，下廣四丈，袤六丈，深二丈。問︰積幾何？
荅曰：七萬六百六十六尺、太半尺。
負土往來七十步，其二十步上下棚除。棚除二當平道五，踟躕之間十加一，載輸之間三十步，定一返一百四十步。土籠積一尺六寸，秋程人功行五十九里半。問︰人到、積尺、用徒各幾何？
術曰：以一籠積尺乘程行步數為實。往來上下，棚除二當平道五。置定往來步數，十加一，及載輸之間三十步以為法。除之，所得即一人所到尺。以所到約積尺，即用徒人數。
荅曰：人到 a尺 。用徒 b人 。
"""

#----- content starts here -----
### Part 1: Calculating the volume of the pond (積幾何)

The pond has the following dimensions:
- Top width: 6 zhang
- Top length: 8 zhang
- Bottom width: 4 zhang
- Bottom length: 6 zhang
- Depth: 2 zhang

The pond is a frustum of a rectangular pyramid. The formula for the volume of a frustum is:

\[
V = \frac{h}{3} \times (A_1 + A_2 + \sqrt{A_1 \cdot A_2})
\]

Where:
- \(h\) is the height (depth of the pond)
- \(A_1\) is the area of the top rectangle
- \(A_2\) is the area of the bottom rectangle

#### Step 1: Calculate the areas of the top and bottom
\[
A_1 = \text{Top width} \times \text{Top length} = 6 \times 8 = 48 \, \text{zhang}^2
\]
\[
A_2 = \text{Bottom width} \times \text{Bottom length} = 4 \times 6 = 24 \, \text{zhang}^2
\]

#### Step 2: Calculate the volume
\[
V = \frac{2}{3} \times (48 + 24 + \sqrt{48 \cdot 24})
\]
\[
\sqrt{48 \cdot 24} = \sqrt{1152} \approx 34
\]
\[
V = \frac{2}{3} \times (48 + 24 + 34) = \frac{2}{3} \times 106 = 70.6667 \, \text{zhang}^3
\]

Convert \(zhang^3\) to \(chi^3\) (since 1 zhang = 10 chi):
\[
V = 70.6667 \times 1000 = 70666.7 \, \text{chi}^3
\]

Answer for the first part:
- Volume: \(70666 \, \text{chi}^3\), plus a little over half a chi.

---

### Part 2: Calculating human labor (人到、用徒)

#### Given:
- One basket holds \(1 \, \text{chi} \, 6 \, \text{cun} = 1.6 \, \text{chi}\)
- Total volume of soil to move: \(70666.7 \, \text{chi}^3\)
- Round trip walking distance: \(70 \, \text{bu}\)
- Subtract \(20 \, \text{bu}\) for shelving (棚除)
- Shelving: \(2 \, \text{bu}\) is equivalent to \(5 \, \text{bu}\) on flat ground
- Hesitation (踟躕): Add \(10\%\) of the remaining distance
- Loading/unloading adds \(30 \, \text{bu}\)
- Total round trip distance: \(140 \, \text{bu}\)
- Daily work: \(59.5 \, \text{li}\)

#### Step 1: Adjust the round trip distance
\[
\text{Shelving adjustment: } 20 \, \text{bu} \times \frac{5}{2} = 50 \, \text{bu}
\]
\[
\text{Remaining distance: } 70 \, \text{bu} - 20 \, \text{bu} + 50 \, \text{bu} = 100 \, \text{bu}
\]
\[
\text{Add hesitation: } 100 \, \text{bu} \times 1.1 = 110 \, \text{bu}
\]
\[
\text{Add loading/unloading: } 110 \, \text{bu} + 30 \, \text{bu} = 140 \, \text{bu}
\]

#### Step 2: Calculate the distance per basket
Each basket holds \(1.6 \, \text{chi}\), and the total distance per basket is \(140 \, \text{bu}\).

#### Step 3: Calculate the total number of baskets
\[
\text{Total baskets: } \frac{\text{Total volume}}{\text{Basket volume}} = \frac{70666.7}{1.6} \approx 44167 \, \text{baskets}
\]

#### Step 4: Calculate the total distance
\[
\text{Total distance: } 44167 \times 140 = 6183380 \, \text{bu}
\]

Convert \(bu\) to \(li\) (since 1 li = 300 bu):
\[
\text{Total distance: } \frac{6183380}{300} \approx 20611.27 \, \text{li}
\]

#### Step 5: Calculate the number of workers
Each worker can travel \(59.5 \, \text{li}\) per day. The total number of worker-days is:
\[
\text{Worker-days: } \frac{20611.27}{59.5} \approx 346.4 \, \text{worker-days}
\]

Answer for the second part:
- Total distance per person: \(a = 20611.27 \, \text{li}\)
- Total workers needed: \(b = 347 \, \text{workers}\) (rounding up).#----- content ends here -----

"""
Code error: invalid syntax (<string>, line 4)"""
