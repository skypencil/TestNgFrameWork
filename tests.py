import payloads.fund_management_api_payloads as fund_payload 
import payloads.order_placement_api_payloads as order_payload 
import apis.order_placement_apis as order_api
import apis.symbols_and_minimums_apis as symbols_api
import apis.fund_management_apis as funds_api
import pytest
import random
from pytest import fixture
import logging

def get_available_balances_per_asset():
    balance_payload = fund_payload.generate_balances_payload(0)
    balance_headers = fund_payload.generate_request_headers(balance_payload)
    response = funds_api.post_balances(balance_headers).json()
    result = {}
    for asset in response:
        logging.info(asset['currency'].lower(), ":", asset["amount"])
        result[asset["currency"].lower()] = asset["amount"]
    return result 

def get_all_coin_details():
    print('\n getting all coin details')
    list_of_all_symbols_response = symbols_api.get_symbols().json()
    coin_test_data = [] 
    for symbol in list_of_all_symbols_response:
        received_details = symbols_api.get_symbols_details(symbol).json()
        print('details recieved for:', received_details["symbol"])
        coin_test_data.append(received_details)
    return coin_test_data

# seems like a user can have one localization setting, for other currencies, separate tests need to be written
def get_open_status_coins(all_coins):
    result = []
    for coin in all_coins:
        if 'GBP' in coin['symbol']:
            continue
        if 'EUR' in coin['symbol']:
            continue
        if coin['status'] == 'open':
            result.append(coin)
    return result


@fixture(scope='session')
def coins_test_data_current():
    all_coins = get_all_coin_details();
    testData = {
        "openStatusCoins": get_open_status_coins(all_coins),
        "usersAvailableAssets" : get_available_balances_per_asset()
    }
    return testData

def test_can_only_buy_open_status_coins(coins_test_data_current):
    open_status_coins = coins_test_data_current["openStatusCoins"]
    available_funds = coins_test_data_current["usersAvailableAssets"]
    list_of_assets_available_to_user = available_funds.keys()
    random_available_coin = random.choice(list(list_of_assets_available_to_user))
    random_open_status_coin = ""
    valid_pair_not_found = True
    while valid_pair_not_found:
        random_choice = random.choice(open_status_coins)
        print(random_available_coin, random_choice["symbol"].lower())
        if random_available_coin in random_choice["symbol"].lower():
            random_open_status_coin = random_choice['symbol']
            valid_pair_not_found = False

    new_order_payload = order_payload.generate_new_order_payload(1) 
    new_order_payload['symbol'] = random_open_status_coin
    new_order_payload['price'] = "0.01"
    new_order_payload['options'] = ["maker-or-cancel"]
    new_order_payload['side'] = 'buy'
    new_order_payload['type'] = "exchange limit"
    new_order_headers = order_payload.generate_request_headers(new_order_payload)

    response = order_api.post_new_order(new_order_headers)
    print(response.json())
    assert response.status_code == 200 
    assert response.json()["is_cancelled"] == False
    assert response.json()["is_live"] == True
    assert response.json()["side"] == "buy"
    assert response.json()["side"] == "buy"
    assert "order_id" in response.json()
    assert "timestampms" in response.json()

def test_can_place_a_new_orders_with_client_order_id(coins_test_data_current):
    open_status_coins = coins_test_data_current["openStatusCoins"]
    available_funds = coins_test_data_current["usersAvailableAssets"]
    list_of_assets_available_to_user = available_funds.keys()
    random_available_coin = random.choice(list(list_of_assets_available_to_user))
    random_open_status_coin = ""
    valid_pair_not_found = True
    while valid_pair_not_found:
        random_choice = random.choice(open_status_coins)
        print(random_available_coin, random_choice["symbol"].lower())
        if random_available_coin in random_choice["symbol"].lower():
            random_open_status_coin = random_choice['symbol']
            valid_pair_not_found = False

    new_order_payload = order_payload.generate_new_order_payload(2) 
    new_order_payload['symbol'] = random_open_status_coin
    new_order_payload['client_order_id'] = f"{random.randrange(10)}_example"
    new_order_payload['price'] = "0.01"
    new_order_payload['options'] = ["maker-or-cancel"]
    new_order_payload['side'] = 'buy'
    new_order_payload['type'] = "exchange limit"
    new_order_headers = order_payload.generate_request_headers(new_order_payload)

    response = order_api.post_new_order(new_order_headers)
    print(response.json())
    assert response.status_code == 200 
    assert response.json()["is_cancelled"] == False
    assert response.json()["is_live"] == True
    assert response.json()["side"] == "buy"
    assert response.json()["side"] == "buy"
    assert "order_id" in response.json()
    assert "timestampms" in response.json()

def test_required_stop_price_for_stop_limit_orders(coins_test_data_current):
    open_status_coins = coins_test_data_current["openStatusCoins"]
    available_funds = coins_test_data_current["usersAvailableAssets"]
    open_status_coins = open_status_coins
    list_of_assets_available_to_user = available_funds.keys()
    random_available_coin = random.choice(list(list_of_assets_available_to_user))
    random_open_status_coin = ""
    valid_pair_not_found = True
    while valid_pair_not_found:
        random_choice = random.choice(open_status_coins)
        print(random_available_coin, random_choice["symbol"].lower())
        if random_available_coin in random_choice["symbol"].lower():
            random_open_status_coin = random_choice['symbol']
            valid_pair_not_found = False

    new_order_payload = order_payload.generate_new_order_payload(2) 
    new_order_payload['symbol'] = random_open_status_coin
    new_order_payload['price'] = "0.01"
    new_order_payload['side'] = 'buy'
    new_order_payload['options'] = []
    new_order_payload['type'] = "exchange stop limit"
    new_order_headers = order_payload.generate_request_headers(new_order_payload)

    response = order_api.post_new_order(new_order_headers)
    print(response.json())
    assert response.status_code == 400 
    assert response.json()["result"] == 'error' 
    assert response.json()["reason"] == 'MissingStopPrice'

def test_required_stop_price_for_stop_limit_orders(coins_test_data_current):
    available_funds = coins_test_data_current["usersAvailableAssets"]
    list_of_assets_available_to_user = list(available_funds.keys())
    
    # to avoid 'usdusd' coin pairing below
    list_of_assets_available_to_user.remove('usd')
    random_available_coin = random.choice(list_of_assets_available_to_user)

    new_order_payload = order_payload.generate_new_order_payload(3) 
    new_order_payload['symbol'] = f"{random_available_coin}usd"
    new_order_payload['price'] = "0.01"
    new_order_payload['options'] = ["maker-or-cancel"]
    new_order_payload['side'] = 'sell'
    new_order_payload['type'] = "exchange limit"
    new_order_headers = order_payload.generate_request_headers(new_order_payload)

    response = order_api.post_new_order(new_order_headers)
    print(response.json())
    assert response.status_code == 200 
    assert response.json()["side"] == "sell"
    assert "order_id" in response.json()
    assert "timestampms" in response.json()


def test_cannot_place_sell_orders_with_unavailable_asset():
    new_order_payload = order_payload.generate_new_order_payload(4) 
    new_order_payload['symbol'] = "audiogbp"
    new_order_payload['price'] = "0.01"
    new_order_payload['options'] = ["maker-or-cancel"]
    new_order_payload['side'] = 'sell'
    new_order_payload['type'] = "exchange limit"
    new_order_headers = order_payload.generate_request_headers(new_order_payload)

    response = order_api.post_new_order(new_order_headers)
    print(response.json())
    assert response.status_code == 403 
    assert response.json()["result"] == "error"
    assert "AUDIOGBP" in response.json()["message"] 

def test_invalid_request_string_throws_error():
    new_order_payload = order_payload.generate_new_order_payload(5) 
    new_order_payload["request"] = "/invalid/path/new",
    new_order_payload['symbol'] = "audiogbp"
    new_order_payload['price'] = "0.01"
    new_order_payload['options'] = ["maker-or-cancel"]
    new_order_payload['side'] = 'sell'
    new_order_payload['type'] = "exchange limit"
    new_order_headers = order_payload.generate_request_headers(new_order_payload)

    response = order_api.post_new_order(new_order_headers)
    print(response.json())
    assert response.status_code == 400 
    assert response.json()["result"] == "error"
    assert response.json()["reason"] == "EndpointMismatch"

@pytest.mark.skip(reason="Based on the documentation only for a USD account holder trading in GBP should cause an error, however, the following pair btcgp doesnt")
def test_USD_user_gets_restricted_error_while_selling_with_GBP():
    new_order_payload = order_payload.generate_new_order_payload(6) 
    new_order_payload['symbol'] = "btcgbp"
    new_order_payload['price'] = "0.01"
    new_order_payload['options'] = ["maker-or-cancel"]
    new_order_payload['side'] = 'sell'
    new_order_payload['type'] = "exchange limit"
    new_order_headers = order_payload.generate_request_headers(new_order_payload)

    response = order_api.post_new_order(new_order_headers)
    print(response.json())
    assert response.status_code == 403 
    assert response.json()["result"] == "error"
    assert "AUDIOGBP" in response.json()["message"] 


