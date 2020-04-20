from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.index, name = 'index'),
    path('createProtocolFile', views.create_protocol_file, name = 'create_protocol_file'),
    path('displayTemplateFile=<int:p_template_id>', views.display_template_file, name = 'display_template_file'),
    path('uploadProtocolTemplates', views.upload_protocol_templates, name = 'upload_protocol_templates'),
    path('listOfRequests', views.index, name = 'index'),
	]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
