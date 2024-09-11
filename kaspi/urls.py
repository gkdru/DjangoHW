from django.urls import path, re_path, include
from . import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('goods', views.ApiGoodsViewSet)
router.register('shop', views.ApiGoodsViewSetReadOnly)
app_name = "kaspi"
urlpatterns = [
    # path("api/get_goods/", views.api_goods, name="for_api"),
    # path("api/good_detail/<int:pk>/", views.api_good_detail, name="detail_good"),
    # path("api/get_goods/", views.APIGoods.as_view(), name="for_api"),
    # path("api/good_detail/<int:pk>/", views.APIGoodsDetail.as_view(), name="detail_good"),
    path('api/', include(router.urls)),

]
0