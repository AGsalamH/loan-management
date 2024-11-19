# Generated by Django 5.0.7 on 2024-11-19 03:49

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0003_bankpersonnel_loancustomer_loanprovider'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fund',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('interest_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('max_fund_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('min_fund_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('duration', models.IntegerField(help_text='Duration in months.')),
                ('status', models.CharField(choices=[('AVAILABLE', 'Available'), ('CLOSED', 'Closed'), ('PENDING', 'Pending'), ('ACTIVE', 'Active'), ('COMPLETED', 'Completed')], default='PENDING', verbose_name='Fund status')),
                ('assigned_to', models.ForeignKey(help_text='Employee responsible for revising the Fund request.', on_delete=django.db.models.deletion.CASCADE, related_name='funds', to='users.bankpersonnel')),
                ('initiated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='funds', to='users.loanprovider')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]