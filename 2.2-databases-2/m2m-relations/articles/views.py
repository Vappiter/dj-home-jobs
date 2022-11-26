from django.shortcuts import render

from articles.models import Article, Tag, Scopes


def articles_list(request):
    template = 'articles/news.html'
    
    ordering = '-published_at'
    
    var = Article.objects.all().order_by(ordering)
        
    context = {'object_list':var}
    

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    

    return render(request, template, context)
