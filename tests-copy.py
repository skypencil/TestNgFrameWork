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
    balance_payload = fund_payload.generate_balances_payload()
    balance_headers = fund_payload.generate_request_headers(balance_payload)
    response = funds_api.post_balances(balance_headers).json()
    result = {}
    for asset in response:
        result[asset["currency"].lower()] = asset["amount"]
    return result 

def get_all_coin_details():
    list_of_all_symbols_response = symbols_api.get_symbols().json()
    coin_test_data = [] 
    for symbol in list_of_all_symbols_response:
        received_details = symbols_api.get_symbols_details(symbol).json()
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
        if coin['status'] == 'open' and coin['']:
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

openstatus = [{'symbol': 'BTCUSD', 'base_currency': 'BTC', 'quote_currency': 'USD', 'tick_size': 1e-08, 'quote_increment': 0.01, 'min_order_size': '0.00001', 'status': 'open', 'wrap_enabled': False}, {'symbol': 'BTCGUSD', 'base_currency': 'BTC', 'quote_currency': 'GUSD', 'tick_size': 1e-08, 'quote_increment': 0.01, 'min_order_size': '0.00001', 'status': 'open', 'wrap_enabled': False}, {'symbol': 'BTCGBP', 'base_currency': 'BTC', 'quote_currency': 'GBP', 'tick_size': 1e-08, 'quote_increment': 0.01, 'min_order_size': '0.00001', 'status': 'open', 'wrap_enabled': False}, {'symbol': 'BTCEUR', 'base_currency': 'BTC', 'quote_currency': 'EUR', 'tick_size': 1e-08, 'quote_increment': 0.01, 'min_order_size': '0.00001', 'status': 'open', 'wrap_enabled': False}, {'symbol': 'BTCSGD', 'base_currency': 'BTC', 'quote_currency': 'SGD', 'tick_size': 1e-08, 'quote_increment': 0.01, 'min_order_size': '0.00001', 'status': 'open', 'wrap_enabled': False}, {'symbol': 'ETHUSD', 'base_currency': 'ETH', 'quote_currency': 'USD', 'tick_size': 1e-06, 'quote_increment': 0.01, 'min_order_size': '0.001', 'status': 'open', 'wrap_enabled': False}, {'symbol': 'ETHGUSD', 'base_currency': 'ETH', 'quote_currency': 'GUSD', 'tick_size': 1e-06, 'quote_increment': 0.01, 'min_order_size': '0.001', 'status': 'open', 'wrap_enabled': False}, {'symbol': 'ETHGBP', 'base_currency': 'ETH', 'quote_currency': 'GBP', 'tick_size': 1e-06, 'quote_increment': 0.01, 'min_order_size': '0.001', 'status': 'open', 'wrap_enabled': False}, {'symbol': 'ETHEUR', 'base_currency': 'ETH', 'quote_currency': 'EUR', 'tick_size': 1e-06, 'quote_increment': 0.01, 'min_order_size': '0.001', 'status': 'open', 'wrap_enabled': False}, {'symbol': 'ETHSGD', 'base_currency': 'ETH', 'quote_currency': 'SGD', 'tick_size': 1e-06, 'quote_increment': 0.01, 'min_order_size': '0.001', 'status': 'open', 'wrap_enabled': False}, {'symbol': 'BCHUSD', 'base_currency': 'BCH', 'quote_currency': 'USD', 'tick_size': 1e-06, 'quote_increment': 0.01, 'min_order_size': '0.001', 'status': 'open', 'wrap_enabled': False}, {'symbol': 'BCHBTC', 'base_currency': 'BCH', 'quote_currency': 'BTC', 'tick_size': 1e-06, 'quote_increment': 1e-05, 'min_order_size': '0.001', 'status': 'open', 'wrap_enabled': False}, {'symbol': 'BCHETH', 'base_currency': 'BCH', 'quote_currency': 'ETH', 'tick_size': 1e-06, 'quote_increment': 0.0001, 'min_order_size': '0.001', 'status': 'open', 'wrap_enabled': False}, {'symbol': 'LTCUSD', 'base_currency': 'LTC', 'quote_currency': 'USD', 'tick_size': 1e-05, 'quote_increment': 0.01, 'min_order_size': '0.01', 'status': 'open', 'wrap_enabled': False}, {'symbol': 'LTCETH', 'base_currency': 'LTC', 'quote_currency': 'ETH', 'tick_size': 1e-05, 'quote_increment': 0.0001, 'min_order_size': '0.01', 'status': 'open', 'wrap_enabled': False}, {'symbol': 'LTCBCH', 'base_currency': 'LTC', 'quote_currency': 'BCH', 'tick_size': 1e-05, 'quote_increment': 0.0001, 'min_order_size': '0.01', 'status': 'open', 'wrap_enabled': False}, {'symbol': 'ZECUSD', 'base_currency': 'ZEC', 'quote_currency': 'USD', 'tick_size': 1e-06, 'quote_increment': 0.01, 'min_order_size': '0.001', 'status': 'open', 'wrap_enabled': False}, {'symbol': 'ZECBCH', 'base_currency': 'ZEC', 'quote_currency': 'BCH', 'tick_size': 1e-06, 'quote_increment': 0.0001, 'min_order_size': '0.001', 'status': 'open', 'wrap_enabled': False}, {'symbol': 'ZECLTC', 'base_currency': 'ZEC', 'quote_currency': 'LTC', 'tick_size': 1e-06, 'quote_increment': 0.001, 'min_order_size': '0.001', 'status': 'open', 'wrap_enabled': False}, {'symbol': 'BATUSD', 'base_currency': 'BAT', 'quote_currency': 'USD', 'tick_size': 1e-06, 'quote_increment': 0.01, 'min_order_size': '1', 'status': 'open', 'wrap_enabled': False}, {'symbol': 'BATBTC', 'base_currency': 'BAT', 'quote_currency': 'BTC', 'tick_size': 1e-06, 'quote_increment': 1e-05, 'min_order_size': '1', 'status': 'open', 'wrap_enabled': False}, {'symbol': 'BATETH', 'base_currency': 'BAT', 'quote_currency': 'ETH', 'tick_size': 1e-06, 'quote_increment': 0.0001, 'min_order_size': '0.001', 'status': 'open', 'wrap_enabled': False}, {'symbol': 'LINKUSD', 'base_currency': 'LINK', 'quote_currency': 'USD', 'tick_size': 1e-06, 'quote_increment': 0.01, 'min_order_size': '0.1', 'status': 'open', 'wrap_enabled': False}, {'symbol': 'LINKBTC', 'base_currency': 'LINK', 'quote_currency': 'BTC', 'tick_size': 1e-06, 'quote_increment': 1e-05, 'min_order_size': '0.1', 'status': 'open', 'wrap_enabled': False}, {'symbol': 'LINKETH', 'base_currency': 'LINK', 'quote_currency': 'ETH', 'tick_size': 1e-06, 'quote_increment': 0.0001, 'min_order_size': '0.1', 'status': 'open', 'wrap_enabled': False}, {'symbol': 'DAIUSD', 'base_currency': 'DAI', 'quote_currency': 'USD', 'tick_size': 1e-06, 'quote_increment': 0.01, 'min_order_size': '0.1', 'status': 'open', 'wrap_enabled': False}, {'symbol': 'OXTUSD', 'base_currency': 'OXT', 'quote_currency': 'USD', 'tick_size': 1e-06, 'quote_increment': 0.01, 'min_order_size': '1', 'status': 'open', 'wrap_enabled': False}, {'symbol': 'OXTBTC', 'base_currency': 'OXT', 'quote_currency': 'BTC', 'tick_size': 1e-06, 'quote_increment': 1e-05, 'min_order_size': '1', 'status': 'open', 'wrap_enabled': False}, {'symbol': 'OXTETH', 'base_currency': 'OXT', 'quote_currency': 'ETH', 'tick_size': 1e-06, 'quote_increment': 0.0001, 'min_order_size': '1', 'status': 'open', 'wrap_enabled': False}, {'symbol': 'AMPUSD', 'base_currency': 'AMP', 'quote_currency': 'USD', 'tick_size': 1e-06, 'quote_increment': 1e-05, 'min_order_size': '10', 'status': 'open', 'wrap_enabled': False}, {'symbol': 'COMPUSD', 'base_currency': 'COMP', 'quote_currency': 'USD', 'tick_size': 1e-06, 'quote_increment': 0.01, 'min_order_size': '0.001', 'status': 'open', 'wrap_enabled': False}, {'symbol': 'MKRUSD', 'base_currency': 'MKR', 'quote_currency': 'USD', 'tick_size': 1e-06, 'quote_increment': 0.01, 'min_order_size': '0.001', 'status': 'open', 'wrap_enabled': False}, {'symbol': 'KNCUSD', 'base_currency': 'KNC', 'quote_currency': 'USD', 'tick_size': 1e-06, 'quote_increment': 1e-05, 'min_order_size': '0.1', 'status': 'open', 'wrap_enabled': False}, {'symbol': 'AAVEUSD', 'base_currency': 'AAVE', 'quote_currency': 'USD', 'tick_size': 1e-06, 'quote_increment': 0.0001, 'min_order_size': '0.001', 'status': 'open', 'wrap_enabled': False}, {'symbol': 'SNXUSD', 'base_currency': 'SNX', 'quote_currency': 'USD', 'tick_size': 1e-06, 'quote_increment': 0.0001, 'min_order_size': '0.01', 'status': 'open', 'wrap_enabled': False}, {'symbol': 'YFIUSD', 'base_currency': 'YFI', 'quote_currency': 'USD', 'tick_size': 1e-06, 'quote_increment': 0.01, 'min_order_size': '0.00001', 'status': 'open', 'wrap_enabled': False}, {'symbol': 'UNIUSD', 'base_currency': 'UNI', 'quote_currency': 'USD', 'tick_size': 1e-06, 'quote_increment': 0.0001, 'min_order_size': '0.01', 'status': 'open', 'wrap_enabled': False}, {'symbol': 'SUSHIUSD', 'base_currency': 'SUSHI', 'quote_currency': 'USD', 'tick_size': 1e-06, 'quote_increment': 1e-06, 'min_order_size': '0.01', 'status': 'open', 'wrap_enabled': False}, {'symbol': 'API3USD', 'base_currency': 'API3', 'quote_currency': 'USD', 'tick_size': 1e-06, 'quote_increment': 0.0001, 'min_order_size': '0.002', 'status': 'open', 'wrap_enabled': False}, {'symbol': 'XTZUSD', 'base_currency': 'XTZ', 'quote_currency': 'USD', 'tick_size': 1e-06, 'quote_increment': 0.0001, 'min_order_size': '0.02', 'status': 'open', 'wrap_enabled': False}, {'symbol': 'USDCUSD', 'base_currency': 'USDC', 'quote_currency': 'USD', 'tick_size': 1e-06, 'quote_increment': 0.001, 'min_order_size': '0.1', 'status': 'open', 'wrap_enabled': False}, {'symbol': 'SLPUSD', 'base_currency': 'SLP', 'quote_currency': 'USD', 'tick_size': 1e-06, 'quote_increment': 1e-05, 'min_order_size': '0.5', 'status': 'open', 'wrap_enabled': False}, {'symbol': 'USTUSD', 'base_currency': 'UST', 'quote_currency': 'USD', 'tick_size': 1e-06, 'quote_increment': 0.001, 'min_order_size': '0.1', 'status': 'open', 'wrap_enabled': False}, {'symbol': 'DOGEBTC', 'base_currency': 'DOGE', 'quote_currency': 'BTC', 'tick_size': 1e-08, 'quote_increment': 1e-08, 'min_order_size': '1', 'status': 'open', 'wrap_enabled': False}, {'symbol': 'DOGEETH', 'base_currency': 'DOGE', 'quote_currency': 'ETH', 'tick_size': 1e-08, 'quote_increment': 1e-06, 'min_order_size': '1', 'status': 'open', 'wrap_enabled': False}, {'symbol': 'WCFGUSD', 'base_currency': 'WCFG', 'quote_currency': 'USD', 'tick_size': 1e-06, 'quote_increment': 0.001, 'min_order_size': '0.05', 'status': 'open', 'wrap_enabled': False}, {'symbol': 'RADUSD', 'base_currency': 'RAD', 'quote_currency': 'USD', 'tick_size': 1e-06, 'quote_increment': 0.001, 'min_order_size': '0.01', 'status': 'open', 'wrap_enabled': False}, {'symbol': 'QNTUSD', 'base_currency': 'QNT', 'quote_currency': 'USD', 'tick_size': 1e-06, 'quote_increment': 0.01, 'min_order_size': '0.0004', 'status': 'open', 'wrap_enabled': False}, {'symbol': 'MASKUSD', 'base_currency': 'MASK', 'quote_currency': 'USD', 'tick_size': 1e-06, 'quote_increment': 0.001, 'min_order_size': '0.01', 'status': 'open', 'wrap_enabled': False}, {'symbol': 'FETUSD', 'base_currency': 'FET', 'quote_currency': 'USD', 'tick_size': 1e-06, 'quote_increment': 1e-05, 'min_order_size': '0.1', 'status': 'open', 'wrap_enabled': False}, {'symbol': 'AUDIOUSD', 'base_currency': 'AUDIO', 'quote_currency': 'USD', 'tick_size': 1e-06, 'quote_increment': 0.001, 'min_order_size': '0.05', 'status': 'open', 'wrap_enabled': False}, {'symbol': 'NMRUSD', 'base_currency': 'NMR', 'quote_currency': 'USD', 'tick_size': 1e-06, 'quote_increment': 0.001, 'min_order_size': '0.003', 'status': 'open', 'wrap_enabled': False}, {'symbol': 'RLYUSD', 'base_currency': 'RLY', 'quote_currency': 'USD', 'tick_size': 1e-06, 'quote_increment': 1e-05, 'min_order_size': '0.2', 'status': 'open', 'wrap_enabled': False}, {'symbol': 'SHIBUSD', 'base_currency': 'SHIB', 'quote_currency': 'USD', 'tick_size': 1e-06, 'quote_increment': 1e-09, 'min_order_size': '1000', 'status': 'open', 'wrap_enabled': False}, {'symbol': 'LDOUSD', 'base_currency': 'LDO', 'quote_currency': 'USD', 'tick_size': 1e-06, 'quote_increment': 0.001, 'min_order_size': '0.02', 'status': 'open', 'wrap_enabled': False}, {'symbol': 'TOKEUSD', 'base_currency': 'TOKE', 'quote_currency': 'USD', 'tick_size': 1e-06, 'quote_increment': 0.001, 'min_order_size': '0.002', 'status': 'open', 'wrap_enabled': False}]
available_funds = {'zec': '20000', 'eth': '20000', 'ltc': '20000', 'usd': '100000.00', 'bch': '20000', 'btc': '1000'}
# def test_can_only_buy_open_status_coins(coins_test_data_current):
def test_can_only_place_buy_orders_with_open_status_coins_and_available_funds():
    # open_status_coins = coins_test_data_current["openStatusCoins"]
    # users_available_assets = coins_test_data_current["usersAvailableAssets"]
    open_status_coins = openstatus
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

    new_order_payload = order_payload.generate_new_order_payload() 
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
    

# def test_can_only_buy_open_status_coins(coins_test_data_current):
def test_can_only_place_sell_orders_with_available_funds():
    # open_status_coins = coins_test_data_current["openStatusCoins"]
    # users_available_assets = coins_test_data_current["usersAvailableAssets"]
    list_of_assets_available_to_user = list(available_funds.keys())
    # to avoid 'usdusd' coin pairing below
    list_of_assets_available_to_user.remove('usd')
    random_available_coin = random.choice(list_of_assets_available_to_user)

    new_order_payload = order_payload.generate_new_order_payload(2) 
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



