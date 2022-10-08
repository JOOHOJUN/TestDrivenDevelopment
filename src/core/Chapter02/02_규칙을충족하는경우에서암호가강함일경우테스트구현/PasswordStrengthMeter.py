#sub02
import enum

class PasswordStrength(enum.Enum):
    강함 = enum.auto()

class PasswordStrengthMeter:
    """암호의 보안 강도 확인하는 클래스"""
    def __init__(self):
        pass

    def get_meter(self, password):
        return PasswordStrength.강함