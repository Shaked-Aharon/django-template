from django.contrib import admin
from django.contrib.auth.models import Group, User
# Register your models here.
from .models import Category, Product, About, CarouselImage
import sys
RUNNING_DEVSERVER = (len(sys.argv) > 1 and sys.argv[1] == 'runserver')
admin.site.register(Category)
admin.site.register(Product)
# admin.site.register(About)

class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Allow add permission only if there are no About instances
        if About.objects.count() >= 1:
            return False
        return super().has_add_permission(request)

admin.site.register(About, AboutAdmin)
admin.site.unregister(Group)
if not RUNNING_DEVSERVER:
    admin.site.unregister(User)
    
class CarouselImageAdmin(admin.ModelAdmin):
    list_display = ['caption', 'image']

admin.site.register(CarouselImage, CarouselImageAdmin)