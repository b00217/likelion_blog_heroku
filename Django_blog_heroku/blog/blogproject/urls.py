from django.contrib import admin
from django.urls import path, include
import blogapp.views
import portfolio.views
#media 파일 쓰기위해 두개 받기
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.views.home, name="home"),
    path('blog/', include('blogapp.urls')), #url상속
    path('portfolio/', portfolio.views.portfolio, name="portfolio"),
    path('accounts/', include('accounts.urls')),
]

#media 파일 위해서
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)