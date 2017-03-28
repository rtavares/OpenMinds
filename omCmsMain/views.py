from django.shortcuts import render

from .models import categoryItem
from .models import siteMainInfo
from .models import siteSocialMediaReference
from .models import contentArticle


# Create your views here.

def baseIndex(request):
    """
        Home page index
    """

    context = {}
    #context['articleList'] = {}

    siteInfoData = siteMainInfo.objects.get(active=1)

    itemList = categoryItem.objects.filter(itemActive=1).filter(itemOrder__gt=0).order_by('itemOrder')

    articleList = contentArticle.objects.filter(active=1).order_by('order')
    
    context['siteInfoData'] = siteInfoData
    context['itemList'] = itemList
    context['articleList'] = articleList

    template = "omCmsMain/index.html"

    return render(request, template, context)