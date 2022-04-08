import requests

api_version = 'v1' 
base_url = "https://api.sandbox.gemini.com"

def post_new_order(request_headers, data = None):
    new_order_endpoint = f'/{api_version}/order/new'
    url = base_url + new_order_endpoint
    response = requests.post(url, data, headers=request_headers)
    return response

def post_cancel_order(request_headers, data = None):
    cancle_order_endpoint = f'/{api_version}/order/cancel'
    print(f'implementation for {cancle_order_endpoint} goes here')