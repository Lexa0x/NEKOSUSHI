from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('prod/', views.ProdListView.as_view(), name='prod'),
    path('prod/<uuid:pk>/', views.ProdDetailView.as_view(), name='prod-detail'),
    path('prod/create/', views.ProdCreate.as_view(), name='prod_create'),
    path('prod/<uuid:pk>/update/', views.ProdUpdate.as_view(), name='prod_update'),
    path('prod/<uuid:pk>/delete/', views.ProdDelete.as_view(), name='prod_delete'),
]