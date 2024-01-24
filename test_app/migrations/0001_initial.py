# Generated by Django 4.2.7 on 2024-01-24 16:28

from django.db import migrations, models
import test_app.storage


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TestModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        storage=test_app.storage.NoReadFileSystemStorage(),
                        upload_to="images/",
                    ),
                ),
                ("width", models.IntegerField()),
                ("height", models.IntegerField()),
            ],
        ),
    ]
