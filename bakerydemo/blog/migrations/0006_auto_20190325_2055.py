# Generated by Django 2.1.7 on 2019-03-25 20:55

from django.db import migrations, models
import django.db.models.deletion
import uuid
import wagtail_i18n.models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_i18n', '0004_locale'),
        ('blog', '0005_auto_20190325_1757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpeoplerelationship',
            name='language',
        ),
        migrations.AddField(
            model_name='blogindexpage',
            name='locale',
            field=models.ForeignKey(default=wagtail_i18n.models.Locale.default_id, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtail_i18n.Locale'),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='locale',
            field=models.ForeignKey(default=wagtail_i18n.models.Locale.default_id, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtail_i18n.Locale'),
        ),
        migrations.AddField(
            model_name='blogpeoplerelationship',
            name='locale',
            field=models.ForeignKey(default=wagtail_i18n.models.Locale.default_id, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtail_i18n.Locale'),
        ),
        migrations.AlterField(
            model_name='blogindexpage',
            name='translation_key',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='translation_key',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='blogpeoplerelationship',
            name='translation_key',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.RemoveField(
            model_name='blogindexpage',
            name='language',
        ),
        migrations.AlterUniqueTogether(
            name='blogindexpage',
            unique_together={('translation_key', 'locale')},
        ),
        migrations.RemoveField(
            model_name='blogpage',
            name='language',
        ),
        migrations.AlterUniqueTogether(
            name='blogpage',
            unique_together={('translation_key', 'locale')},
        ),
    ]