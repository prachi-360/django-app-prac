
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/',include('product.urls')),
    path('group/',include('group.urls')),
    path('orm/',include('orm.urls')),
    path('employee/',include('employee.urls'))
    
]
