from django.contrib import admin


from .models import News,Category




class NewsAdmin(admin.ModelAdmin):
	list_display=('id','title','category','create_at','update_at','is_published')
	## link berish oynasi
	list_display_links=('id','title')
	##qidirish oynasi
	search_fields=('title','content')
	###-- table yasash
	list_editable=('is_published',)
	##-filter qilish
	list_filter=('is_published','category')

class CategoryAdmin(admin.ModelAdmin):
	list_display=('id','title')
	## link berish oynasi
	list_display_links=('id','title')
	##qidirish oynasi
	search_fields=('title',)


admin.site.register(News,NewsAdmin)
admin.site.register(Category,CategoryAdmin)