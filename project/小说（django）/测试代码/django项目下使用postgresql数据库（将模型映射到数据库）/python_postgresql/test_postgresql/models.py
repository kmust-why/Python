from django.db import models

# Create your models here.

class Chapter(models.Model):
    chapterid = models.AutoField(primary_key=True)
    novelid = models.ForeignKey('Novel', models.DO_NOTHING, db_column='novelid')
    title = models.CharField(max_length=100)
    content = models.TextField()

    class Meta:
        db_table = 'chapter'

class Novel(models.Model):
    novelid = models.AutoField(primary_key=True)
    type = models.IntegerField()
    novelname = models.CharField(max_length=100)
    novelimg = models.CharField(max_length=100)
    description = models.TextField()
    state = models.CharField(max_length=20)
    author = models.CharField(max_length=20)

    class Meta:
        db_table = 'novel'
