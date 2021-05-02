from client.resource import Resource


class Mirror(Resource):

  
    def accounts(self, acct_path=None, transaction_type=None, acct_id=None, acct_balance=None, acct_pubkey=None):
        params = {
            'transactionType': transaction_type,
            'account.id': acct_id,
            'account.balance': acct_balance,
            'account.publickey': acct_pubkey
        }
        if acct_path == None:
            return self.request_get('accounts', params)
        else:
            return self.request_get('accounts/{}'.format(acct_path), params)
    
    
    def balances(self):
        pass
    
    
    def transactions(self):
        pass
    
    
    def topic_messages(self):
        pass
    
    
    def token_balances(self):
        pass
    
    
    def token_info(self):
        pass
    
    
    def schedule_list(self):
        pass
    
    
    def schedule_transaction(self):
        pass
    
    
    def transaction_state_proof(self):
        pass
    
    
    def get(self, block_id):
        return self.request_get('blocks/{}'.format(block_id))

    def first(self):
        return self.request_get('blocks/first')

    def last(self):
        return self.request_get('blocks/last')

 
