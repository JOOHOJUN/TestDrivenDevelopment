
import enum

class PasswordStrength(enum.Enum):
    강함 = enum.auto()
    보통 = enum.auto()
    약함 = enum.auto()
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

        lengthEnough = len(password) >= 8
        containsNum = self._get_meetsContainingNumberCriteria(password=password)
        containsUpp = self._get_meetsContainingUpperCriteria(password=password)
        
        if all([not containsUpp, not containsNum, lengthEnough]): return PasswordStrength.약함
        if all([not containsUpp, containsNum, not lengthEnough]): return PasswordStrength.약함

        if not lengthEnough: return PasswordStrength.보통
        if not containsUpp: return PasswordStrength.보통
        if not containsNum: return PasswordStrength.보통

        return PasswordStrength.강함

    def _get_meetsContainingNumberCriteria(self, password) -> bool:
        """암호에 숫자가 있는지 확인 - 있으면 True"""
        return any(x.isdigit() for x in password)

    def _get_meetsContainingUpperCriteria(self, password) -> bool: # 리팩토링
        """암호에 대문자가 있는지 확인 """
        return any([char.isupper() for char in password])