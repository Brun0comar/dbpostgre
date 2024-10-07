from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model


User = get_user_model()

@receiver(post_save, sender=User)
def create_auth_user(sender, instance, created, **kwargs):
    if created:
                print(f"Usuario {instance.username} creado con éxito.")
                

