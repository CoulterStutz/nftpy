class Attribute:
    def __init__(self, trait_type, value, display_type=None, count=None, floor_order=None):
        self.trait_type = trait_type
        self.value = value
        self.display_type = display_type
        self.count = count
        self.floor_order = floor_order

    @classmethod
    def from_dict(cls, data):
        trait_type = data.get('traitType')
        value = data.get('value')
        display_type = data.get('displayType')
        count = data.get('count')
        floor_order = data.get('floorOrder')
        return cls(trait_type, value, display_type, count, floor_order)

    def __repr__(self):
        return (f"Attribute(trait_type={self.trait_type}, value={self.value}, display_type={self.display_type}, "
                f"count={self.count}, floor_order={self.floor_order})")


class Token:
    def __init__(self, id, collection_address, token_id, token_uri, image_uri, is_explicit, is_animated, flag, name,
                 description, collection, attributes):
        self.id = id
        self.collection_address = collection_address
        self.token_id = token_id
        self.token_uri = token_uri
        self.image_uri = image_uri
        self.is_explicit = is_explicit
        self.is_animated = is_animated
        self.flag = flag
        self.name = name
        self.description = description
        self.collection = collection
        self.attributes = attributes

    @classmethod
    def from_dict(cls, data):
        id = data.get('id')
        collection_address = data.get('collectionAddress')
        token_id = data.get('tokenId')
        token_uri = data.get('tokenURI')
        image_uri = data.get('imageURI')
        is_explicit = data.get('isExplicit')
        is_animated = data.get('isAnimated')
        flag = data.get('flag')
        name = data.get('name')
        description = data.get('description')
        collection = data.get('collection')
        attributes = [Attribute.from_dict(attr) for attr in data.get('attributes', [])]
        return cls(id, collection_address, token_id, token_uri, image_uri, is_explicit, is_animated, flag, name, description, collection, attributes)

    def __repr__(self):
        return (f"Token(id={self.id}, collection_address={self.collection_address}, token_id={self.token_id}, token_uri={self.token_uri}, "
                f"image_uri={self.image_uri}, is_explicit={self.is_explicit}, is_animated={self.is_animated}, flag={self.flag}, "
                f"name={self.name}, description={self.description}, collection={self.collection}, attributes={self.attributes})")
