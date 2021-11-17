# Generated by Django 3.2.7 on 2021-11-14 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_comment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_text',
            field=models.TextField(max_length=250, verbose_name='Comment Text'),
        ),
        migrations.AlterField(
            model_name='news',
            name='news_item_text',
            field=models.TextField(max_length=500),
        ),
    ]