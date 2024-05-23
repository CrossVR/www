from django.db import migrations, models

def transfer_release_to_dlv(apps, schema_editor):
    ReleaseVersion = apps.get_model('downloads', 'ReleaseVersion')
    for release in ReleaseVersion.objects.all():
        release.shortrev = release.version
        release.save()

class Migration(migrations.Migration):

    dependencies = [
        ('downloads', '0002_dlv_move_from_dev'),
    ]

    operations = [
        # ReleaseVersion -> DownloadableVersion
        migrations.RunPython(transfer_release_to_dlv),
        migrations.RemoveField(
            model_name='releaseversion',
            name='version',
        ),
    ]
