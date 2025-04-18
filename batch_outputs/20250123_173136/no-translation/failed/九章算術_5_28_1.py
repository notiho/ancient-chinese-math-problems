"""
今有冥谷上廣二丈，袤七丈，下廣八尺，袤四丈，深六丈五尺。問︰積幾何？
荅曰：五萬二千尺。
載土往來二百步，載輸之間一里，程行五十八里，六人共車，車載三十四尺七寸。問︰人到積尺及用徒各幾何？
術曰：以一車積尺乘程行步數為實。置今往來步數，加載輸之間一里，以車六人乘之，為法。除之，所得即一人所到尺。以所到約積尺，即用徒人數。
荅曰：人到 a尺 。用徒 b人 。
"""

### 第一部分：計算冥谷積幾何

# 上廣二丈，袤七丈
上廣 = 2 * 10  # 轉換為尺
上袤 = 7 * 10  # 轉換為尺

# 下廣八尺，袤四丈
下廣 = 8
下袤 = 4 * 10  # 轉換為尺

# 深六丈五尺
深 = 6 * 10 + 5  # 轉換為尺

# 計算冥谷積
# 冥谷積公式：積 = 深 * ((上廣 * 上袤 + 下廣 * 下袤) / 2)
積 = 深 * ((上廣 * 上袤 + 下廣 * 下袤) / 2)

# 驗算積
assert 積 == 52000  # 答案應為 52000 尺

### 第二部分：計算人到積尺及用徒

# 載土往來二百步
往來步數 = 200

# 載輸之間一里
載輸步數 = 1 * 300  # 一里等於 300 步

# 程行五十八里
程行步數 = 58 * 300  # 一里等於 300 步

# 六人共車
車人數 = 6

# 車載三十四尺七寸
車載積尺 = 34 + Fraction(7, 10)  # 轉換為小數表示

# 計算一人所到尺
# 以一車積尺乘程行步數為實
實 = 車載積尺 * 程行步數

# 置今往來步數，加載輸之間一里
法 = (往來步數 + 載輸步數) * 車人數

# 除之，所得即一人所到尺
人到尺 = Fraction(實, 法)

# 計算用徒人數
# 以所到約積尺，即用徒人數
用徒人數 = Fraction(積, 人到尺)

# 簡化用徒人數為整數
用徒人數 = 用徒人數.numerator // 用徒人數.denominator

# 答案
a = 人到尺
b = 用徒人數
"""
Code error: """
