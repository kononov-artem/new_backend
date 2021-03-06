from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'languages', views.LanguagesView.as_view(), name='languages'),
    url(r'words', views.WordsView.as_view(), name='words'),
    url(r'translates', views.TranslateView.as_view(), name='translates'),
    path('dictionaries/update/', views.DictionariesUpdate.as_view(), name='dictionaries_update'),
    url(r'dictionaries', views.DictionariesView.as_view(), name='dictionaries'),

    path('user/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
    path('translate/<int:pk>/', views.TranslateDetailDetail.as_view(), name='translate_detail'),
    path('language/<int:pk>/', views.LanguageDetailDetail.as_view(), name='language_detail'),
    path('dictionary/<int:pk>/', views.DictionaryDetail.as_view(), name='dictionary_detail'),
    path('language/add/', views.LanguageAdd.as_view(), name='language_add'),
    path('word/add/', views.WordAdd.as_view(), name='word_add'),

    path('check-permission/', views.CheckPermission.as_view(), name='check_permission'),
    path('get-token-by-user/', views.GetTokenByUser.as_view(), name='get_token_by_user'),
    path('search-word/', views.SearchWord.as_view(), name='search_word'),
    path('search-translate/', views.SearchTranslate.as_view(), name='search_translate'),

    #     # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

    path(r'auth/', include('djoser.urls')),
    path(r'auth/', include('djoser.urls.authtoken')),
    path(r'auth/', include('djoser.urls.jwt')),
]
