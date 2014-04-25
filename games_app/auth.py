from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.conf import settings
from django.db import models
import hashlib

def email_hash(email):
    sha = hashlib.sha1()
    sha.update(settings.USER_SALT)
    sha.update()
    return sha.hexdigest()


class SWGUserManager(BaseUserManager):
    def create_user(self, email, is_admin=False):
        """Creates a new user based on the hash of the email address."""
        email = BaseUserManager.normalize_email()
        user_id = email_hash(email)
        user = self.model(user=user_id, is_admin=is_admin)

        user.password_notify(new=True)
        user.save(using=self._db)
        return user

class SWGUser(AbstractBaseUser): 
    user_hash = models.CharField(max_length=30, 
                                 unique=True, 
                                 db_index=True, 
                                 verbose_name='user hash')
    moniker = models.CharField(max_length=30, 
                               unique=True, 
                               verbose_name="Moniker")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'user_hash'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        """Our short and long names are the same."""
        return self.moniker
    get_short_name = __unicode__ = get_full_name

    def has_perm(self, perm, obj=None):
        """We're not using permissions other than is_admin."""
        return True

    def has_module_perms(self, app_label):
        """Users can view all apps."""
        return True

    @property
    def is_staff(self):
        """For the admin interface."""
        return self.is_admin

class HashedUserBackend(ModelBackend):
    def hash_user(self, user_id):
        if user_id is None:
            return None
        sha = hashlib.sha1()
        sha.update(settings.USER_SALT)
        sha.update(user_id)
        return sha.hexdigest()

    def get_user(self, user_id):
        return super(HashedUserBackend,self).get_user(self.hash_user(user_id))

    def authenticate(self, username=None, password=None):
        user_hash = self.hash_user(username)
        return super(HashedUserBackend,self).authenticate(user_hash, password)
