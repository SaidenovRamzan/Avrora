from django.urls import path
from documents import views


urlpatterns = [
    path('list/', views.DocumentListView.as_view(), name='document_list'),
    path('<int:pk>/detail', views.DocumentDetailView.as_view(), name='document_detail'),
    path('create/', views.DocumentCreateView.as_view(), name='document_create'),
    path('<int:pk>/update/', views.DocumentUpdateView.as_view(), name='document_update'),
    path('<int:pk>/delete/', views.DocumentDeleteView.as_view(), name='document_delete'),
]
