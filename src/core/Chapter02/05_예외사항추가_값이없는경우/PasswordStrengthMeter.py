
import enum

class PasswordStrength(enum.Enum):
    강함 = enum.auto()
    보통 = enum.auto()
    유효하지않음 = enum.auto()

class PasswordStrengthMeter:
    """암호의 보안 강도 확인하는 클래스"""
    def __init__(self):
        pass

    def get_meter(self, password):
        if password is None:
            return PasswordStrength.유효하지않음
        if not password:
            return PasswordStrength.유효하지않음
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