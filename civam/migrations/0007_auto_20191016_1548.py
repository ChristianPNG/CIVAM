# Generated by Django 2.2.6 on 2019-10-16 19:48

import constrainedfilefield.fields.file
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('civam', '0006_auto_20191014_1544'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', constrainedfilefield.fields.file.ConstrainedFileField(content_types=['image/png', 'image/jpeg'], mime_lookup_length=4096, upload_to='uploaded/')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='civam.Item')),
            ],
        ),
        migrations.DeleteModel(
            name='Media',
        ),
    ]
