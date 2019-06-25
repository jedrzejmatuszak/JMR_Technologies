from django.urls import path
from shortener.views import URLView, RedirectView


urlpatterns = [
    path('', URLView.as_view(), name='get_url'),
    path('url-<int:url_no>', RedirectView.as_view(), name='redirect')
]
