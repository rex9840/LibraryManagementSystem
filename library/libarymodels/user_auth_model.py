from .books import BorrowedBooks
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

class LibraryUserManager(BaseUserManager):
    
    def create_user(self, email,username,password=None,burrowed_books=None):
        if not email: 
            raise ValueError("Email is required")
        if not username:
            raise ValueError("Username is required")

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            burrowed_books = burrowed_books,
        )   
        user.password = password
        user.save(using=self._db)
        return user

    def create_superuser(self, email,username,password=None):

        create_user = self.create_user(
            email = email,
            username = username,
        )
        create_user.password = password
        create_user.is_admin = True
        create_user.is_staff = True
        create_user.is_superuser = True
        create_user.save(using=self._db)
        return create_user




class LibraryUser(AbstractBaseUser): 
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=255,unique=True)
    username = models.CharField(max_length=255,unique=True)
    password = models.CharField(max_length=16)
    borrowed_books = models.ManyToManyField(BorrowedBooks,blank=True)
    is_active = models.BooleanField(default=True)
    membership_date = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','password']
    PASSWORD_FIELD = 'password'


    objects = LibraryUserManager()



    class Meta:
        db_table = 'library_user'
        verbose_name = 'Library User'
        verbose_name_plural = 'Library Users'
        ordering = ['membership_date']


    def __str__(self):
        return self.username

    
    def has_perm(self,per,obj=None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True


    def save(self, *args, **kwargs):
        self.set_password(self.password)
        return super().save(*args, **kwargs)

