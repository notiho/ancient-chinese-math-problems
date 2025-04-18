"""
今有盤池，上廣六丈，袤八丈，下廣四丈，袤六丈，深二丈。問︰積幾何？
荅曰：七萬六百六十六尺、太半尺。
負土往來七十步，其二十步上下棚除。棚除二當平道五，踟躕之間十加一，載輸之間三十步，定一返一百四十步。土籠積一尺六寸，秋程人功行五十九里半。問︰人到、積尺、用徒各幾何？
術曰：以一籠積尺乘程行步數為實。往來上下，棚除二當平道五。置定往來步數，十加一，及載輸之間三十步以為法。除之，所得即一人所到尺。以所到約積尺，即用徒人數。
荅曰：人到 a尺 。用徒 b人 。
"""

"""
### 第一部分：計算盤池的積


### 第二部分：計算人到、積尺、用徒

"""


# 上廣六丈，袤八丈
上廣 = 6
上袤 = 8

# 下廣四丈，袤六丈
下廣 = 4
下袤 = 6

# 深二丈
深 = 2

# 計算上底面積
上底積 = 上廣 * 上袤

# 計算下底面積
下底積 = 下廣 * 下袤

# 計算平均底面積
平均底積 = Fraction(上底積 + 下底積, 2)

# 計算盤池積
盤池積 = 平均底積 * 深

# 換算為尺（1丈 = 10尺）
盤池積_尺 = 盤池積 * 100

# 答案
積 = Fraction(盤池積_尺)

# 土籠積一尺六寸
土籠積 = Fraction(1, 1) + Fraction(6, 10)

# 秋程人功行五十九里半
程行 = Fraction(59, 1) + Fraction(1, 2)

# 一里 = 180步，換算程行步數
程行步數 = 程行 * 180

# 往來七十步，其二十步上下棚除
往來步數 = 70
上下棚除 = 20

# 棚除二當平道五
棚除當平道 = Fraction(2, 5)

# 棚除步數換算為平道步數
棚除步數 = 上下棚除 * 棚除當平道

# 十加一，及載輸之間三十步
十加一 = Fraction(11, 10)
載輸步數 = 30

# 定一返一百四十步
定一返步數 = 140

# 計算法
法 = (往來步數 - 上下棚除) * 十加一 + 棚除步數 + 載輸步數 + 定一返步數

# 以一籠積尺乘程行步數為實
實 = 土籠積 * 程行步數

# 人到尺
人到 = Fraction(實, 法)

# 以所到約積尺，即用徒人數
用徒 = Fraction(盤池積_尺, 人到)

# 答案
a = 人到
b = 用徒


"""

"""


"""
Variable 'a' has wrong value. Expected: 204, Actual: 17136/233
Variable 'b' has wrong value. Expected: 53000/153, Actual: 11650/119"""
