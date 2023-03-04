from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import os

urlpatterns = [
    path('admin/', admin.site.urls),
    path('driver/', include('driver.urls'))
]

# Include project-level static files
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Include app-level static files
urlpatterns += static(settings.STATIC_URL, document_root=os.path.join(settings.BASE_DIR, 'driver', 'static'))

