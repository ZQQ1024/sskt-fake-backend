from django.db import models

# Create your models here.

class ApplicationRecord(models.Model):
    seller = models.CharField(max_length=45)
    recorder = models.CharField(max_length=45)
    updater = models.CharField(max_length=45)
    lastUpdate = models.DateField()
    createDate = models.DateField(auto_now_add=True)


class House(models.Model):
    ar = models.OneToOneField(
        ApplicationRecord,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    thingName = models.CharField(max_length=45)
    thingNumber = models.CharField(max_length=45)
    structI = models.CharField(max_length=45)
    structII = models.CharField(max_length=45)
    thingArea = models.IntegerField()
    stayPeopleNumber = models.IntegerField()
    thingAddr = models.CharField(max_length=45)
    thingAddrPostcode = models.CharField(max_length=45)
    thingRentCost = models.CharField(max_length=45)
    thingManageCost = models.CharField(max_length=45)
    thingGiftCost = models.CharField(max_length=45)
    thingDepositCost = models.CharField(max_length=45)
    thingReliefCost = models.CharField(max_length=45)


class Reward(models.Model):
    ar = models.OneToOneField(
        ApplicationRecord,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    AD = models.CharField(max_length=45)
    agencyFee = models.CharField(max_length=45)
    backFee = models.CharField(max_length=45)


class Company(models.Model):
    ar = models.OneToOneField(
        ApplicationRecord,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    managerCompanyName = models.CharField(max_length=45)
    managerCompanyAddr = models.CharField(max_length=45)
    managerCompanyChargerName = models.CharField(max_length=45)
    managerCompanyPhone = models.CharField(max_length=45)


class Live(models.Model):
    ar = models.OneToOneField(
        ApplicationRecord,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    settlementDate = models.DateField()
    contractDate = models.DateField()


class Renter(models.Model):
    ar = models.OneToOneField(
        ApplicationRecord,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    userNameWrite = models.CharField(max_length=45)
    userNameAlias = models.CharField(max_length=45)
    userNameRead = models.CharField(max_length=45)
    userAddr = models.CharField(max_length=45)
    userAddrPostcode = models.CharField(max_length=45)
    userPhone = models.CharField(max_length=45)

class Tip(models.Model):
    ar = models.OneToOneField(
        ApplicationRecord,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    tip = models.CharField(max_length=45)


class Comment(models.Model):
    ar = models.ForeignKey(ApplicationRecord, on_delete=models.CASCADE)

    upPerson = models.CharField(max_length=45)
    createPerson = models.CharField(max_length=45)
    createDate = models.DateField()
    updatePerson = models.CharField(max_length=45)
    updateDate = models.DateField()
    status = models.CharField(max_length=45)
    content = models.CharField(max_length=45)


class File(models.Model):
    ar = models.ForeignKey(ApplicationRecord, on_delete=models.CASCADE)

    path = models.CharField(max_length=45)


