from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserAccount(models.Model):
	"""注册用户信息"""
	user_account = models.OneToOneField(User, on_delete = models.CASCADE)
	nickname = models.CharField(blank=True, max_length=50, verbose_name='昵称')
	birthday = models.DateField(blank=True, verbose_name='生日')
	avartar  = models.ImageField(default = 'default_avartar.png', upload_to = 'avartars', verbose_name='头像')
	location = models.CharField(blank=True, null=True, max_length=50, verbose_name='常住地')
	
	class Meta:
		verbose_name_plural = "注册用户"

	def __str__(self):
		return ""
		##避免下是useraccount.object(1)这类字样
    