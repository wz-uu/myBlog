from django.shortcuts import render
from .models import Articles,Category,Tag

# FBV function based view 基于函数的视图


def index(request):
    articles = Articles.objects.all()
    #获取最新的5篇文章
    lastest_articles = articles[:5]
    #获取所有的分类
    categories = Category.objects.all()
    #获取所有的标签
    tags = Tag.objects.all()
    context = {
        "articles":articles,
        "lastest_articles":lastest_articles,
        "categories":categories,
        "tags":tags
    }
    return render(request,'index.html',context)


def detail(request,pk):
    article = Articles.objects.get(pk=pk)
    article.increace_visited()
    #获取最新的5篇文章
    lastest_articles = Articles.objects.all()[:5]
    #获取所有的分类
    categories = Category.objects.all()
    #获取所有的标签
    tags = Tag.objects.all()
    context = {
        'article':article,
        "lastest_articles":lastest_articles,
        "categories":categories,
        "tags":tags
    }
    return render(request,'single_article.html',context)

def contact(request):
    return render(request,'contact.html')


def about(request):
    return render(request,'about.html')

