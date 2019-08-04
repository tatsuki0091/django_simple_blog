from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    published = models.DateTimeField()
    image = models.ImageField(upload_to='media/')
    body = models.TextField()

    # 管理画面でタイトルを表示するためのメソッド
    def __str__(self):
        return self.title

    # 本文の表示する文字数を設定して返してもらうメソッド
    def summary(self):
        return self.body[:20]
