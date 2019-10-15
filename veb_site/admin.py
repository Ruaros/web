from django.contrib import admin
from django.contrib.auth.models import Group
from .models import rComplProgects, rContacts, rWantContacts
from .forms import rComplProgectsForm


# Register your models here.

#admin.site.site_header = 'Админка'
class rComplProgectsAdmin(admin.ModelAdmin):
   list_display = ('title', 'article', 'datatime', 'typing', 'price', 'author')
   list_filter = ('typing', 'price','author')
   form = rComplProgectsForm
   search_fields = ['article', 'price']

   def get_queryset(self, request):
        """
        Return a QuerySet of all model instances that can be edited by the
        admin site. This is used by changelist_view.
        """
        if request.user.is_superuser:
            qs = self.model._default_manager.get_queryset()
        else:
            qs = rComplProgects.objects.filter(author = request.user.username)
        #qs = self.model._default_manager.get_queryset()
        # TODO: this should be handled by some parameter to the ChangeList.
        ordering = self.get_ordering(request)
        if ordering:
            qs = qs.order_by(*ordering)
        return qs
admin.site.register(rComplProgects, rComplProgectsAdmin)

class rContactsAdmin(admin.ModelAdmin):
   list_display = ('adres', 'email', 'telephone')

admin.site.register(rContacts, rContactsAdmin)

class rWantContactsAdmin(admin.ModelAdmin):
   list_display = ('name', 'town', 'tel', 'email', 'article', 'comment', 'success')
   list_filter = ['success']
   search_fields = ['name', 'town', 'tel', 'email', 'article', 'comment']

admin.site.register(rWantContacts, rWantContactsAdmin)

