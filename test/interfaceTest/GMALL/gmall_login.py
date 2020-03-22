import requests
from gmall_header import get_header_h5

host, header = get_header_h5()


class login():
    def old_password(self):
        url_01 = host + "/api/auth/check-old-password"




