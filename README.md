# Hedera - Python Client

## Installation
```git clone https://github.com/galperins4/hedera-python-client/```

```cd hedera-python-client```

```sudo python3 setup.py install```

## Usage (Example)

```
# import module
from client import Hedera Client

# initialize client
client = HederaClient('https://testnet.mirrornode.hedera.com/api/v1')

acct_id = '0.0.575713'
accounts = client.mirror.accounts(acct_path=acct_id)
print(accounts)
```

Refer to [Mirror Node API](https://docs.hedera.com/guides/docs/mirror-node-api/cryptocurrency-api) for REST API documentation
