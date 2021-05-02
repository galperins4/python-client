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
    
    
    def topic_messages(self, topic_id, sequence_number=sequence_number, consensus_timestamp = consensus_timestamp):
        params = {
            'sequenceNumber': sequence_number,  
            'consensusTimestamp': consensus_timestamp,
        }
        return self.request_get('topics/{}/messages'.format(topic_id), params)

    
    def tokens(self, token_path=token_path, pubkey=pubkey, token_id=token_id, acct_id=acct_id):
        params = {
            'publickey': pubkey,
            'token.id': token_id,
            'account.id': acct_id,
        }
        if token_path == None:
            return self.request_get('tokens', params)
        else:
            return self.request_get('tokens/{}'.format(token_path), params)
    
    
    def token_balances(self, token_id, acct_pubkey=None, acct_id=None, acct_balance=None, timestamp=None):
        params = {
            'account.publickey': acct_pubkey,  
            'account.id': acct_id,
            'account.balance': acct_balance,  
            'timestamp': timestamp,
        }
        return self.request_get('tokens/{}'.format(token_id))
    
    def token_info(self, token_id):
        return self.request_get('tokens/{}/balances'.format(token_id), params)
    
    
    def schedule_list(self, schedule_id=schedule_id, acct_id=acct_id, executed=executed, limit=limit):
        params = {
            'schedule.id': schedule_id,  
            'account.id': acct_id,
            'executed': executed,  
            'limit': limit,
        }
        return self.request_get('schedules', params)
      
    
    def schedule_transaction(self, schedule_id):
        return self.request_get('schedules/{}'.format(schedule_id))
    
    
    def transaction_state_proof(self, tx_id):
        return self.request_get('transactions/{}/stateproof'.format(tx_id))
