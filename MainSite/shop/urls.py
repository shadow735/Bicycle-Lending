
from django.urls import path
from . import views         # This Import Views File

urlpatterns = [

    path("",views.index, name="Shop"),
    path("about/",views.about, name="AboutUs"),
    path("contact/",views.contact, name="Contact"),
    path("tracker/",views.tracker, name="Teacker"),
    path("search",views.search, name="Search"),
    path("productview",views.product, name="ProductView"),
    path("checkout",views.checkout, name="Checkout")

]
