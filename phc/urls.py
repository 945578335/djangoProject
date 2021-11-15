from django.urls import path
from phc import views

urlpatterns = [
    path('phcindex/',views.indexshow),

    path('basic_hash_index/', views.basic_hash_index),
    path('phcbasic1/',views.basicshow1),
    path('phcbasic2/', views.basicshow2),

    path('share_hash_index/', views.share_hash_index),
    path('phcshare1/',views.shareshow1),
    path('phcshare2/',views.shareshow2),

    path('salt_hash_index/', views.salt_hash_index),
    path('phcsalt1/', views.saltshow1),
    path('phcsalt2/', views.saltshow2),

    path('mutual_hash_index/', views.mutual_hash_index),
    path('phcmutual/',views.mutualshow),

    path('first_sign_index/', views.first_sign_index),
    path('phcfirst1/',views.firstshow1),
    path('phcfirst2/', views.firstshow2),

    path('final_sign_index/', views.final_sign_index),
    path('phcfinal1/',views.finalshow1),
    path('phcfinal2/', views.finalshow2),

    path('interval_sign_index/', views.interval_sign_index),
    path('phcinterval1/',views.intervalshow1),
    path('phcinterval2/', views.intervalshow2),

    path('datashow_page/', views.datashow_page),

]