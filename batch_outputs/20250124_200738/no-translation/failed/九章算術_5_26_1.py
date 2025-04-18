"""
今有盤池，上廣六丈，袤八丈，下廣四丈，袤六丈，深二丈。問︰積幾何？
荅曰：七萬六百六十六尺、太半尺。
負土往來七十步，其二十步上下棚除。棚除二當平道五，踟躕之間十加一，載輸之間三十步，定一返一百四十步。土籠積一尺六寸，秋程人功行五十九里半。問︰人到、積尺、用徒各幾何？
術曰：以一籠積尺乘程行步數為實。往來上下，棚除二當平道五。置定往來步數，十加一，及載輸之間三十步以為法。除之，所得即一人所到尺。以所到約積尺，即用徒人數。
荅曰：人到 a尺 。用徒 b人 。
"""

#----- content starts here -----
### 第一部分：計算盤池的積

# 上廣六丈，袤八丈
上廣 = 6
上袤 = 8

# 下廣四丈，袤六丈
下廣 = 4
下袤 = 6

# 深二丈
深 = 2

# 計算上底面積
上底面積 = 上廣 * 上袤

# 計算下底面積
下底面積 = 下廣 * 下袤

# 計算平均底面積
平均底面積 = Fraction(上底面積 + 下底面積, 2)

# 計算盤池積
盤池積 = 平均底面積 * 深

# 換算為尺（1丈 = 10尺）
盤池積_尺 = 盤池積 * 10 * 10 * 10

# 盤池積結果
積 = Fraction(盤池積_尺)

### 第二部分：計算人到與用徒

# 土籠積一尺六寸（1尺6寸 = 1.6尺）
土籠積 = Fraction(16, 10)

# 秋程人功行五十九里半（1里 = 180步）
程行步數 = Fraction(59, 2) * 180

# 負土往來七十步
往來步數 = 70

# 其二十步上下棚除
棚除步數 = 20

# 棚除二當平道五
棚除當平道 = Fraction(2, 5)

# 踟躕之間十加一
踟躕加 = Fraction(11, 10)

# 載輸之間三十步
載輸步數 = 30

# 定一返一百四十步
定一返步數 = 140

# 計算棚除平道步數
棚除平道步數 = 棚除步數 * 棚除當平道

# 計算法（總步數）
法 = 定一返步數 + 踟躕加 * 棚除平道步數 + 載輸步數

# 計算一人所到尺
人到 = Fraction(土籠積 * 程行步數, 法)

# 計算用徒人數
用徒 = Fraction(積, 人到)

# 結果
a = 人到
b = 用徒#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 204, Actual: 7080/149
Variable 'b' has wrong value. Expected: 53000/153, Actual: 89400/59"""
