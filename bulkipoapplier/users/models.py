from django.db import models
from django.contrib.auth.models import User

# is_active true for auth.models
#override the default user model

User.is_active = models.BooleanField(default=True)
