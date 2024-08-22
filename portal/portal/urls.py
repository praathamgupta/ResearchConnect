from django.contrib import admin
from django.urls import path
from faculty import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('optimizing-your-resume/', views.blog1, name='optimizing-your-resume'),
    path('sample-cover-letter/', views.blog2, name="sample-cover-letter"),
    path('tips-for-cold-emailing/', views.blog3, name="tips-for-cold-emailing"),
    path('tips-for-getting-internships/', views.blog4, name='tips-for-getting-internships'),
    path('undergraduate-physics-research-internships/', views.blog5, name='undergraduate-physics-research-internships'),
    path('search/', views.search, name='search'),
    path('professor/<slug:professor_name>/', views.professor, name='professor'),
] 

if settings.DEBUG:
  urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
