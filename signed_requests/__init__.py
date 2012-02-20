import base64, hmac, hashlib
from requests.auth import AuthBase

def sign_string(s, key):
    return base64.b64encode(
        hmac.new(str(key),
        msg=s.lower(),
        digestmod=hashlib.sha1).digest())

class SignedAuth(AuthBase):
    def __init__(self, public_key, private_key):
        self.public_key = public_key
        self.private_key = private_key

    def __call__(self, r):
        r.params.append(('apikey', self.public_key)),
        r.params, r._enc_params = r._encode_params(r.params)
        r.params.append(('signature', sign_string(r.path_url, self.private_key)))
        r.params, r._enc_params = r._encode_params(r.params)
        
        return r
