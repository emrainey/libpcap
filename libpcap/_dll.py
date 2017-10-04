# Copyright (c) 2016-2017, Adam Karpierz
# Licensed under the BSD license
# https://opensource.org/licenses/BSD-3-Clause

from ._platform import DLL_PATH, DLL, dlclose

try:
    dll = DLL(DLL_PATH)
except OSError as exc:
    raise exc
except Exception as exc:
    raise OSError("{}".format(exc))
