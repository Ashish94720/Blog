from django.contrib import admin

from .models import Post
# Register your models here.


class PostmodelAdmin(admin.ModelAdmin):
	list_display = ['title','updated','timestamp']
	list_display_links = ['updated']
	list_editable = ['title']
	list_filter = ['updated','timestamp']
	search_fields = ['title','content']
	class Meta:
		model = Post


admin.site.register(Post, PostmodelAdmin)


