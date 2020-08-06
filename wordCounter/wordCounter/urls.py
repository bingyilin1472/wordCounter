"""wordCounter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from . import view
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    # empty string就是沒有slash加path
    # path('', view.homepage),
    # path('get-eggs/', view.eggs),
    # path('greeting/', view.greeting),
    # 下面都有設定name屬性，這樣可以比較自由的修改連結的url，而不用再去修改HTML裡面的連結url path
    path('', view.wordcounting, name='home'),
    # 有name的route path很適合用在連結上，譬如<a>、<form action=>，因為比較方便去修改切換的path
    # 因為它會追蹤name，就不會因為route path修改，造成無法去運作
    path('count-word/', view.counting, name='count'),
    path('info/', view.showInfo, name='info')
]
