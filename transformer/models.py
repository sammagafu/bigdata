from django.db import models

# Create your models here.
class Transformer(models.Model):
    """Model definition for Transformer."""
    transname = models.CharField(verbose_name="Transformer's name", max_length=100, null=False, blank=False)
    transloclat = models.DecimalField(verbose_name="Transformer's Latitude", max_digits=10, decimal_places=6)
    transloclong = models.DecimalField(verbose_name="Transformer's Longitute", max_digits=10, decimal_places=6)
    kvarating = models.DecimalField(verbose_name="KVA Rating", decimal_places=3, max_digits=5)
    phyaddress = models.TextField(verbose_name="Physical Address")

    class Meta:
        """Meta definition for Transformer."""

        verbose_name = 'Transformer'
        verbose_name_plural = 'Transformers'

    def __str__(self):
        """Unicode representation of Transformer."""
        return self.transname

class TransformerReading(models.Model):
    transformer =models.ForeignKey(Transformer,on_delete=models.CASCADE,related_name="transformer")
    time = models.DateTimeField(auto_now=False, auto_now_add=False)
    phasevred = models.DecimalField(decimal_places=2,max_digits=6,verbose_name="Pharse Voltage Red")
    phasevblue = models.DecimalField(decimal_places=2,max_digits=6,verbose_name="Pharse Voltage Blue")
    phasevyellow = models.DecimalField(decimal_places=2,max_digits=6,verbose_name="Pharse Voltage Yellow")
    phasecred = models.DecimalField(decimal_places=2,max_digits=6,verbose_name="Pharse Current Red")
    phasecblue = models.DecimalField(decimal_places=2,max_digits=6,verbose_name="Pharse Current Blue")
    phasecyellow = models.DecimalField(decimal_places=2, max_digits=6,verbose_name="Pharse Current Yellow")
    
    class Meta:
        verbose_name = "Transformer Reading"
        verbose_name_plural = "Transformer Readings"

    def __str__(self):
        return self.transformer
