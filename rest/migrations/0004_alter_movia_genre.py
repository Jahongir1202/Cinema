# Generated by Django 5.0.7 on 2024-07-19 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rest", "0003_alter_movia_genre"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movia",
            name="genre",
            field=models.CharField(
                choices=[
                    ("jangari", "jangari"),
                    ("comedy", "komedia"),
                    ("drama", "drama"),
                    ("horror", "ujas"),
                    ("romance", "romance"),
                    ("fantastik", "fantastik"),
                    ("hayotiy", "hayotiy"),
                ],
                max_length=20,
            ),
        ),
    ]
