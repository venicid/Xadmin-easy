from django.db import models

# Create your models here.


class Author(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32,verbose_name="姓名")
    age = models.IntegerField(verbose_name="年龄")

    # 与AuthorDetail建立一对一的关系
    authorDetail = models.OneToOneField(to="AuthorDetail",to_field="nid", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class AuthorDetail(models.Model):
    nid = models.AutoField(primary_key=True)
    birthday = models.DateField()
    telephone = models.BigIntegerField()
    addr = models.CharField(max_length=64)

    def __str__(self):
        return str(self.telephone)


class Publish(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Book(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='名称', max_length=32)
    publishDate = models.DateField()
    price = models.DecimalField(verbose_name='价格', max_digits=5,decimal_places=2)

    # 与Publish建立一对多的关系,外键字段建立在多的一方
    publish = models.ForeignKey(to="Publish", to_field="nid", on_delete=models.CASCADE)
    # 与Author表建立多对多的关系,ManyToManyField可以建在两个模型中的任意一个，自动创建第三张表
    authors = models.ManyToManyField("Author")

    def __str__(self):
        return self.title
