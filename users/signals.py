import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile
import time

@receiver(post_save, sender=User)
def slow_signal_handler(sender, instance, **kwargs):
    print(f"Signal received for user: {instance.username}")
    print("Simulating a long process...")
    time.sleep(5)
    print("Signal processing completed.")

@receiver(post_save, sender=User)
def log_signal_thread(sender, instance, **kwargs):
    print(f"Signal received for user: {instance.username}")
    print(f"Signal handler running in thread: {threading.current_thread().name}")

@receiver(post_save, sender=User)
def create_profile(sender, instance, **kwargs):
    print("Signal handler: Creating profile")
    Profile.objects.create(user=instance)