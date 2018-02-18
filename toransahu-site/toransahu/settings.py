import socket


if socket.gethostname() == "mint-ThinkPad-L440":
    from .dev_settings import *
else:
    from .prod_settings import *