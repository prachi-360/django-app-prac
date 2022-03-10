
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/',include('product.urls')),
    path('group/',include('group.urls')),
    path('orm/',include('orm.urls')),
    path('employee/',include('employee.urls')),
    path('classview/',include('classview.urls')),
    # path('task/',include('task.urls')),
    path('ticket1/',include('ticket1.urls')),
    path('serviceprovider/',include('serviceprovider.urls')),
    path('core/',include('core.urls')),
    path('cart/',include('cart.urls')),
    path('simpleform/',include('simpleform.urls')),
    path('user/',include('userapp.urls')),
]
