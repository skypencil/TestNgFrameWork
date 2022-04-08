import payloads.order_placement_api_payloads as payload 
import apis.order_placement_apis as order_api
import unittest
import logging


class NewOrder(unittest.TestCase):
    def test_smoke(self):
        new_order_payload = payload.generate_new_order_payload()

        new_order_payload['price'] = "0.01"
        new_order_payload['options'] = ["maker-or-cancel"]
        new_order_payload['side'] = 'buy'
        new_order_payload['type'] = "exchange limit"

        new_order_headers = payload.generate_request_headers(new_order_payload)

        response = order_api.post_new_order(new_order_headers)
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
