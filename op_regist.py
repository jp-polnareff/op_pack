from ctypes import windll

from win32com.client import Dispatch

# 加载免注册dll
dll = windll.LoadLibrary("./op/tools_64.dll")
# 调用setupW函数
result = dll.setupW("./op/op_x64.dll")
if result != 1:
    exit(0)
op = Dispatch("op.opsoft")
op.SetDict(0, "./dic/shatan.txt")
op.UseDict(0)
print(op.Ver())
