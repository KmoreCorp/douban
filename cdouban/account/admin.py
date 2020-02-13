from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import UserAccount
# Register your models here.


#将新加入的user信息加到原user的表单中
class UserAccountInline(admin.TabularInline):
	"""docstring for UserAccountAdmin"""
	model = UserAccount
	can_delete = False
	verbose_name_plural ='注册用户'

class UserAccountAdmin(BaseUserAdmin):
	"""docstring for UserAccountAdmin"""
	inlines = (UserAccountInline, )

admin.site.unregister(User)
admin.site.register(User, UserAccountAdmin)