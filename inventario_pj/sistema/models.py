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


class InventarioAppCambiotoner(models.Model):
    id = models.BigAutoField(primary_key=True)
    fecha_cambio = models.DateTimeField()
    observaciones = models.TextField(blank=True, null=True)
    equipo = models.ForeignKey('InventarioAppEquipo', models.DO_NOTHING, blank=True, null=True)
    toner_entrante = models.ForeignKey('InventarioAppToner', models.DO_NOTHING)
    toner_saliente = models.ForeignKey('InventarioAppToner', models.DO_NOTHING, related_name='inventarioappcambiotoner_toner_saliente_set')
    usuario = models.ForeignKey('InventarioAppUsuario', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventario_app_cambiotoner'


class InventarioAppCargo(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'inventario_app_cargo'


class InventarioAppDepartamento(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'inventario_app_departamento'


class InventarioAppDependencia(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100, blank=True, null=True)
    sede = models.ForeignKey('InventarioAppSede', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'inventario_app_dependencia'


class InventarioAppDistrito(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    provincia = models.ForeignKey('InventarioAppProvincia', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'inventario_app_distrito'


class InventarioAppEquipo(models.Model):
    id = models.BigAutoField(primary_key=True)
    numero_serie = models.CharField(unique=True, max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True)
    fecha_ingreso = models.DateField(blank=True, null=True)
    estado_equipo = models.ForeignKey('InventarioAppEstadoequipo', models.DO_NOTHING, blank=True, null=True)
    modelo = models.ForeignKey('InventarioAppModelo', models.DO_NOTHING)
    usuario = models.ForeignKey('InventarioAppUsuario', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventario_app_equipo'


class InventarioAppEstadoequipo(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'inventario_app_estadoequipo'


class InventarioAppHistorialestadoequipo(models.Model):
    id = models.BigAutoField(primary_key=True)
    fecha = models.DateTimeField()
    equipo = models.ForeignKey(InventarioAppEquipo, models.DO_NOTHING)
    estado_anterior = models.ForeignKey(InventarioAppEstadoequipo, models.DO_NOTHING, blank=True, null=True)
    estado_nuevo = models.ForeignKey(InventarioAppEstadoequipo, models.DO_NOTHING, related_name='inventarioapphistorialestadoequipo_estado_nuevo_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventario_app_historialestadoequipo'


class InventarioAppMantenimiento(models.Model):
    id = models.BigAutoField(primary_key=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(blank=True, null=True)
    tipo = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    realizado_por = models.CharField(max_length=100, blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    equipo = models.ForeignKey(InventarioAppEquipo, models.DO_NOTHING)
    estado_equipo_post = models.ForeignKey(InventarioAppEstadoequipo, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventario_app_mantenimiento'


class InventarioAppMarca(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'inventario_app_marca'


class InventarioAppModelo(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    marca = models.ForeignKey(InventarioAppMarca, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'inventario_app_modelo'


class InventarioAppNotificacion(models.Model):
    id = models.BigAutoField(primary_key=True)
    mensaje = models.TextField()
    fecha = models.DateTimeField()
    equipo = models.ForeignKey(InventarioAppEquipo, models.DO_NOTHING)
    usuario = models.ForeignKey('InventarioAppUsuario', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'inventario_app_notificacion'


class InventarioAppProvincia(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    departamento = models.ForeignKey(InventarioAppDepartamento, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'inventario_app_provincia'


class InventarioAppSede(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    ciudad = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventario_app_sede'


class InventarioAppToner(models.Model):
    id = models.BigAutoField(primary_key=True)
    codigo = models.CharField(unique=True, max_length=50)
    numero_serie = models.CharField(max_length=100, blank=True, null=True)
    marca = models.CharField(max_length=100, blank=True, null=True)
    fecha_ingreso = models.DateField()
    fecha_solicitud_cambio = models.DateField(blank=True, null=True)
    fecha_cambio = models.DateField(blank=True, null=True)
    cantidad_hojas = models.IntegerField(blank=True, null=True)
    estado = models.CharField(max_length=20)
    equipo = models.ForeignKey(InventarioAppEquipo, models.DO_NOTHING, blank=True, null=True)
    reemplaza_a = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    usuario = models.ForeignKey('InventarioAppUsuario', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventario_app_toner'


class InventarioAppUsuario(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    usuario = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=100)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    cargo = models.ForeignKey(InventarioAppCargo, models.DO_NOTHING, blank=True, null=True)
    dependencia = models.ForeignKey(InventarioAppDependencia, models.DO_NOTHING, blank=True, null=True)
    distrito = models.ForeignKey(InventarioAppDistrito, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventario_app_usuario'
