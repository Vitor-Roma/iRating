from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from app import views
from app.views import Register, home, products
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from app.views import RatingDocumentView, RestaurantDocumentView, ProductDocumentView, ProfileDocumentView, \
    WishlistDocumentView

route = routers.DefaultRouter()

route.register(r'profile', views.ProfileViewSet, basename='profile')
route.register(r'restaurants', views.RestaurantViewSet, basename='restaurants')
route.register(r'products', views.ProductViewSet, basename='products')
route.register(r'rating', views.RatingViewSet, basename='ratings')
route.register(r'wishlist', views.WishlistViewSet, basename='wishlist')

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', home, name='home'),
                  path('products/', products, name='html_products'),
                  path('api/login/', TokenObtainPairView.as_view(), name='login'),
                  path('login/refresh/', TokenRefreshView.as_view(), name='refresh'),
                  path('api/sign-up/', Register.as_view(), name='sign-up'),
                  path('api/', include(route.urls), name='api-home'),
                  path('profile/search/', ProfileDocumentView.as_view({'get': 'list'}), name='search_profile'),
                  path('restaurants/search/', RestaurantDocumentView.as_view({'get': 'list'}),
                       name='search_restaurants'),
                  path('products/search/', ProductDocumentView.as_view({'get': 'list'}), name='search_product'),
                  path('rating/search/', RatingDocumentView.as_view({'get': 'list'}), name='search_rating'),
                  path('wishlist/search/', WishlistDocumentView.as_view({'get': 'list'}), name='search_wishlist'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
