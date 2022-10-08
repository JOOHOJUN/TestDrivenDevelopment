"""
31p / 모든 규칙을 충족하는 경우를 우선 테스트하기로함
그럼에도, 조건 충족에서 일부분(=>"강함") 목적만을 우선 구현함
"""

import unittest
from PasswordStrengthMeter import PasswordStrength
from PasswordStrengthMeter import PasswordStrengthMeter

class PasswordStrengthMeterTest(unittest.TestCase):

    def test_meetsAllCriteria_Then_Strong(self):
        #test init

        #do
        passwordstrengthmeter_ = PasswordStrengthMeter() # Checker보다 Meter를 더 많이 쓴다고함
        result = passwordstrengthmeter_.get_meter(password="ab12!@AB")
        passwordstrengthmeter_ = PasswordStrengthMeter()
        result2 = passwordstrengthmeter_.get_meter(password="abc1!Add") # 강함을 부여받을 예시데이터

        #assert
        self.assertEqual(PasswordStrength.강함, result)
        self.assertEqual(PasswordStrength.강함, result2)

    def test_meetsAllCriteria_Then_Normal(self):
        #test init

        #do
        passwordstrengthmeter_ = PasswordStrengthMeter() # Checker보다 Meter를 더 많이 쓴다고함
        result = passwordstrengthmeter_.get_meter(password="ab12!@A")

        #assert
        self.assertEqual(PasswordStrength.보통, result)