## Installation
```bash
    pip install -r requirements.txt 
```

## Run tests
```bash
    pytest tests.py -s
```

Limitations:
1. coin-pairings requires a more robust test data. I couldn't find single coin lists anywhere in the documentation where could normalize the available coin pairs. Right now the test cases may give false negatives for 3% of "buy" scenarios.
2. This endpoint is a mature endpoint with a lot of complex logic. It requires all of the following test cases, only few of which I could finish in a reasonable amount of time. The rest of the scenarios I have outlined as tests to be covered.
3. Each coin pairing has different trading status e.g. `open`, `closed`, `cancel_only`, `post_only`, and `limit_only` which appears to be changing regularly. To be able to test against these changing variables I have decided to run my test cases against an updated data set each time. Which is generated for all valid coin pairs through api calls. Which makes the test cases very time consuming. 

Tests covered:
1. user can place a buy order if they have the funds available
2. user can place a sell order if they already have the asset available
3. user cannot place a sell order on an asset they don't own
4. every request should have an increased new nonce
5. all optional and and conditional fields are accepted as a request payload
6. missing required fields throw an error
7. invalid  request string should give endpointmismatch error

Tests to be covered:
1. testing a complete list of required and non required fields
2. invalid nonce
3. invalid request string
4. test cases for `close`,`cancel_only`, `post_only`, `limit_only` coin statuses
5. different order execution option permutations

Questions:

1. while putting an order for selling `btcgbp` for a us based `usd` account the expected response was as follows:

```json
{'result': 'error', 'reason': 'RestrictedSymbol', 'message': 'Your account is not permitted to trade this symbol, BTCGBP'}
```

but I received the following:

```json
{'order_id': '1712382732', 'id': '1712382732', 'symbol': 'btcgbp', 'exchange': 'gemini', 'avg_execution_price': '0.00', 'side': 'sell', 'type': 'exchange limit', 'timestamp': '1649716696', 'timestampms': 1649716696022, 'is_live': False, 'is_cancelled': True, 'is_hidden': False, 'was_forced': False, 'executed_amount': '0', 'reason': 'MakerOrCancelWouldTake', 'options': ['maker-or-cancel'], 'price': '0.01', 'original_amount': '33', 'remaining_amount': '33'}
```
