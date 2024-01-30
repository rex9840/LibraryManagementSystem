# Generated by Django 5.0.1 on 2024-01-30 13:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_bookmodel_genremodel_bookdetailsmodel_borrowedbooks_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.AutoField(db_column='BookID', primary_key=True, serialize=False)),
                ('title', models.CharField(db_column='Title', max_length=100)),
                ('isbn', models.CharField(db_column='ISBN', max_length=100)),
                ('published_data', models.DateField(db_column='PublishedDate')),
            ],
            options={
                'ordering': ['book_id'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genere_name', models.CharField(db_column='GenreName', max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='bookmodel',
            name='Genre',
        ),
        migrations.RemoveField(
            model_name='borrowedbooks',
            name='BookID',
        ),
        migrations.CreateModel(
            name='BookDetail',
            fields=[
                ('details_id', models.AutoField(db_column='DetailsID', primary_key=True, serialize=False)),
                ('number_of_pages', models.IntegerField(db_column='NumberOfPages')),
                ('publisher', models.CharField(db_column='Publisher', max_length=100)),
                ('language', models.CharField(db_column='Language', max_length=100)),
                ('book_id', models.ForeignKey(db_column='BookID', on_delete=django.db.models.deletion.CASCADE, to='library.book')),
            ],
            options={
                'ordering': ['book_id'],
            },
        ),
        migrations.CreateModel(
            name='BorrowedBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrowed_date', models.DateField(db_column='BurrowedDate')),
                ('return_date', models.DateField(db_column='ReturnDate')),
                ('book_id', models.ForeignKey(db_column='BookID', on_delete=django.db.models.deletion.CASCADE, to='library.book')),
            ],
            options={
                'ordering': ['borrowed_date'],
            },
        ),
        migrations.AlterField(
            model_name='libraryuser',
            name='borrowed_books',
            field=models.ManyToManyField(blank=True, to='library.borrowedbook'),
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(db_column='Genre', to='library.genre'),
        ),
        migrations.DeleteModel(
            name='BookDetailsModel',
        ),
        migrations.DeleteModel(
            name='GenreModel',
        ),
        migrations.DeleteModel(
            name='BookModel',
        ),
        migrations.DeleteModel(
            name='BorrowedBooks',
        ),
    ]