# enums.py
#
# Authors:
#   - Coumes Quentin <coumes.quentin@gmail.com>


from enum import IntEnum, unique



@unique
class SandboxErrCode(IntEnum):
    UNKNOWN = -1
    TIMEOUT = -2
    RESULT_NOT_FOUND = -3
    RESULT_NOT_UTF8 = -4
