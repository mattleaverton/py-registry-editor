from win32api import Beep, RegOpenKeyEx, RegOpenCurrentUser, RegCloseKey, RegQueryInfoKey, RegEnumKeyEx
from winreg import HKEY_LOCAL_MACHINE, HKEY_CURRENT_USER, HKEYType, KEY_READ


class Node(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


if __name__ == "__main__":
    hkcu_handle = RegOpenKeyEx(HKEY_CURRENT_USER,
                               None,
                               0,
                               KEY_READ, )

    hkcu_sub_keys, hkcu_values, hkcu_last_modified = RegQueryInfoKey(hkcu_handle)

    if hkcu_sub_keys > 0:
        for k in RegEnumKeyEx(hkcu_handle):
            k_name, k_reserved, k_class, k_last_write_time = k
            print(f"{k_name} {k_class} {k_last_write_time.date().isoformat()}")

    RegCloseKey(hkcu_handle)
