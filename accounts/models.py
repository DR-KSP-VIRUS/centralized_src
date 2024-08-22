from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    
    def create_user(self, email, password=None, is_active=True, is_admin=False, is_staff=False,is_student=False):
        if not email:
            raise ValueError("User must have email")
        if not password or len(password) < 6:
            raise ValueError("Password must be at least 6 characters")
        
        user_obj = self.model(email=self.normalize_email(email))
        user_obj.set_password(password)
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.staff = is_staff
        user_obj.student = is_student
        user_obj.save(using=self._db)
        return user_obj
    
    def create_staffuser(self, email, password=None):
        user = self.create_user(email, password=password, is_staff=True)
        return user
    
    def create_superuser(self, email, password):
        user = self.create_user(
            email, password=password,
            is_admin=True,
            is_staff=True,
            is_student=True
        )
        return user

    def create_studentuser(self, email, password=None):
        user = self.create(
            email, password=password, is_student=True
        )

# Create your models here.
class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    active = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    student = models.BooleanField(default=False)
    full_name = models.CharField(max_length=255, null=True, blank=False)
    created = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    objects = UserManager()

    def get_full_name(self):
        return self.email
    
    def get_short_name(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.staff
    
    @property
    def is_admin(self):
        return self.admin
    
    @property
    def is_active(self):
        return self.active
    
    @property
    def is_student(self):
        return self.student


class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_portfolios")
    full_name = models.CharField(blank=True, null=True, max_length=255)
    title = models.CharField(blank=True, null=True, max_length=255)
    first_phone = models.CharField(blank=True, null=True, max_length=255)
    second_phone =  models.CharField(blank=True, null=True, max_length=255)
    email = models.CharField(blank=True, null=True, max_length=255)
    photo = models.ImageField(upload_to="images/%Y/%m/%d")
    turnor = models.CharField(blank=True, null=True, max_length=255) #2024/2025
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.full_name}'