from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('vcyou_app.urls')),
]

class ReactAppView(TemplateView):
    template_name = "index.html"

urlpatterns += [path('', ReactAppView.as_view())]
urlpatterns += [path('', TemplateView.as_view(template_name='index.html'), name='home')]