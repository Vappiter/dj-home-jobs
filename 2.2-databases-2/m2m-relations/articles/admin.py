from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scopes

class ScopesInlineFormset(BaseInlineFormSet):
    def clean(self):
        # var_tag = 
        var_is_main = 0
        for form in self.forms:
          if  form.cleaned_data ['is_main'] == True:
           var_is_main += 1   
                          
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
           form.cleaned_data
           print (form.cleaned_data)
            # for var in form.cleaned_data.items():
            #   print(var) 
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
            # raise ValidationError('Тут всегда ошибка')
        if  var_is_main == 0:
         raise ValidationError('Должен быть выбран один ОСНОВНОЙ тег')      
        elif var_is_main > 1:
         raise ValidationError('ОСНОВНОЙ тег может быть только один')  
            
        return super().clean()  # вызываем базовый код переопределяемого метода



class ScopesInLine(admin.TabularInline):
    model = Scopes
    formset = ScopesInlineFormset
    extra = 0

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display: ('id', 'title', 'published_at')
    inlines = [ScopesInLine,]

@admin.register(Tag)    
class TagAdmin(admin.ModelAdmin):
    list_display: ('id', 'name')
    
     