from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("medical.urls")),
    path("admin/", admin.site.urls),
]

admin.site.site_header = "Quiz Admin Portal"
admin.site.site_title = "Quiz Admin Portal"
admin.site.index_title = "Site administration"
