from django.conf.urls import url

from.import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # 正規表現で記載
    url(r'^(?P<post_id>[0-9]+)/$', views.post_detail, name='post_detail')

]
