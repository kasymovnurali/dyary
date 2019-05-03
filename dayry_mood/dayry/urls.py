from django.urls import path
from . import views

urlpatterns = [
	path('', views.DyaryList.as_view(), name='dyary_list'),
	path('dyary/<int:pk>', views.DyaryDetail.as_view(), name='dyary_detail'),
	path('create/', views.DyaryCreate.as_view(), name='dyary_create'),
	path('update/<int:pk>', views.DyaryUpdate.as_view(), name='dyary_update'),
	path('delete/<int:pk>', views.DyaryDelete.as_view(), name='dyary_delete')
]

