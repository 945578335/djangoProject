# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Basicchain1(models.Model):
    context = models.TextField(blank=True, null=True)
    msghash = models.CharField(max_length=80, blank=True, null=True)
    chainhash = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'basicchain_1'


class Basicchain2(models.Model):
    context = models.TextField(blank=True, null=True)
    msghash = models.CharField(max_length=80, blank=True, null=True)
    chainhash = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'basicchain_2'


class Finalsig1(models.Model):
    context = models.TextField(blank=True, null=True)
    msghash = models.CharField(max_length=80, blank=True, null=True)
    chainhash = models.CharField(max_length=80, blank=True, null=True)
    action = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'finalsig_1'


class Finalsig2(models.Model):
    context = models.TextField(blank=True, null=True)
    msghash = models.CharField(max_length=80, blank=True, null=True)
    chainhash = models.CharField(max_length=80, blank=True, null=True)
    action = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'finalsig_2'


class Firstsig1(models.Model):
    context = models.TextField(blank=True, null=True)
    msghash = models.CharField(max_length=80, blank=True, null=True)
    chainhash = models.CharField(max_length=80, blank=True, null=True)
    action = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'firstsig_1'


class Firstsig2(models.Model):
    context = models.TextField(blank=True, null=True)
    msghash = models.CharField(max_length=80, blank=True, null=True)
    chainhash = models.CharField(max_length=80, blank=True, null=True)
    action = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'firstsig_2'


class Intervalsig1(models.Model):
    context = models.TextField(blank=True, null=True)
    msghash = models.CharField(max_length=80, blank=True, null=True)
    chainhash = models.CharField(max_length=80, blank=True, null=True)
    action = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intervalsig_1'


class Intervalsig2(models.Model):
    context = models.TextField(blank=True, null=True)
    msghash = models.CharField(max_length=80, blank=True, null=True)
    chainhash = models.CharField(max_length=80, blank=True, null=True)
    action = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intervalsig_2'


class Mutualchain(models.Model):
    context = models.TextField(blank=True, null=True)
    msghash = models.CharField(max_length=80, blank=True, null=True)
    chainhash = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mutualchain'


class PhcBasic(models.Model):
    sipname = models.CharField(max_length=50, blank=True, null=True)
    sip = models.CharField(max_length=15)
    dipname = models.CharField(max_length=50, blank=True, null=True)
    dip = models.CharField(max_length=15, blank=True, null=True)
    sipsei = models.CharField(max_length=50, blank=True, null=True)
    dipsei = models.CharField(max_length=50, blank=True, null=True)
    sipsui = models.CharField(max_length=50, blank=True, null=True)
    dipsui = models.CharField(max_length=50, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'phc_basic'


class PhcFinalsig(models.Model):
    sipname = models.CharField(max_length=50, blank=True, null=True)
    sip = models.CharField(max_length=15)
    dipname = models.CharField(max_length=50, blank=True, null=True)
    dip = models.CharField(max_length=15, blank=True, null=True)
    sipsei = models.CharField(max_length=50, blank=True, null=True)
    dipsei = models.CharField(max_length=50, blank=True, null=True)
    sipsui = models.CharField(max_length=50, blank=True, null=True)
    dipsui = models.CharField(max_length=50, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    sign = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'phc_finalsig'


class PhcFirstsig(models.Model):
    sipname = models.CharField(max_length=50, blank=True, null=True)
    sip = models.CharField(max_length=15)
    dipname = models.CharField(max_length=50, blank=True, null=True)
    dip = models.CharField(max_length=15, blank=True, null=True)
    sipsei = models.CharField(max_length=50, blank=True, null=True)
    dipsei = models.CharField(max_length=50, blank=True, null=True)
    sipsui = models.CharField(max_length=50, blank=True, null=True)
    dipsui = models.CharField(max_length=50, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    sign = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'phc_firstsig'


class PhcIntervalsig(models.Model):
    sipname = models.CharField(max_length=50, blank=True, null=True)
    sip = models.CharField(max_length=15)
    dipname = models.CharField(max_length=50, blank=True, null=True)
    dip = models.CharField(max_length=15, blank=True, null=True)
    sipsei = models.CharField(max_length=50, blank=True, null=True)
    dipsei = models.CharField(max_length=50, blank=True, null=True)
    sipsui = models.CharField(max_length=50, blank=True, null=True)
    dipsui = models.CharField(max_length=50, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    interval = models.IntegerField(blank=True, null=True)
    sign = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'phc_intervalsig'


class PhcMutual(models.Model):
    sipname = models.CharField(max_length=50, blank=True, null=True)
    sip = models.CharField(max_length=15)
    dipname = models.CharField(max_length=50, blank=True, null=True)
    dip = models.CharField(max_length=15, blank=True, null=True)
    sipsei = models.CharField(max_length=50, blank=True, null=True)
    dipsei = models.CharField(max_length=50, blank=True, null=True)
    sipsui = models.CharField(max_length=50, blank=True, null=True)
    dipsui = models.CharField(max_length=50, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'phc_mutual'


class PhcSalt(models.Model):
    sipname = models.CharField(max_length=50, blank=True, null=True)
    sip = models.CharField(max_length=15)
    dipname = models.CharField(max_length=50, blank=True, null=True)
    dip = models.CharField(max_length=15, blank=True, null=True)
    sipsei = models.CharField(max_length=50, blank=True, null=True)
    dipsei = models.CharField(max_length=50, blank=True, null=True)
    sipsui = models.CharField(max_length=50, blank=True, null=True)
    dipsui = models.CharField(max_length=50, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    salt = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'phc_salt'


class PhcShare(models.Model):
    sipname = models.CharField(max_length=50, blank=True, null=True)
    sip = models.CharField(max_length=15)
    dipname = models.CharField(max_length=50, blank=True, null=True)
    dip = models.CharField(max_length=15, blank=True, null=True)
    sipsei = models.CharField(max_length=50, blank=True, null=True)
    dipsei = models.CharField(max_length=50, blank=True, null=True)
    sipsui = models.CharField(max_length=50, blank=True, null=True)
    dipsui = models.CharField(max_length=50, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    sharekey = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'phc_share'


class Saltchain1(models.Model):
    context = models.TextField(blank=True, null=True)
    msghash = models.CharField(max_length=80, blank=True, null=True)
    chainhash = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'saltchain_1'


class Saltchain2(models.Model):
    context = models.TextField(blank=True, null=True)
    msghash = models.CharField(max_length=80, blank=True, null=True)
    chainhash = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'saltchain_2'


class Sharechain1(models.Model):
    context = models.TextField(blank=True, null=True)
    msghash = models.CharField(max_length=80, blank=True, null=True)
    chainhash = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sharechain_1'


class Sharechain2(models.Model):
    context = models.TextField(blank=True, null=True)
    msghash = models.CharField(max_length=80, blank=True, null=True)
    chainhash = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sharechain_2'
