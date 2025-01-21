"""
今有盤池，上廣六丈，袤八丈，下廣四丈，袤六丈，深二丈。問︰積幾何？
荅曰：七萬六百六十六尺、太半尺。
負土往來七十步，其二十步上下棚除。棚除二當平道五，踟躕之間十加一，載輸之間三十步，定一返一百四十步。土籠積一尺六寸，秋程人功行五十九里半。問︰人到、積尺、用徒各幾何？
術曰：以一籠積尺乘程行步數為實。往來上下，棚除二當平道五。置定往來步數，十加一，及載輸之間三十步以為法。除之，所得即一人所到尺。以所到約積尺，即用徒人數。
荅曰：人到 a尺 。用徒 b人 。
"""

### Part 1: Calculating the volume of the pond (積幾何)

"""
Suppose there is a pond. The top width is 6 zhang, the top length is 8 zhang. 
The bottom width is 4 zhang, the bottom length is 6 zhang. The depth is 2 zhang.
Question: what is the volume?

Answer: 76066.5 chi³ (七萬六百六十六尺、太半尺).
"""

# 上廣六丈，袤八丈
上廣 = 6 * 10  # Convert zhang to chi
上袤 = 8 * 10  # Convert zhang to chi

# 下廣四丈，袤六丈
下廣 = 4 * 10  # Convert zhang to chi
下袤 = 6 * 10  # Convert zhang to chi

# 深二丈
深 = 2 * 10  # Convert zhang to chi

# Calculate the average area of the top and bottom
上面積 = 上廣 * 上袤
下面積 = 下廣 * 下袤
平均面積 = Fraction(上面積 + 下面積, 2)

# Calculate the volume
積 = 平均面積 * 深

# Convert to chi³
積尺 = 積

# Answer for the first part
a1 = 積尺  # 76066.5 chi³

### Part 2: Calculating the work required (人到、積尺、用徒)

"""
The procedure says:
1. Multiply the volume of one basket of earth (土籠積尺) by the total number of steps in the journey (程行步數) to get the dividend.
2. For the round trip, the shelves (棚除) are treated such that 2 steps on the shelves are equivalent to 5 steps on flat ground.
3. Place the total round-trip steps (定往來步數), add 10%, and include the 30 steps for loading and unloading (載輸之間) to form the divisor.
4. Divide the dividend by the divisor to get the amount of earth one person can transport (一人所到尺).
5. Divide the total volume of earth by the amount one person can transport to get the number of workers required (用徒人數).

Answer: *a* chi per person, *b* workers.
"""

# 土籠積一尺六寸
土籠積尺 = 1 + Fraction(6, 10)  # 1 chi 6 cun = 1.6 chi

# 秋程人功行五十九里半
程行里 = 59 + Fraction(1, 2)  # 59.5 li
程行步數 = 程行里 * 300  # 1 li = 300 steps

# 負土往來七十步
往來步數 = 70

# 其二十步上下棚除
上下棚除 = 20

# 棚除二當平道五
棚除平道比 = Fraction(2, 5)

# Adjust the steps for棚除
有效步數 = 往來步數 - 上下棚除 + (上下棚除 * 棚除平道比)

# 踟躕之間十加一
踟躕加成 = Fraction(10, 100)  # 10%
有效步數 = 有效步數 * (1 + 踟躕加成)

# 載輸之間三十步
載輸步數 = 30
有效步數 += 載輸步數

# 定一返一百四十步
定往返步數 = 140

# Calculate the amount of earth one person can transport
實 = 土籠積尺 * 程行步數
法 = 有效步數
人到尺 = Fraction(實, 法)

# Calculate the number of workers required
用徒 = Fraction(積尺, 人到尺)

# Answer for the second part
a2 = 人到尺  # chi per person
b = 用徒  # number of workers

# Final answers
a1, a2, b
"""
Missing variable in output: 'a'
Variable 'b' has wrong value. Expected: 53000/153, Actual: 4020/17"""
