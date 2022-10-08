
import enum

class PasswordStrength(enum.Enum):
    강함 = enum.auto()
    보통 = enum.auto()

#sub01
class PasswordStrengthMeter:
    """암호의 보안 강도 확인하는 클래스"""
    def __init__(self):
        pass

    def get_meter(self, password):
        if len(password) < 8:
            return PasswordStrength.보통

        containsNum = any(x.isdigit() for x in password) # 숫자를 하나라도 포함하면 True 아니면 False
        if containsNum:
            return PasswordStrength.강함
        else:
            return PasswordStrength.보통

#sub02 - 코드 리팩토링
class PasswordStrengthMeter:
    """암호의 보안 강도 확인하는 클래스"""
    def __init__(self):
        pass

    def get_meter(self, password):
        if len(password) < 8:
            return PasswordStrength.보통

        containsNum = self._meetsContainingNumberCriteria(password=password)
        if containsNum:
            return PasswordStrength.강함
        else:
            return PasswordStrength.보통

    def _meetsContainingNumberCriteria(self,password): # 리팩토링
        """암호에 숫자가 있는지 확인 - 있으면 True"""
        return any(x.isdigit() for x in password)