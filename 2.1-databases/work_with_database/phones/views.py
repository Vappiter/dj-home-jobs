from django.shortcuts import render, redirect


from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    var_sort = request.GET.get("sort", '')
    if var_sort == 'min_price':
     var_phone = Phone.objects.all().order_by('price')
    elif var_sort == 'name':
        var_phone = Phone.objects.all().order_by ('name')
    elif var_sort == 'max_price':
        var_phone = Phone.objects.all().order_by ('-price')    
    elif var_sort == '':   
       var_phone = Phone.objects.all() 
    phones = []
    for var in var_phone:
      print (var.slug)  
      phones.append({'name':var.name, 'image':var.image, 'price':var.price, 'slug':var.slug})
                       
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    var = Phone.objects.get(slug = slug)
    context = {'phone': var}
    return render(request, template, context)
    
   
