from django.db import migrations, models

def transfer_dev_to_dlv(apps, schema_editor):
    DevVersion = apps.get_model('downloads', 'DevVersion')
    for dev in DevVersion.objects.all():
        dev.description_dlv = dev.description
        dev.hash_dlv = dev.hash
        dev.shortrev_dlv = dev.shortrev
        dev.save()

class Migration(migrations.Migration):

    dependencies = [
        ('downloads', '0001_initial'),
    ]

    operations = [
        # DevVersion -> DownloadableVersion
        migrations.AddField(
            model_name='downloadableversion',
            name='description_dlv',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='downloadableversion',
            name='hash_dlv',
            field=models.CharField(db_index=True, default='0000000000000000000000000000000000000000', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='downloadableversion',
            name='shortrev_dlv',
            field=models.CharField(default='build', max_length=64),
            preserve_default=False,
        ),
        migrations.RunPython(transfer_dev_to_dlv),
        migrations.RemoveField(
            model_name='devversion',
            name='description',
        ),
        migrations.RemoveField(
            model_name='devversion',
            name='hash',
        ),
        migrations.RemoveField(
            model_name='devversion',
            name='shortrev',
        ),
        migrations.RenameField(
            model_name='downloadableversion',
            old_name='description_dlv',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='downloadableversion',
            old_name='hash_dlv',
            new_name='hash',
        ),
        migrations.RenameField(
            model_name='downloadableversion',
            old_name='shortrev_dlv',
            new_name='shortrev',
        ),
    ]
