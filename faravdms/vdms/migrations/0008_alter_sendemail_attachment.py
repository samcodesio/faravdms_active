# Generated by Django 3.2.8 on 2022-02-10 13:41

from django.db import migrations, models
import vdms.validators


class Migration(migrations.Migration):

    dependencies = [
        ('vdms', '0007_alter_sendemail_attachment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sendemail',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to='files', validators=[vdms.validators.validate_file_size], verbose_name=''),
        ),
    ]
