
import enum

class PasswordStrength(enum.Enum):
    강함 = enum.auto()
    보통 = enum.auto()

class PasswordStrengthMeter:
    """암호의 보안 강도 확인하는 클래스"""
    def __init__(self):
        pass

    def get_meter(self, password):
        if len(password) < 8:
            return PasswordStrength.보통 # 보통과 강함 조건 코드 추가
        return PasswordStrength.강함