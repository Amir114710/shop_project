from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserManager(BaseUserManager):
    def create_user(self, phone , password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not phone:
            raise ValueError('Users must have an email address')

        user = self.model(
            phone=self.normalize_email(phone),
        )

        user.set_password(password)
        # user.set_email(email)
        # user.set_Full_name(Full_name)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            phone,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='پست الکترونیک',
        max_length=255,
    )
    phone = models.CharField(max_length=12 , verbose_name='شماره تلفن' , unique = True , default='0')
    image = models.ImageField(upload_to='UserImage' , verbose_name='عکس کاربر' , null=True, blank=True)
    Full_name = models.CharField(max_length=200 , verbose_name='نام کامل' , null=True, blank=True)
    is_active = models.BooleanField(default=True , verbose_name='فعال')
    is_admin = models.BooleanField(default=False , verbose_name='ادمین')

    objects = UserManager()

    USERNAME_FIELD = 'phone'
    # REQUIRED_FIELDS = ['']

    def __str__(self):
        return self.phone
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural ='کاربر ها'
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

class OTP(models.Model):
    token = models.CharField(max_length=12 , null=True)
    phone = models.CharField(max_length=12)
    password = models.CharField(max_length=50)
    code = models.SmallIntegerField(null=True, blank=True)
    expiration_date =  models.DateTimeField(null=True, blank=True , auto_now_add=True)
    created_at = models.DateTimeField(null=True, blank=True , auto_now_add=True)

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = "کد:otp"
        verbose_name_plural = "کد:otp ها"
        ordering = ("-created_at",)