# Generated by Django 2.2.6 on 2020-05-28 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('civam', '0004_auto_20200528_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='access_notes_or_rights_and_reproduction',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='collection',
            name='citation',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='collection',
            name='provenance',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='access_notes_or_rights_and_reproduction',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='other_forms',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='physical_details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='provenance',
            field=models.TextField(blank=True, null=True),
        ),
    ]
