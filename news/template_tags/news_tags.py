# from django import template
# from news.models import Category


# ###----- kodlarni takrorlab yozmaslik ushun  simple_tag()----
# @register.simple_tag(name='get_yusuf')

# register = template.Library()

# def get_category():
# 	return Category.objects.all()



# @register.inclusion_tag('news/list_categories.html')

# # register=template.Library()

# def show_cat(arg1='Hello',arg2='world'):
	
# 	categories=Category.objects.all()
	
# 	return {"categories":categories,"arg1":arg1,"arg2":arg2}
#  