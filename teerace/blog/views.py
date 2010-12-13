from django.views.generic.list_detail import object_list, object_detail
from blog.models import Entry


def entry_list(request):
	entries = Entry.objects.all().select_related()
	return object_list(request, queryset=entries)


def entry_detail(request, entry_id):
	entries = Entry.objects.all().select_related()
	return object_detail(request, queryset=entries, object_id=entry_id)
