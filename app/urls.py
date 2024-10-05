from django.urls import path
from .views import news_list, news_detail, HomePageView, single,contact,UzbekistanPageview,JahonPageview,Fan_texnikaPageview,IqtisodiyotPageview,SportPageview,JamiyatPageview


urlpatterns = [
    path("", HomePageView, name="homepage"),
    path("uzbekistan/", UzbekistanPageview, name="uzbekistan"),
    path("fan_texnika/", Fan_texnikaPageview, name="fan_texnika"),
    path("iqtisodiyot/", IqtisodiyotPageview, name="iqtisodiyot"),
    path("sport/", SportPageview, name="sport"),
    path("jamiyat/", JamiyatPageview, name="jamiyat"),
    path("jahon/", JahonPageview, name="jahon"),
    path("single/", single, name="single"),
    path("news/", news_list, name='news_all'),
    path("news/<int:id>/", news_detail, name='news_detail_page'),
    path("contact/", contact, name="contact"),
]
