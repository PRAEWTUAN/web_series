from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('series/<int:series_id>/comments/', views.comments_view, name='comments'),
    path('series/<int:id>/', views.series_detail, name='series_detail'),  # Keep only one
    path('add_series/', views.add_series, name='add_series'),
    path('series/', views.series_list, name='series_list'),
    path('series/<str:country>/', views.series_list, name='series_by_country'),
    path('recommended/', views.recommended_series, name='recommended_series'),  # New path for recommended

    # เพิ่ม path สำหรับการแก้ไขซีรีส์
    path('series/edit/<int:series_id>/', views.edit_series, name='edit_series'),

    # เพิ่ม path สำหรับการลบซีรีส์
    path('series/delete/<int:series_id>/', views.delete_series, name='delete_series'),
    path('watchlist/', views.view_watchlist, name='view_watchlist'),
    path('watchlist/add/<int:series_id>/', views.add_to_watchlist, name='add_to_watchlist'),
    path('watchlist/remove/<int:series_id>/', views.remove_from_watchlist, name='remove_from_watchlist'),
    path('series/<int:id>/', views.series_detail, name='series_detail'),
    path('series/<int:id>/', views.series_detail, name='series_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
