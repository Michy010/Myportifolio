# Generated by Django 4.2.3 on 2023-10-16 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='portfoilio_images/')),
                ('technologies_used', models.CharField(max_length=100)),
                ('website_link', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
