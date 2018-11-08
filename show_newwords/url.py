from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^show_new_words/(\d+)',views.show_new_words,name='show_new_words'),
    url(r'^show_new_words/createTask',views.createTask,name='show_user_defined_num'),
    url(r'^show_new_words/add_new',views.add_new,name='add_new'),
    url(r'^show_new_words/add_stop',views.add_stop,name='add_stop'),
    url(r'^show_new_words/go_new',views.go_new,name='go_new'),
    url(r'^show_new_words/go_stop',views.go_stop,name='go_stop'),
    url(r'^show_new_words/delete_word',views.delete_word,name='delete_word'),
    url(r'^show_new_words/new_to_stop',views.new_to_stop,name='new_to_stop'),
    url(r'^show_new_words/stop_to_new',views.stop_to_new,name='stop_to_new'),
    url(r'^show_new_words/getCoverResult',views.getCoverResult,name='getCoverResult'),
    url(r'^show_new_words/getAllCoverResult',views.getCoverAllResult,name='getCoverResult'),
]