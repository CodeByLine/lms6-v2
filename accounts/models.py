from django.db import models
from django.contrib.auth.models import (
	BaseUserManager, AbstractBaseUser
)
class MyAccountManager(BaseUserManager):
	def create_user(self, email, username, password=None):
		if not email:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')

		user = self.model(
			email=self.normalize_email(email),
			username=username,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user

		
class Account(AbstractBaseUser):
	email = models.EmailField(
		verbose_name ='email address',
		max_length = 255,
		unique = True,
	)
	username = models.CharField(max_length=30, unique=True)
	date_joined	= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login	= models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin	= models.BooleanField(default=False)
	is_active	= models.BooleanField(default=True)
	is_staff	= models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	first_name  = models.CharField(max_length=30)
	last_name  = models.CharField(max_length=30)


	USERNAME_FIELD = 'email' # use email instead of username for login 
	REQUIRED_FIELDS = ['username'] #required for login

	objects = MyAccountManager()

	def __str__(self):
		return self.email + "  |  " + " Username: " + self.username

	# # For checking permissions. to keep it simple all admin have ALL permissons
	def has_perm(self, perm, obj=None):
		return self.is_admin

	# # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
	def has_module_perms(self, app_label):
		return True
	


class CustomUserManager(BaseUserManager):
	pass
#     def create_user(self, email, password=None):
#         """
#         Creates and saves a User with the given email, date of
#         birth and password.
#         """
#         if not email:
#             raise ValueError('Users must have an email address')
#         # username = self.model.normalize_username(username)
#         user = self.model(
#             # username=username,
#             email=self.normalize_email(email),
#             # date_of_birth=date_of_birth,
#         )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None):
#         """
#         Creates and saves a superuser with the given email, date of
#         birth and password.
#         """
#         user = self.create_user(
#             email,
#             password=password,
	
#         )
#         user.is_admin = True
#         user.save(using=self._db)
#         return user


class CustomUser(AbstractBaseUser):
	pass
#     email = models.EmailField(
#         verbose_name='email address',
#         max_length=255,
#         unique=True,
#     )
#     id = models.AutoField(primary_key=True)
#     date_of_birth = models.DateField(blank=True)
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)
#     first_name = models.CharField(max_length=55, blank=True)
#     last_name = models.CharField(max_length=55, blank=True)
#     address = models.TextField(blank=True)
#     username = models.CharField(max_length=55)

#     objects = CustomUserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     def __str__(self):
#         return self.email

#     def has_perm(self, perm, obj=None):
#         "Does the user have a specific permission?"
#         # Simplest possible answer: Yes, always
#         return True

#     def has_module_perms(self, app_label):
#         "Does the user have permissions to view the app `app_label`?"
#         # Simplest possible answer: Yes, always
#         return True
	
#     def get_full_name(self):
#         return f"{self._first_name} {self._last_name}"

#     @property
#     def is_staff(self):
#         "Is the user a member of staff?"
#         # Simplest possible answer: All admins are staff
#         return self.is_admin

# class AdminHOD(CustomUser):
#     # id = models.AutoField(primary_key=True)
#     # admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
#     # created_at = models.DateTimeField(auto_now_add=True)
#     # updated_at = models.DateTimeField(auto_now_add=True)

#     objects = models.Manager()


# class Staff(models.Model):
#     id = models.AutoField(primary_key=True)
#     admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
#     email = models.EmailField()
#     address = models.TextField(blank=True)
#     date_joined = models.DateTimeField(auto_now_add=True)
#     note = models.TextField(blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now_add=True)
#     objects = models.Manager()

#     def get_absolute_url(self):
#         return reverse('staff_detail', kwargs={'pk': self.pk})
