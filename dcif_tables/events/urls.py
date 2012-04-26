from django.conf.urls.defaults import *
from dcif_tables.events.views import *

urlpatterns = patterns('',
                        url(r'^set/$',
                           set_tables,
                           name='set_tables'),
                        url(r'^get/$',
                           get_tables,
                           name='get_tables'),
                        url(r'^get_api/$',
                          get_tables_api,
                          name='get_tables_api'),
                        )
