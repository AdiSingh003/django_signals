from django.shortcuts import HttpResponse
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import transaction
from django.db.models.signals import post_save
from users.signals import slow_signal_handler, log_signal_thread, create_profile
import threading

def create_user_view_q1(request):
    post_save.disconnect(log_signal_thread, sender=User)
    post_save.disconnect(create_profile, sender=User)
    unique_username = f'testuser_{timezone.now().timestamp()}'
    email = f'{unique_username}@example.com'
    user = User.objects.create(username=unique_username, email=email)
    post_save.connect(log_signal_thread, sender=User)
    post_save.connect(create_profile, sender=User)
    return HttpResponse(f'User {user.username} created')

def create_user_view_q2(request):
    post_save.disconnect(slow_signal_handler, sender=User)
    post_save.disconnect(create_profile, sender=User)
    print(f"View running in thread: {threading.current_thread().name}")
    unique_username = f'testuser_{timezone.now().timestamp()}'
    email = f'{unique_username}@example.com'
    user = User.objects.create(username=unique_username, email=email)
    post_save.connect(slow_signal_handler, sender=User)
    post_save.connect(create_profile, sender=User)
    return HttpResponse(f'User {user.username} created')

def create_user_view_q3(request):
    post_save.disconnect(slow_signal_handler, sender=User)
    post_save.disconnect(log_signal_thread, sender=User)

    try:
        with transaction.atomic():
            unique_username = f'testuser_{timezone.now().timestamp()}'
            email = f'{unique_username}@example.com'
            user = User.objects.create(username=unique_username, email=email)
            print("View: User created")
            raise Exception("Simulating an error to trigger a rollback")
    except Exception as e:
        return HttpResponse(f"Error occurred: {str(e)}")
    
    post_save.connect(slow_signal_handler, sender=User)
    post_save.connect(log_signal_thread, sender=User)
    return HttpResponse(f'User {user.username} created')