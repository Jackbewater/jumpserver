from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('acls', '0008_ticket_workflow_integration'),
    ]

    operations = [
        migrations.AddField(
            model_name='commandfilteracl',
            name='script_preflight_enabled',
            field=models.BooleanField(
                default=False, verbose_name='Enable Agent script preflight',
                help_text='Apply this rejection rule to commands inside Bash scripts in Linux SSH sessions.',
            ),
        ),
    ]
