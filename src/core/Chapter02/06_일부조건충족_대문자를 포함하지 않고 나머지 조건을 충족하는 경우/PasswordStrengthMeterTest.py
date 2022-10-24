"""
31p / 모든 규칙을 충족하는 경우를 우선 테스트하기로함
그럼에도, 조건 충족에서 일부분(=>"강함") 목적만을 우선 구현함
"""

import unittest
from PasswordStrengthMeter import PasswordStrength
from PasswordStrengthMeter import PasswordStrengthMeter

class PasswordStrengthMeterTest(unittest.TestCase):

    def assertStrength(self, password: str, expMeter: PasswordStrength):
        """암호가 수준에 맞는지 확인"""
        passwordstrengthmeter_ = PasswordStrengthMeter() # Checker보다 Meter를 더 많이 쓴다고함
        result = passwordstrengthmeter_.get_meter(password=password)
        self.assertEqual(expMeter, result)

    def test_meetsAllCriteria_Then_Strong(self): # 강함일 경우 테스트
        """암호가 강함일 때. 강함으로 나오는 것을 확인하는 함수(테스트)"""
        #test init

        #do

        #assert
        self.assertStrength(password="ab12!@AB",
                            expMeter=PasswordStrength.강함)
        self.assertStrength(password="abc1!Add",
                            expMeter=PasswordStrength.강함)

    def test_meetsAllCriteria_Then_Normal(self): # 보통일 경우 테스트
        """암호가 보통인 조건일 때. 보통으로 나오는 것을 확인하는 함수(테스트)"""
        #test init

        #do

        #assert
        self.assertStrength(password="ab12!@A",
                            expMeter=PasswordStrength.보통)

    def test_meetsOtherCriteria_except_for_number_then_Normal(self):
        """암호가 숫자를 포함하지 않지만 보통일 때, 보통으로 나오는 것을 확인하는 함수(테스트)"""
        #test init

        #do

        #assert
        self.assertStrength(password="ab!@ABqwer",
                            expMeter=PasswordStrength.보통)


    def test_nullInput_Then_Invalid(self):
        """입력텍스트가 유효하지 않을 때"""
        #test init

        #do

        #assert
        self.assertStrength(password=None, expMeter=PasswordStrength.유효하지않음)

    def test_emptyInput_Then_Invalid(self):
        """입력텍스트가 공백("")일 때"""
        #test init

        #do

        #assert
        self.assertStrength(password="", expMeter=PasswordStrength.유효하지않음)

    def test_meetsOtherCriteria_except_for_Uppercase_Then_Normal(self):
        """입력텍스트가 대문자를 포함하지 않고 나머지 조건을 충족하는 경우"""
        #test init

        #do

        #assert
        self.assertStrength(password="ab12!@df", expMeter=PasswordStrength.보통)