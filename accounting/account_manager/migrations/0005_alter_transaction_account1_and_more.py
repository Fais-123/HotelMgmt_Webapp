# Generated by Django 4.2.2 on 2023-06-12 03:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account_manager', '0004_remove_account_name_remove_transaction_account_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='account1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='credit', to='account_manager.account'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='account2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='debit', to='account_manager.account'),
        ),
    ]