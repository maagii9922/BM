from django.db import models
from django.utils.translation import ugettext_lazy as _

class Company(models.Model):
    comName = models.CharField(max_length=50, verbose_name=_("Компаний нэр"))
    hayag = models.CharField(max_length=150, verbose_name=_("Компаний хаяг"))
    phone = models.CharField(max_length=30, verbose_name=_("Компаний утас"))

    class Meta:
        verbose_name = _("Компани")
        verbose_name_plural = _("Компани")

    
    def __str__(self):
         return self.comName

class Customer(models.Model):
    name = models.CharField(max_length=30, verbose_name=_("Харилцагчийн нэр"))
    code = models.CharField(max_length=30, verbose_name=_("Харилцагчийн код"))
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    mail = models.CharField(max_length=50, verbose_name=_("Компаний майл"))
    password = models.CharField(max_length=50, verbose_name=_("Майлын нууц үг"))

    class Meta:
        verbose_name = _("Харилцагч")
        verbose_name_plural = _("Харилцагч")

    def __str__(self):
         return self.name

class Category(models.Model):
    catName = models.CharField(max_length=50, verbose_name=_("Ангилалын нэр"))

    class Meta:
        verbose_name = _("Ангилал")
        verbose_name_plural = _("Ангилал")

    def __str__(self):
         return self.catName

class ProdType(models.Model):
    typeName = models.CharField(max_length=50, verbose_name=_("Төрлийн нэр"))

    class Meta:
        verbose_name = _("Барааны төрөл")
        verbose_name_plural = _("Барааны төрөл")

    def __str__(self):
         return self.typeName

class State(models.Model):
    stateName = models.CharField(max_length=50, verbose_name=_("Төлөвийн нэр"))

    class Meta:
        verbose_name = _("Барааны төлөв")
        verbose_name_plural = _("Барааны төлөв")

    def __str__(self):
         return self.stateName

class Product(models.Model):
    prodName = models.CharField(max_length=50, verbose_name=_("Барааны нэр"))
    zCode = models.IntegerField(null=True, blank=True, verbose_name=_("Зураасан код"))
    prodType = models.ForeignKey(ProdType, on_delete=models.CASCADE)
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
    # category = models.CharField(max_length=50, verbose_name=_("Дотоод ангилал"))
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    borBoloh = models.CharField(max_length=50, verbose_name=_("Борлуулж болох"))
    hudAwch = models.CharField(max_length=50, verbose_name=_("Худалдан авч болох"))
    state = models.ForeignKey(State, on_delete=models.CASCADE)


    class Meta:
        verbose_name = _("Бараа")
        verbose_name_plural = _("Бараа")

    def __str__(self):
         return self.prodName+" "+str(self.state.stateName)















