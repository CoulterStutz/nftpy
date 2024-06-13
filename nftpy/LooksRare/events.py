class Event:
    def __init__(self, id, from_address, to_address, event_type, hash, created_at, collection, token, order):
        self.id = id
        self.from_address = from_address
        self.to_address = to_address
        self.event_type = event_type
        self.hash = hash
        self.created_at = created_at
        self.collection = collection
        self.token = token
        self.order = order

    @classmethod
    def from_dict(cls, data):
        id = data.get('id')
        from_address = data.get('from')
        to_address = data.get('to')
        event_type = data.get('type')
        hash = data.get('hash')
        created_at = data.get('createdAt')
        collection = data.get('collection')
        token = data.get('token')
        order = data.get('order')
        return cls(id, from_address, to_address, event_type, hash, created_at, collection, token, order)

    def __repr__(self):
        return (f"Event(id={self.id}, from_address={self.from_address}, to_address={self.to_address}, event_type={self.event_type}, "
                f"hash={self.hash}, created_at={self.created_at}, collection={self.collection}, token={self.token}, order={self.order})")
