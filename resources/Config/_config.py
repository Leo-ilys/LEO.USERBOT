# config values will be loaded from here

import os

ENV = bool(os.environ.get("ENV", False))

if ENV:
    from ._icsconfig import Config  # @QHR_1
else:
    if os.path.exists("config.py"):
        from config import Development as Config  # Hey there
