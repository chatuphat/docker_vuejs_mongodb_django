from django.contrib import admin
from django.urls import path, include
from recipe.views import recipe_view_set, book_view_set, doctor_view_set
from rest_framework import routers

# define the router
router = routers.DefaultRouter()
router.register(r'recipe', recipe_view_set)
router.register(r'book', book_view_set)
router.register(r'doctor', doctor_view_set)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # Adds 'Login' link in the top right of the page
    path('api-auth/', include('rest_framework.urls'))

]
