from client.resource import Resource


class Mirror(Resource):

  
    def accounts(self, acct_path=None, tx_type=None, acct_id=None, acct_balance=None, acct_pubkey=None):
        params = {
            'transactionType': tx_type,
            'account.id': acct_id,
            'account.balance': acct_balance,
            'account.publickey': acct_pubkey
        }
        if acct_path == None:
            return self.request_get('accounts', params)
        else:
            return self.request_get('accounts/{}'.format(acct_path), params)
    
    
    def balances(self, acct_id=None, acct_balance=None, timestamp=None, acct_pubkey=None):
        params = {
            'account.id': acct_id,
            'account.balance': acct_balance,
            'timestamp': timestamp,
            'account.publickey': acct_pubkey
        }
        return self.request_get('balances', params)
    
    def transactions(self, tx_type=None, acct_id=None, timestamp=None, result=None, htype=None):
        params = {
            'transactionType': tx_type,  
            'account.id': acct_id,
            'timestamp': timestamp,
            'result': result,
            'type': htype
        }
        return self.request_get('transactions', params)
    
    def topic_messages(self):
        pass
    
    
    def token_balances(self, token_id=token_id, acct_pubkey=None, acct_id=None, acct_balance=None, timestamp=None):
        params = {
            'account.publickey': acct_pubkey,  
            'account.id': acct_id,
            'account.balance': acct_balance,  
            'timestamp': timestamp,
        }
        return self.request_get('tokens/{}'.format(token_id))
    
    def token_info(self, token_id=token_id):
        return self.request_get('tokens/{}/balances'.format(token_id), params)
    
    def schedule_list(self):
        pass
    
    
    def schedule_transaction(self, schedule_id=schedule_id):
        return self.request_get('schedules/{}'.format(schedule_id))
    
    
    def transaction_state_proof(self):
        pass
    
    
    def get(self, block_id):
        return self.request_get('blocks/{}'.format(block_id))

    def first(self):
        return self.request_get('blocks/first')

    def last(self):
        return self.request_get('blocks/last')

 
