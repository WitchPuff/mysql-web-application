# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Advisor(models.Model):
    s = models.OneToOneField('Student', models.DO_NOTHING, db_column='s_ID', primary_key=True)  # Field name made lowercase.
    i = models.ForeignKey('Instructor', models.DO_NOTHING, db_column='i_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'advisor'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Classroom(models.Model):
    building = models.CharField(primary_key=True, max_length=15)
    room_number = models.CharField(max_length=7)
    capacity = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'classroom'
        unique_together = (('building', 'room_number'),)


class Course(models.Model):
    course_id = models.CharField(primary_key=True, max_length=8)
    title = models.CharField(max_length=50, blank=True, null=True)
    dept_name = models.ForeignKey('Department', models.DO_NOTHING, db_column='dept_name', blank=True, null=True)
    credits = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course'


class Department(models.Model):
    dept_name = models.CharField(primary_key=True, max_length=20)
    building = models.CharField(max_length=15, blank=True, null=True)
    budget = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'department'


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
    id = models.BigAutoField(primary_key=True)
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


class Grades(models.Model):
    grade = models.CharField(max_length=2, blank=True, null=True)
    point = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grades'


class Instructor(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=5)  # Field name made lowercase.
    name = models.CharField(max_length=20)
    dept_name = models.ForeignKey(Department, models.DO_NOTHING, db_column='dept_name', blank=True, null=True)
    salary = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'instructor'


class Prereq(models.Model):
    course = models.OneToOneField(Course, models.DO_NOTHING, primary_key=True)
    prereq = models.ForeignKey(Course, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'prereq'
        unique_together = (('course', 'prereq'),)


class Section(models.Model):
    course = models.OneToOneField(Course, models.DO_NOTHING, primary_key=True)
    sec_id = models.CharField(max_length=8)
    semester = models.CharField(max_length=6)
    year = models.DecimalField(max_digits=4, decimal_places=0)
    building = models.ForeignKey(Classroom, models.DO_NOTHING, db_column='building', blank=True, null=True)
    room_number = models.ForeignKey(Classroom, models.DO_NOTHING, db_column='room_number', to_field='room_number', blank=True, null=True)
    time_slot_id = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'section'
        unique_together = (('course', 'sec_id', 'semester', 'year'),)


class Student(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=5)  # Field name made lowercase.
    name = models.CharField(max_length=20)
    dept_name = models.ForeignKey(Department, models.DO_NOTHING, db_column='dept_name', blank=True, null=True)
    tot_cred = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'


class Takes(models.Model):
    id = models.OneToOneField(Student, models.DO_NOTHING, db_column='ID', primary_key=True)  # Field name made lowercase.
    course = models.ForeignKey(Section, models.DO_NOTHING)
    sec = models.ForeignKey(Section, models.DO_NOTHING, to_field='sec_id')
    semester = models.ForeignKey(Section, models.DO_NOTHING, db_column='semester', to_field='semester')
    year = models.ForeignKey(Section, models.DO_NOTHING, db_column='year', to_field='year')
    grade = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'takes'
        unique_together = (('id', 'course', 'sec', 'semester', 'year'),)


class Teaches(models.Model):
    id = models.OneToOneField(Instructor, models.DO_NOTHING, db_column='ID', primary_key=True)  # Field name made lowercase.
    course = models.ForeignKey(Section, models.DO_NOTHING)
    sec = models.ForeignKey(Section, models.DO_NOTHING, to_field='sec_id')
    semester = models.ForeignKey(Section, models.DO_NOTHING, db_column='semester', to_field='semester')
    year = models.ForeignKey(Section, models.DO_NOTHING, db_column='year', to_field='year')

    class Meta:
        managed = False
        db_table = 'teaches'
        unique_together = (('id', 'course', 'sec', 'semester', 'year'),)


class TimeSlot(models.Model):
    time_slot_id = models.CharField(primary_key=True, max_length=4)
    day = models.CharField(max_length=1)
    start_hr = models.DecimalField(max_digits=2, decimal_places=0)
    start_min = models.DecimalField(max_digits=2, decimal_places=0)
    end_hr = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    end_min = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'time_slot'
        unique_together = (('time_slot_id', 'day', 'start_hr', 'start_min'),)
