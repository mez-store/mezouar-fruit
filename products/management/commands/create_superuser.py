from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os

class Command(BaseCommand):
    help = "Create superuser automatically"

    def handle(self, *args, **kwargs):
        username = os.environ.get("ADMIN_USER")
        email = os.environ.get("ADMIN_EMAIL")
        password = os.environ.get("ADMIN_PASS")

        if not username or not password:
            self.stdout.write("❌ Admin credentials not found")
            return

        if User.objects.filter(username=username).exists():
            self.stdout.write("✅ Superuser already exists")
            return

        User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
        self.stdout.write("✅ Superuser created successfully")