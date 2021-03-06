
from django.conf.urls.defaults import *
from lebron.models import Entry

entry_info_dict = {
'queryset': Entry.objects.all(),
'date_field': 'pub_date',
}


urlpatterns = patterns('django.views.generic.date_based',(r'^$','archive_index',entry_info_dict),
	(r'^(?P<year>\d{4})/$','archive_year', entry_info_dict),
	(r'^(?P<year>\d{4})/(?P<month>\w{3})/$','archive_month',entry_info_dict),
	(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$','archive_day',entry_info_dict),
	(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$','object_detail',entry_info_dict),
)