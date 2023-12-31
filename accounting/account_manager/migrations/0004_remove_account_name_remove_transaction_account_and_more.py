# Generated by Django 4.2.2 on 2023-06-12 02:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account_manager', '0003_account_account_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='name',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='account',
        ),
        migrations.AddField(
            model_name='account',
            name='credit_account',
            field=models.CharField(default='service revenue', max_length=100),
        ),
        migrations.AddField(
            model_name='account',
            name='debit_account',
            field=models.CharField(default='utility expense', max_length=100),
        ),
        migrations.AddField(
            model_name='transaction',
            name='account1',
            field=models.ForeignKey(default='service revenue', on_delete=django.db.models.deletion.CASCADE, related_name='credit', to='account_manager.account'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='account2',
            field=models.ForeignKey(default='utility expense', on_delete=django.db.models.deletion.CASCADE, related_name='debit', to='account_manager.account'),
        ),
    ]
