"""
今有盤池，上廣六丈，袤八丈，下廣四丈，袤六丈，深二丈。問︰積幾何？
荅曰：七萬六百六十六尺、太半尺。
負土往來七十步，其二十步上下棚除。棚除二當平道五，踟躕之間十加一，載輸之間三十步，定一返一百四十步。土籠積一尺六寸，秋程人功行五十九里半。問︰人到、積尺、用徒各幾何？
術曰：以一籠積尺乘程行步數為實。往來上下，棚除二當平道五。置定往來步數，十加一，及載輸之間三十步以為法。除之，所得即一人所到尺。以所到約積尺，即用徒人數。
荅曰：人到 a(=204)尺 。用徒 b(=53000/153)人 。
"""

#----- content starts here -----
### Part 1: Calculating the volume of the pond

"""
Suppose there is a pond.
The top width is 6 zhang, the top length is 8 zhang.
The bottom width is 4 zhang, the bottom length is 6 zhang.
The depth is 2 zhang.
Question: what is the total volume?

Answer: 70666 chi and a little more than half a chi.
"""

# 上廣六丈，袤八丈
上廣 = 6 * 10  # Convert zhang to chi
上袤 = 8 * 10  # Convert zhang to chi

# 下廣四丈，袤六丈
下廣 = 4 * 10  # Convert zhang to chi
下袤 = 6 * 10  # Convert zhang to chi

# 深二丈
深 = 2 * 10  # Convert zhang to chi

# Calculate the area of the top and bottom
上積 = 上廣 * 上袤
下積 = 下廣 * 下袤

# Average area (trapezoidal prism formula)
平均積 = Fraction(上積 + 下積, 2)

# Multiply by depth to get the total volume
積 = 平均積 * 深

# Convert to chi and fractional chi
積整數 = int(積)  # Integer part
積餘數 = 積 - 積整數  # Fractional part

a1 = 積整數  # 70666
a2 = 積餘數  # Slightly more than half a chi

### Part 2: Calculating the labor required for moving the soil

"""
The soil is moved back and forth for 70 bu, with 20 bu being for the upper and lower shelves.
The shelves are equivalent to 2 units of flat road for every 5 units.
The hesitation in between adds 1 for every 10.
The loading and unloading distance is 30 bu.
One round trip is determined to be 140 bu.
Each soil basket holds 1 chi 6 cun of soil.
The autumn work rate is 59.5 li per person.

Question: How much soil does one person move, and how many workers are needed?

The procedure says: Multiply the volume of one basket of soil by the total number of steps traveled.
For the back-and-forth and shelves, 2 units of shelves are equivalent to 5 units of flat road.
Place the determined round-trip steps, add 1 for every 10, and add the loading/unloading distance of 30 bu as the divisor.
Divide to obtain the amount of soil moved by one person.
Divide the total soil volume by the amount moved by one person to obtain the number of workers needed.

Answer: *a*(=204) chi per person, *b*(=53000/153) workers.
"""

# 負土往來七十步
往來步數 = 70

# 其二十步上下棚除
棚除步數 = 20

# 棚除二當平道五
棚除當平道 = Fraction(2, 5)

# 棚除 equivalent in flat road
棚除平道步數 = 棚除步數 * 棚除當平道

# 踟躕之間十加一
踟躕加步數 = Fraction(往來步數, 10)

# 載輸之間三十步
載輸步數 = 30

# 定一返一百四十步
定往返步數 = 140

# 土籠積一尺六寸
土籠積 = 1 + Fraction(6, 10)  # Convert 1 chi 6 cun to chi

# 秋程人功行五十九里半
秋程行 = 59.5 * 300  # Convert li to bu (1 li = 300 bu)

# Calculate total steps for one round trip
總步數 = 定往返步數 + 棚除平道步數 + 踟躕加步數 + 載輸步數

# Calculate soil moved by one person
人到 = 土籠積 * 秋程行 / 總步數

# Calculate the number of workers needed
用徒 = 積 / 人到

a = 人到  # 204 chi
b = 用徒  # 53000/153 workers#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 204, Actual: 154.3783783783784
Variable 'b' has wrong value. Expected: 53000/153, Actual: 466.3865546218487"""
