from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os

class Command(BaseCommand):
    help = 'Create default admin user if not exists'

    def handle(self, *args, **kwargs):
        username = os.environ.get("ADMIN_USER", "mez_pc")
        email = os.environ.get("ADMIN_EMAIL", "admin@mezouar.com")
        password = os.environ.get("ADMIN_PASS", "Admin12345")

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
            self.stdout.write(self.style.SUCCESS("✅ Admin created"))
        else:
            self.stdout.write("ℹ️ Admin already exists")