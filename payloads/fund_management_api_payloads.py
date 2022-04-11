import util.util as util
import random
import json
import base64
import hmac
import hashlib

#  for the purposes of this demo I have hard coded the following values
#  ideally these values should be populated from environment variables.
#  that way it makes it easier to point test cases to different environments and user roles
# gemini_api_key = "account-aYYgogztC7Q8N3k4qL7p", 
# gemini_api_secret = "3HNMPw49xpMHpuURyCBK522VZGoM"

api_version = 'v1' 
gemini_api_key="account-zne4QraHWlhDKRE5S0H5"
gemini_api_secret="29RaGpF1BNz1C21Qp3sM9L9jZniE".encode()


def generate_balances_payload():
     payload = {
         "request": f"/{api_version}/balances",
         "nonce": util.generateNonce(),
     }
     return payload
    
def generate_request_headers(payload):
     encoded_payload = json.dumps(payload).encode()
     b64 = base64.b64encode(encoded_payload)
     signature = hmac.new(gemini_api_secret, b64, hashlib.sha384).hexdigest()
     request_headers = {
         'Content-Type': "text/plain",
         'Content-Length': "0",
         'X-GEMINI-APIKEY': gemini_api_key,
         'X-GEMINI-PAYLOAD': b64,
         'X-GEMINI-SIGNATURE': signature,
         'Cache-Control': "no-cache"
     }
     return request_headers