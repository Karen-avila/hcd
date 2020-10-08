from .modelsBase import *

########################################################################################
########################################################################################
VARS = {
    'model': 'Module',
    'name': 'modulo',
    'plural': 'modulos',
}
class Module(ModelBase):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    VARS = VARS
    class Meta(ModelBase.Meta):
        verbose_name = VARS['name']
        verbose_name_plural = VARS['plural']
        permissions = MakePermissions(VARS)
    def __str__(self):
        return """[ {0} ] {1}""".format(self.code, self.name)
########################################################################################
########################################################################################
VARS = {
    'model': 'Organization',
    'name': 'organización',
    'plural': 'organizaciones',
}
class Organization(MPTTModel, ModelBase):
    parent = TreeForeignKey('self', null=True, blank=True, related_name='+', db_index=True, on_delete=models.SET_NULL)
    sites = models.ManyToManyField(Site)
    code = models.CharField(max_length=50, unique=True)
    name = models.CharField('Nombre de la organización', max_length=100)
    modules = models.ManyToManyField('Module', blank=True, related_name='+',)
    VARS = VARS
    class Meta(ModelBase.Meta):
        verbose_name = VARS['name']
        verbose_name_plural = VARS['plural']
        permissions = MakePermissions(VARS)
    def __str__(self):
        return """[ {0} ] {1}""".format(self.code, self.name)
    def getModules(self):
        return self.modules.values_list('code', flat=True)
    def getDomains(self):
        return self.sites.values_list('domain', flat=True)
class OrganizationSerializer(Basic_Serializer):
    getModules = serializers.ReadOnlyField()
    class Meta(Basic_Serializer.Meta):
        model = Organization
        fields = ['code','name','getModules','getDomains']
########################################################################################
########################################################################################
VARS = {
    'model': 'User',
    'name': 'usuario',
    'plural': 'usuarios',
}
class User(AbstractUser, ModelBase):
    organization = models.ForeignKey('Organization', blank=True, null=True, on_delete=models.SET_NULL, related_name='+',)
    visibleUsername = models.CharField(max_length=100)
    VARS = VARS
    class Meta():
        verbose_name = VARS['name']
        verbose_name_plural = VARS['plural']
        permissions = MakePermissions(VARS)
    def getVisibleUsername(self):
        return self.username.split("__", 1)[1]
    def getProfiles(self):
        return 'Nuevo Perfil'


