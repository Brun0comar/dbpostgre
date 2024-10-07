from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from superheroes.views import SuperheroesListCreate, SuperheroesDetail
from superheroes.serializers import MyTokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/superheroes/', SuperheroesListCreate.as_view(), name='superheroes_list_create'),
    path('api/superheroes/<int:pk>/', SuperheroesDetail.as_view(), name='superheroes_detail'),
]
