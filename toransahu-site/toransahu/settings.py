import socket


if socket.gethostname() == "mint-ThinkPad-L440":
    from .dev_settings import *
elif socket.gethostname() == "PUNHJW364576D":
    from .dev_settings import *
else:
    from .prod_settings import *