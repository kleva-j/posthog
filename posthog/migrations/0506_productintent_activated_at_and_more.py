# Generated by Django 4.2.15 on 2024-11-01 16:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posthog", "0505_grouptypemapping_project"),
    ]

    operations = [
        migrations.AddField(
            model_name="productintent",
            name="activated_at",
            field=models.DateTimeField(
                blank=True,
                help_text="The date the org completed activation for the product. Generally only used to know if we should continue updating the product_intent row.",
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="productintent",
            name="activation_last_checked_at",
            field=models.DateTimeField(
                blank=True,
                help_text="The date we last checked if the org had completed activation for the product.",
                null=True,
            ),
        ),
    ]
