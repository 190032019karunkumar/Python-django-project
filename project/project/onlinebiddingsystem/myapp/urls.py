from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.mainpage,name="main"),
    path('start',views.mainpage,name="main"),
    path('reg/', views.registerpage,name="register"),
    path('login/', views.loginpage, name="login"),
    path('auc',views.auctionpage,name="auctions"),
    path('daily',views.dailyauctionpage,name="daily"),
    path('win',views.winnerpage,name="winners"),
    path('test',views.testimonialspage,name="testimonials"),
    path('off', views.offerpage, name="offers"),
    path('bid/<int:id>', views.bidpage, name="bidding"),
    path('bc/<int:id>', views.destroy, name="biddingcancel"),
    path('up/<int:id>',views.update,name="update"),
    path('uppro/<int:id>',views.updatepro,name="updateprofile"),
    path('dbid/<int:id>', views.dailybidpage, name="dailybidding"),
    path('logout/',views.logoutUser,name="logout"),
    path('ind',views.indexpage,name="index"),
    path('pro/<int:id>/<str:username>', views.profile, name="profile"),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)