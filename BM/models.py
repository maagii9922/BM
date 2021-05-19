from django.db import models
from django.utils.translation import ugettext_lazy as _

class Hereglegch(models.Model):
    name = models.CharField(max_length=30, verbose_name=_("Хэрэглэгчийн нэр"))
    code = models.CharField(max_length=30, verbose_name=_("Хэрэглэгчийн код"))

    class Meta:
        verbose_name = _("Хэрэглэгч")
        verbose_name_plural = _("Хэрэглэгч")

class Company(models.Model):
    comName = models.CharField(max_length=50, verbose_name=_("Компаний нэр"))
    mail = models.CharField(max_length=50, verbose_name=_("Компаний майл"))
    password = models.CharField(max_length=50, verbose_name=_("Майлын нууц үг"))
    password2 = models.CharField(max_length=50, verbose_name=_("Майлын нууц үг давтах"))

    class Meta:
        verbose_name = _("Компани")
        verbose_name_plural = _("Компани")

class Product(models.Model):
    pName = models.CharField(max_length=50, verbose_name=_("Барааны нэр"))
    zCode = models.IntegerField(null=True, blank=True, verbose_name=_("Зураасан код"))
    pType = models.IntegerField(null=True, blank=True, verbose_name=_("Барааны төрөл"))
    zzCode = models.IntegerField(null=True, blank=True, verbose_name=_("Нэмэлт зураасан код"))
    price = models.IntegerField(null=True, blank=True, verbose_name=_("Үнэ"))
    hemNegj = models.IntegerField(null=True, blank=True, verbose_name=_("Хэмжих нэгж"))
    hudNegj = models.IntegerField(null=True, blank=True, verbose_name=_("Худалдан авалтын нэгж"))
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    erNershil = models.CharField(max_length=50, verbose_name=_("Ерөнхий нэршил"))
    emHelber = models.CharField(max_length=50, verbose_name=_("Эмийн хэлбэр"))
    paiz = models.CharField(max_length=50, verbose_name=_("Пайз"))
    uildwerlegch = models.CharField(max_length=50, verbose_name=_("Үйлдвэрлэгч"))
    uNiiluulegch = models.CharField(max_length=50, verbose_name=_("Үндсэн нийлүүлэгч"))
    category = models.CharField(max_length=50, verbose_name=_("Дотоод ангилал"))
    borBoloh = models.CharField(max_length=50, verbose_name=_("Борлуулж болох"))
    hudAwch = models.CharField(max_length=50, verbose_name=_("Худалдан авч болох"))
    state = models.IntegerField(null=True, blank=True, verbose_name=_("Төлөв"))


    class Meta:
        verbose_name = _("Бараа")
        verbose_name_plural = _("Бараа")















