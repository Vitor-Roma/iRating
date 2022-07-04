from django_elasticsearch_dsl import Document, fields, Index
from django_elasticsearch_dsl.registries import registry
from .models import Profile, Product, Restaurant, Rating, Wishlist


@registry.register_document
class RestaurantDocument(Document):
    # restaurant_product = fields.NestedField(properties={
    #     'name': fields.TextField(),
    #     'detail': fields.TextField(),
    #     'price': fields.TextField(),
    # })

    class Index:
        name = 'restaurant'
        setting = {
            'number_of_shards': 1,
            'number_of_replicas': 1,
            'size': 1000
        }

    class Django:
        model = Restaurant

        fields = ['id', 'name']

        # related_models = [Product]

    # def get_instances_from_related(self, related_instance):
    #     if isinstance(related_instance, Product):
    #         return related_instance.restaurant.all()


@registry.register_document
class ProductDocument(Document):

    # wishlist_product = fields.NestedField(properties={'note': fields.TextField()})
    # rating_product = fields.NestedField(properties={
    #     'product_rate': fields.IntegerField(),
    #     'size': fields.IntegerField(),
    #     'complement': fields.IntegerField(),
    #     'side_dish': fields.IntegerField(),
    #     'comment': fields.TextField(),
    # })
    # restaurant_product = fields.ObjectField(properties={
    #     'name': fields.TextField(),
    #     'detail': fields.TextField(),
    #     'price': fields.TextField(),
    # })

    class Index:
        name = 'product'
        setting = {
            'number_of_shards': 1,
            'number_of_replicas': 1,
            'size': 1000
        }

    class Django:
        model = Product

        fields = ['id', 'name', 'detail', 'price']

        # related_models = [Restaurant]

    # def get_instances_from_related(self, related_instance):
    #     if isinstance(related_instance, Product):
    #         return related_instance.restaurant.all()


@registry.register_document
class ProfileDocument(Document):
    # wishlist_profile = fields.NestedField(properties={'note': fields.TextField()})
    # rating_profile = fields.NestedField(properties={
    #     'product_rate': fields.IntegerField(),
    #     'size': fields.IntegerField(),
    #     'complement': fields.IntegerField(),
    #     'side_dish': fields.IntegerField(),
    #     'comment': fields.TextField(),
    # })

    class Index:
        name = 'profile'
        setting = {
            'number_of_shards': 1,
            'number_of_replicas': 1,
            'size': 1000
        }

    class Django:
        model = Profile

        fields = ['id', 'username']

        # related_models = [Wishlist, Rating]


@registry.register_document
class RatingDocument(Document):

    # rating_product = fields.ObjectField(properties={
    #     'product_rate': fields.IntegerField(),
    #     'size': fields.IntegerField(),
    #     'complement': fields.IntegerField(),
    #     'side_dish': fields.IntegerField(),
    #     'comment': fields.TextField(),
    # })
    # rating_profile = fields.ObjectField(properties={
    #     'product_rate': fields.IntegerField(),
    #     'size': fields.IntegerField(),
    #     'complement': fields.IntegerField(),
    #     'side_dish': fields.IntegerField(),
    #     'comment': fields.TextField(),
    # })

    class Index:
        name = 'rating'
        setting = {
            'number_of_shards': 1,
            'number_of_replicas': 1,
            'size': 1000
        }

    class Django:
        model = Rating

        fields = ['id', 'product_rate', 'size', 'complement', 'side_dish', 'comment']

        # related_models = [Product, Profile]

@registry.register_document
class WishlistDocument(Document):

    # wishlist_profile = fields.ObjectField(properties={'note': fields.TextField()})
    # wishlist_product = fields.ObjectField(properties={'note': fields.TextField()})

    class Index:
        name = 'wishlist'
        setting = {
            'number_of_shards': 1,
            'number_of_replicas': 1,
            'size': 1000
        }

    class Django:
        model = Wishlist

        fields = ['id', 'note']

        # related_models = [Product, Profile]

