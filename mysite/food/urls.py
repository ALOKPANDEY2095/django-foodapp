from . import views
from django.urls import path


app_name="food"
urlpatterns = [
    #"/food/"
    path('', views.index,name='index'),
    #'/food/item_id/
    path('<int:item_id>/',views.details,name="details"),
    path('name/',views.name, name="name"),
    #add item
    path('add',views.create_item, name="create_item"),
    #update item
    path('update/<int:id>/',views.update_item,name='update_item'),
    #deete item
    path('delete/<int:id>/',views.delete_item,name="delete_item")
]
