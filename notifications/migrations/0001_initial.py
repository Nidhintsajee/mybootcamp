# Generated by Django 2.1 on 2018-08-21 05:52

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('unread', models.BooleanField(db_index=True, default=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('uuid_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('slug', models.SlugField(blank=True, max_length=210, null=True)),
                ('verb', models.CharField(choices=[('L', 'liked'), ('C', 'commented'), ('F', 'cavorited'), ('A', 'answered'), ('W', 'accepted'), ('E', 'edited'), ('K', 'also commented'), ('I', 'logged in'), ('O', 'logged out'), ('V', 'voted on'), ('S', 'shared'), ('U', 'created an account'), ('R', 'replied to')], max_length=1)),
                ('action_object_object_id', models.CharField(blank=True, max_length=50, null=True)),
                ('action_object_content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notify_action_object', to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'Notification',
                'ordering': ('-timestamp',),
                'verbose_name_plural': 'Notifications',
            },
        ),
    ]