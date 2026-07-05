from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_interest_cover_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interest',
            name='icon',
        ),
    ]
