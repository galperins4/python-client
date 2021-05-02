# Hedora - Python Client

## Installation
```git clone https://github.com/galperins4/hedora-python-client/```

```cd hedora-python-client```

```sudo python3 setup.py install```

## Usage (Example)

```
# import module
from client import Hedora Client

#initialize client
client = HedoraClient('https://testnet.mirrornode.hedera.com/api/v1')

acct_id = '0.0.575713'
accounts = client.mirror.accounts(acct_path=acct_id)
print(accounts)
```
