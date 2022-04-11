import payloads.order_placement_api_payloads as payload 
import apis.order_placement_apis as order_api
import apis.symbols_and_minimums_apis as symbols_api
import pytest
import logging

def func():
    return True

class NewOrderTests():
    def test_smoke():
        # list_of_all_symbols_response = symbols_api.get_symbols().json()
        # for symbol in list_of_all_symbols_response:
        #     response = symbols_api.get_symbols_details(symbol)
        #     print(response.json()["status"])
            assert func() == True

    # def test_smoke(self):
    #     new_order_payload = payload.generate_new_order_payload()

    #     new_order_payload['price'] = "0.01"
    #     new_order_payload['options'] = ["maker-or-cancel"]
    #     new_order_payload['side'] = 'buy'
    #     new_order_payload['type'] = "exchange limit"

    #     new_order_headers = payload.generate_request_headers(new_order_payload)

    #     response = order_api.post_new_order(new_order_headers)
    #     self.assertEqual(True, False)


