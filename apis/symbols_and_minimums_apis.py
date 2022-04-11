import requests

api_version = 'v1' 
base_url = "https://api.sandbox.gemini.com"

def get_symbols():
    symbols_endpoint = f'/{api_version}/symbols'
    url = base_url + symbols_endpoint
    response = requests.get(url)
    return response

def get_symbols_details(symbol):
    symbols_details_endpoint = f'/{api_version}/symbols/details/{symbol}'
    url = base_url + symbols_details_endpoint;
    response = requests.get(url)
    return response

