from django.db import migrations, models
import django.db.models.deletion


def populate_categories(apps, schema_editor):
    Interest = apps.get_model('about', 'Interest')
    Category = apps.get_model('about', 'Category')

    for interest in Interest.objects.all():
        raw_value = getattr(interest, 'category', '') or ''
        slug = str(raw_value).strip().lower()
        if not slug:
            continue

        name = slug.replace('_', ' ').replace('-', ' ').title()
        category, _ = Category.objects.get_or_create(slug=slug, defaults={'name': name})
        interest.category_new = category
        interest.save(update_fields=['category_new'])


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_remove_interest_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='interest',
            name='category_new',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='interests', to='about.category'),
        ),
        migrations.RunPython(populate_categories, migrations.RunPython.noop),
        migrations.RemoveField(
            model_name='interest',
            name='category',
        ),
        migrations.RenameField(
            model_name='interest',
            old_name='category_new',
            new_name='category',
        ),
    ]
