# Generated by Django 4.2.7 on 2024-01-02 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0007_alter_logo_atu_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='summary',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_title',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lab.category'),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover_image',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to='book_covers'),
        ),
        migrations.AlterField(
            model_name='book',
            name='pdf_book',
            field=models.FileField(blank=True, max_length=200, null=True, upload_to='pdf_books'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publication_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='logo',
            name='atu_logo',
            field=models.ImageField(blank=True, null=True, upload_to='atu_logo'),
        ),
        migrations.AlterField(
            model_name='school',
            name='school_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory_name', models.CharField(max_length=50, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lab.category')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='subcategory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lab.subcategory'),
        ),
        migrations.AddField(
            model_name='category',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lab.department'),
        ),
    ]