# Generated by Django 3.0.10 on 2020-10-16 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiling', '0003_auto_20201016_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilingfilecolumn',
            name='profilingFile',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='profiling.ProfilingFile'),
        ),
        migrations.AlterField(
            model_name='profilingfilecolumn',
            name='profilingRule',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='profiling.ProfilingRules'),
        ),
    ]
