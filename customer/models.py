from django.db import models

# Create your models here.
class CustomerHouseHold(models.Model):
    """Model definition for CustomerHouseld."""
    customerRefno = models.IntegerField(verbose_name="Reference Number",unique=True,blank=False,null=False)
    customerMetreno = models.BigIntegerField(verbose_name="Metre Number",unique=True,blank=False,null=False)
    customerAccno = models.IntegerField(verbose_name="Account Number", unique=True, blank=False, null=False)
    customerFirstName = models.CharField(max_length=120,blank=False,null=False,verbose_name="First name")
    customerLastName = models.CharField(max_length=120, blank=False, null=False, verbose_name="Last name")
    customerLat = models.DecimalField(verbose_name="Customer Latitude",decimal_places=6,max_digits=10)
    customerLong = models.DecimalField(verbose_name="Customer Longtitue",decimal_places=6,max_digits=10)
    customerPhone = models.CharField(max_length=11, blank=False, null=False, verbose_name="Customer Phone Number")

    class Meta:
        """Meta definition for CustomerHouseld."""

        verbose_name = 'Customer House hold'
        verbose_name_plural = 'Customer House Holds'

    def __str__(self):
        """Unicode representation of CustomerHouseld."""
        return self.customerFirstName

class Transaction(models.Model):
    """Model definition for Transaction."""
    buyer = models.ForeignKey(CustomerHouseHold, on_delete=models.CASCADE,related_name="buyer")
    date = models.DateField(auto_now=False, auto_now_add=False, verbose_name="Date Bought")
    units = models.DecimalField(verbose_name="Units",decimal_places=2,max_digits=6)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Transaction."""

        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'

    # def __str__(self):
    #     return self.buyer

class MetreReading(models.Model):
    """Model definition for MetreReading."""
    owner = models.ForeignKey(CustomerHouseHold, on_delete=models.CASCADE,related_name="metre")
    date = models.TimeField(auto_now=False, auto_now_add=False, verbose_name="Date Bought")
    voltage = models.IntegerField(verbose_name="metre voltage")
    current = models.IntegerField(verbose_name="metre current")
    consumption = models.IntegerField(verbose_name="metre consumption")



    # TODO: Define fields here

    class Meta:
        """Meta definition for Metre Reading."""

        verbose_name = 'Metre Reading'
        verbose_name_plural = 'Metre Readings'
