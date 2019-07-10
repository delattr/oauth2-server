from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    """
    Create uesr with the email as an identifer
    """

    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError("The eamil is required.")
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **kwargs):

        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)

        if kwargs.get('is_staff') is False:
            raise ValueError("is_staff must be True")
        if kwargs.get('is_superuser') is False:
            raise ValueError("is_superuser must be True")
        return self.create_user(email, password, **kwargs)

