"""recipes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.urls import path

from calculator.views import recipes_view_1, home_view, recipes_view_2

urlpatterns = [
    path('', home_view, name='home'),
    path('v1',recipes_view_1, name='recipes_1'),
    path('v1/<str:var1>/', recipes_view_1, name='recipes_1'),
    path('v2',recipes_view_2, name='recipes_2'),
    path('v2/<str:var1>/', recipes_view_2, name='recipes_2'),
]
