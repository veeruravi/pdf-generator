from django.conf.urls import url
#from polls import views
urlpatterns=(
	url(r'^all/$','app1.views.all_users'),
	url(r'^user/(?P<user_id>\d+)/$','app1.views.user'),
	url(r'^func/(?P<user_id>\d+)/$','app1.views.func'),
	url(r'^mail/(?P<user_id>\d+)/$','app1.views.mail'),
)

