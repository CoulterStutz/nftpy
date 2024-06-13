class Order:
    def __init__(self, order_id, maker, taker, strategy, currency, amount, price, nonce, start_time, end_time, status, signature, intermediary=None, order_type=None, salt=None, extra_params=None):
        self.order_id = order_id
        self.maker = maker
        self.taker = taker
        self.strategy = strategy
        self.currency = currency
        self.amount = amount
        self.price = price
        self.nonce = nonce
        self.start_time = start_time
        self.end_time = end_time
        self.status = status
        self.signature = signature
        self.intermediary = intermediary
        self.order_type = order_type
        self.salt = salt
        self.extra_params = extra_params

    @classmethod
    def from_dict(cls, data):
        order_id = data.get('orderId')
        maker = data.get('maker')
        taker = data.get('taker')
        strategy = data.get('strategy')
        currency = data.get('currency')
        amount = data.get('amount')
        price = data.get('price')
        nonce = data.get('nonce')
        start_time = data.get('startTime')
        end_time = data.get('endTime')
        status = data.get('status')
        signature = data.get('signature')
        intermediary = data.get('intermediary')
        order_type = data.get('type')
        salt = data.get('salt')
        extra_params = data.get('extraParams')
        return cls(order_id, maker, taker, strategy, currency, amount, price, nonce, start_time, end_time, status, signature, intermediary, order_type, salt, extra_params)

    def __repr__(self):
        return (f"Order(order_id={self.order_id}, maker={self.maker}, taker={self.taker}, strategy={self.strategy}, "
                f"currency={self.currency}, amount={self.amount}, price={self.price}, nonce={self.nonce}, "
                f"start_time={self.start_time}, end_time={self.end_time}, status={self.status}, signature={self.signature}, "
                f"intermediary={self.intermediary}, order_type={self.order_type}, salt={self.salt}, extra_params={self.extra_params})")
