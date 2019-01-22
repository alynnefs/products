from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',
         namespace='rest_framework')),
    path('login/', obtain_jwt_token),
    path('refresh-token/', refresh_jwt_token),
]
