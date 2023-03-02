
from django.urls import path

from calculator.views import recipe_products

urlpatterns = [
    path('<dish_name>/', recipe_products, name='omlet'),
]