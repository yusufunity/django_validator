from django.shortcuts import render,get_object_or_404,redirect
from .models import News,Category
from .forms import NewsForm


def home(request):
	news=News.objects.all()
	categories=Category.objects.all()
	context={
		'news':news,
		'categories':categories,
		'title':"Yusufdev blogi"
		


	}
	return render(request, template_name='news/index.html',context=context)


def get_category(request, category_id):
	
	news = News.objects.filter(category_id=category_id)
	
	categories = Category.objects.all()

	category = Category.objects.get(pk=category_id)
	

	context={

		'news':news,
		'categories':categories,
		'category':category
		

	}	

	return render(request,template_name='news/category.html',context=context)



def view_news(request,news_id):
	
	# news_item = News.objects.get(pk=news_id)
	news_item=get_object_or_404(News,pk=news_id)
	
	context={
		"news_item":news_item
	}

	return render(request,template_name='news/view_news.html',context=context)
	
	
def add_news(request):
	if request.method=="POST":
		form =NewsForm(request.POST)
		####---is_valid() metod bazaga ulanganlik tekshiriladi
		if form.is_valid():
			# # print(form.cleaned_data)
			# title=form.cleaned_data['title']
			# content=form.cleaned_data['content']
			# is_published=form.cleaned_data['is_published']
			# category=form.cleaned_data['category']
			obj=form.save()
			# obj= News.objects.create(title=title,content=content,is_published=is_published,category=category)
			## --- redirect metod url korsatamiz
			# return redirect('home') ##
			return redirect(obj)

	else:

		form = NewsForm()

	return render(request,'news/add_news.html',{"form":form })
	

