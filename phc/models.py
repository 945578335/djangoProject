# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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


class HashChain(models.Model):
    sip = models.CharField(max_length=15)
    dip = models.CharField(max_length=15)
    seq = models.IntegerField()
    contype = models.IntegerField()
    signtype = models.IntegerField()
    content = models.TextField()
    msghash = models.CharField(max_length=80)
    chainhash = models.CharField(max_length=80)
    salt = models.CharField(max_length=100, blank=True, null=True)
    sharekey = models.CharField(max_length=100, blank=True, null=True)
    sign = models.TextField(blank=True, null=True)
    action = models.CharField(max_length=30, null=True)

    class Meta:
        managed = False
        db_table = 'hash_chain'


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


class PhcUser(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=15)
    action = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'phc_user'


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


class SysConfig(models.Model):
    variable = models.CharField(primary_key=True, max_length=128)
    value = models.CharField(max_length=128, blank=True, null=True)
    set_time = models.DateTimeField(blank=True, null=True)
    set_by = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_config'
