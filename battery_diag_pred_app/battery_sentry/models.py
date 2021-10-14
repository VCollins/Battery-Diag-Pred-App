from django.db import models

# Create your models here.

class User(models.Model):
    userId = models.CharField(max_length=200)
    password = models.CharField(max_length=300)

    def __str__(self):
        return self.userId

class Battery(models.Model):
    manufacturer = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    serialNumber = models.CharField(max_length=200)
    originalOutputVoltage = models.FloatField()
    dateOfPurchase = models.DateField()
    capacity = models.CharField(max_length=10)
    batteryType = models.CharField(max_length=200)
    batteryDimensions = models.CharField(max_length=200)
    weight = models.FloatField()
    terminalLayout = models.CharField(max_length=200)
    warranty = models.CharField(max_length=10)
    users = models.ManyToManyField(User, through='UserBatteryDetail')

    def __str__(self):
        return self.manufacturer + ' ' + self.model

class DepletionReading(models.Model):
    batteryId = models.ForeignKey(Battery, on_delete=models.CASCADE)
    depletionVoltageReading = models.FloatField()
    readingDateTime = models.DateTimeField()


    def __str__(self):
        return self.depletionVoltageReading + ' : ' + self.readingDateTime

class ChargeReading(models.Model):
    batteryId = models.ForeignKey(Battery, on_delete=models.CASCADE)
    chargeVoltageReading = models.FloatField()
    readingDateTime = models.DateTimeField()

    def __str__(self):
        return self.chargeVoltageReading + ' : ' + self.readingDateTime

class UserBatteryDetail(models.Model):
    battery = models.ForeignKey(Battery, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)