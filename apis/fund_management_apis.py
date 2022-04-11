import requests

api_version = 'v1' 
base_url = "https://api.sandbox.gemini.com"

def post_balances(request_headers, data = None):
    balances_endpoint = f'/{api_version}/balances'
    url = base_url + balances_endpoint
    response = requests.post(url, data, headers=request_headers)
    return response
