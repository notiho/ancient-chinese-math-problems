"""
今有盤池上廣六丈袤八丈下廣四丈袤六丈深二丈問積幾何
荅曰七萬六百六十六尺太半尺
負土往來七十步其二十步上下棚除棚除二當平道五踟躕之間十加一載輸之間三十步定一返一百四十步土籠積一尺六寸秋程人功行五十九里半問人到積尺用徒各幾何
術曰以一籠積尺乘程行步數為實往來上下棚除二當平道五置定往來步數十加一及載輸之間三十步以為法除之所得即一人所到尺以所到約積尺即用徒人數
荅曰人到 a尺 用徒 b人 
"""

"""
Suppose there is a basin-shaped pond. 
The upper width is 6 zhang, the upper length is 8 zhang. 
The lower width is 4 zhang, the lower length is 6 zhang. 
The depth is 2 zhang.
Question: what is the volume?

Answer: 76,066.5 cubic chi.

For moving soil: 
The round trip is 70 bu, of which 20 bu are for the upper and lower shelves. 
The shelves are equivalent to 2 bu of flat ground. 
For the flat ground, 5 bu are for hesitation, and 10 bu are for adding one load. 
The transportation distance is 30 bu. 
One round trip is fixed at 140 bu. 
A soil basket holds 1 chi 6 cun of soil. 
In autumn, one person can travel 59.5 li.

Question: how much soil does one person move, and how many workers are needed?

The procedure says: Multiply the volume of one basket of soil by the number of steps traveled in one trip to get the dividend. 
For the divisor, take the round-trip steps, add 10 for hesitation, and add 30 for the transportation distance. 
Divide the dividend by the divisor to get the amount of soil moved by one person. 
Divide the total soil volume by the amount moved by one person to get the number of workers needed.

Answer: one person moves *a* cubic chi, and *b* workers are needed.
"""

# 上廣六丈袤八丈
上廣 = 6
上袤 = 8

# 下廣四丈袤六丈
下廣 = 4
下袤 = 6

# 深二丈
深 = 2

# 計算池積
# 上面積 = 上廣 * 上袤
上面積 = 上廣 * 上袤

# 下面積 = 下廣 * 下袤
下面積 = 下廣 * 下袤

# 平均面積 = (上面積 + 下面積) / 2
平均面積 = (上面積 + 下面積) / 2

# 積 = 平均面積 * 深
積 = 平均面積 * 深 * 1000  # 轉換為立方尺 (1 丈 = 10 尺)

# 積結果
總積 = Fraction(76066, 2)  # 七萬六百六十六尺太半尺

# 土籠積一尺六寸
土籠積 = Fraction(16, 10)  # 1 尺 6 寸 = 1.6 尺

# 秋程人功行五十九里半
秋程 = 59.5 * 300  # 1 里 = 300 步

# 負土往來七十步
往來步數 = 70

# 其二十步上下棚
上下棚步數 = 20

# 棚除二當平道五
平道步數 = Fraction(上下棚步數, 2) + 5

# 踟躕之間十加一
踟躕步數 = 10 + 1

# 載輸之間三十步
載輸步數 = 30

# 定一返一百四十步
定步數 = 140

# 計算法
法 = 定步數 + 踟躕步數 + 載輸步數

# 計算一人所到尺
一人所到尺 = Fraction(土籠積 * 秋程, 法)

# 計算用徒人數
用徒人數 = Fraction(總積, 一人所到尺)

# 結果
a = 一人所到尺
b = 用徒人數
"""
Code error: both arguments should be Rational instances"""
