from django.urls import path, re_path
from django.conf.urls import url
from api.views import views, auth

urlpatterns = [
    path('categories/', views.categories_view),
    path('categories/<int:pk>/', views.category_view),
    path('categories/<int:pk>/products/', views.ProductsView.as_view()),
    path('products/<int:pk>/', views.ProductView.as_view()),
    path('comments/', views.ReviewsView.as_view()),
    path('orders/', views.OrdersView.as_view()),
    path('orders/<int:pk>/', views.OrderView.as_view()),
    path('users/', auth.UserList.as_view()),
    path('login/', auth.Login.as_view()),
    path('logout/', auth.logout),
    path('users/', auth.UserList.as_view())

]