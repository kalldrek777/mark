from .production import *
try:
    from .private_settings import *
except ImportError:
    pass
