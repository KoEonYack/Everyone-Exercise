from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('blog/', include('blog.urls')),
    path('ad_post/', include('ad_post.urls')),
    path('map/', include('polls.urls')),
    path('obj/', include('object_board.urls')),
    path('', lambda req:redirect('blog:post_list'), name='root'),  # URL reverse
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)