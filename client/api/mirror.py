from client.resource import Resource


class Mirror(Resource):

    def accounts(self):
        pass
    
    
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

    def transactions(self, block_id, page=None, limit=100):
        params = {
            'page': page,
            'limit': limit,
        }
        return self.request_get('blocks/{}/transactions'.format(block_id), params)
