from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_herosection_intro_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='interest',
            name='cover_image',
            field=models.ImageField(default='', upload_to='interests/covers/'),
            preserve_default=False,
        ),
    ]
