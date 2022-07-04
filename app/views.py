import uuid
from rest_framework.response import Response
from rest_framework import viewsets, status, generics, permissions
from .serializers import UserRegisterSerializer, RestaurantSerializer, ProductSerializer, RatingSerializer, \
    WishlistSerializer, ProfileSerializer
from .models import Profile, Restaurant, Product, Rating, Wishlist
from django.views import generic
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .documents import ProductDocument, ProfileDocument, RestaurantDocument, RatingDocument, WishlistDocument
from django_elasticsearch_dsl_drf.filter_backends import FilteringFilterBackend, CompoundSearchFilterBackend
from django.shortcuts import render

def home(request):
    restaurant = Restaurant.objects.all()
    number_of_rest = len(restaurant)
    products = Product.objects.all()
    number_of_prod = len(products)
    rating = Rating.objects.all()
    number_of_rating = len(rating)
    wishlist = Wishlist.objects.all()
    number_of_wishlist = len(wishlist)
    data = {
            'number_rest': number_of_rest,
            'number_prod': number_of_prod,
            'number_rating': number_of_rating,
            'number_wishlist': number_of_wishlist,
            'restaurant_key': restaurant
    }
    return render(request, 'home.html', data)

def products(request):
    product = Product.objects.all()
    data = {'product_key': product}
    return render(request, 'products.html', data)





class IndexView(generic.ListView):
    template_name = 'index.html'


class Register(generics.GenericAPIView):
    serializer_class = UserRegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'RequestId': str(uuid.uuid4()),
                'Message': 'User has been created',
                'User': serializer.data}, status=status.HTTP_201_CREATED,
            )
        return Response()


class ProfileViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'username']


class RestaurantViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'name']


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'detail', 'price']


class RatingViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'product_rate', 'size', 'complement', 'side_dish', 'comment']


class WishlistViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = WishlistSerializer
    queryset = Wishlist.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'note']


# Elastic search views


class RestaurantDocumentView(DocumentViewSet):
    document = RestaurantDocument
    serializer_class = RestaurantSerializer

    filter_backends = [FilteringFilterBackend, CompoundSearchFilterBackend]

    search_fields = ('id', 'name')
    multi_match_search_fields = ('id', 'name')
    filter_fields = {'id': 'id',
                     'name': 'name'}


class ProfileDocumentView(DocumentViewSet):
    document = ProfileDocument
    serializer_class = ProfileSerializer

    filter_backends = [FilteringFilterBackend, CompoundSearchFilterBackend]

    search_fields = ('id', 'username')
    multi_match_search_fields = ('id', 'username')
    filter_fields = {'id': 'id',
                     'username': 'name'}


class ProductDocumentView(DocumentViewSet):
    document = ProductDocument
    serializer_class = ProductSerializer

    filter_backends = [FilteringFilterBackend, CompoundSearchFilterBackend]

    search_fields = ('id', 'name', 'detail', 'price')
    multi_match_search_fields = ('id', 'name', 'detail', 'price',)
    filter_fields = {'id': 'id',
                     'name': 'name',
                     'detail': 'detail',
                     'price': 'price'
                     }


class RatingDocumentView(DocumentViewSet):
    document = RatingDocument
    serializer_class = RatingSerializer

    filter_backends = [FilteringFilterBackend, CompoundSearchFilterBackend]

    search_fields = ('id', 'product_rate', 'size', 'complement', 'side_dish', 'comment')
    multi_match_search_fields = (
        'id', 'product_rate', 'size', 'complement', 'side_dish', 'comment')
    filter_fields = {'id': 'id',
                     'product_rate': 'product_rate',
                     'size': 'size',
                     'complement': 'complement',
                     'side_dish': 'side_dish',
                     'comment': 'comment'}


class WishlistDocumentView(DocumentViewSet):
    document = WishlistDocument
    serializer_class = WishlistSerializer

    filter_backends = [FilteringFilterBackend, CompoundSearchFilterBackend]

    search_fields = ('id', 'note')
    multi_match_search_fields = ('id', 'profile_id', 'product_id', 'note')
    filter_fields = {'id': 'id',
                     'note': 'note'}
