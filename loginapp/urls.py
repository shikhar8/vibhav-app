from django.conf.urls import url
from . import views
urlpatterns=[
url(r'^sign$',views.signuppg,name='loginx'),
url(r'^reg$',views.registerr,name='registerr'),
url(r'^vote$',views.vote,name='vote'),
url(r'^votecol$',views.votecol,name='votecol'),
url(r'^$',views.home,name='home'),
#url(r'^con$',views.confirmm,name='confirmm'),
url(r'^vp$',views.votepre,name='votepre'),
url(r'^vp$',views.votepre,name='votepre'),
url(r'^e1$',views.e1,name='e1'),
url(r'^r1$',views.r1,name='r1'),
url(r'^o1$',views.o1,name='o1'),
url(r'^e2$',views.e2,name='e2'),
url(r'^r2$',views.r2,name='r2'),
url(r'^o2$',views.o2,name='o2'),
url(r'^e3$',views.e3,name='e3'),
url(r'^r3$',views.r3,name='r3'),
url(r'^o3$',views.o3,name='o3'),
url(r'^e4$',views.e4,name='e4'),
url(r'^r4$',views.r4,name='r4'),
url(r'^o4$',views.o4,name='o4'),
url(r'^e5$',views.e5,name='e5'),
url(r'^r5$',views.r5,name='r5'),
url(r'^o5$',views.o5,name='o5'),
url(r'^profile$',views.profile,name='profile'),
]