# Generated by Django 4.2.16 on 2024-10-28 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_userprofile_profile_picture'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='wishlistitem',
            unique_together={('wishlist_object', 'project_object')},
        ),
    ]
