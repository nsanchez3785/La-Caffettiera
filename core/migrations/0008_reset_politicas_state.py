from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_politicas_content'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[],
            state_operations=[
                migrations.DeleteModel(
                    name='Politicas',
                ),
            ],
        ),
    ]