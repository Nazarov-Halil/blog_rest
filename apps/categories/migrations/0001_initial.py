# Generated by Django 5.0.3 on 2024-03-23 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blogs', '0002_remove_blog_created_at_blog_title_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('blog', models.ManyToManyField(related_name='category', to='blogs.blog')),
            ],
        ),
    ]
