from .modelsBase import *
from graphql import GraphQLError
from django.conf import settings
from rest_framework.authtoken.models import Token

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
    kerberosPassword = models.CharField(max_length=100)
    VARS = VARS
    class Meta():
        verbose_name = VARS['name']
        verbose_name_plural = VARS['plural']
        permissions = MakePermissions(VARS)
    def getUsername(self):
        return self.username.split('__')[1]
    def getUser(self, username, password, organization, backend):
        try:
            organization = Organization.objects.get(code=organization)
        except Organization.DoesNotExist:
            raise Exception('Organization {0} not found'.format(organization))
        if backend == 'kerberos':
            return self.getKerberosUser(username, password, organization)
    def getKerberosUser(self, username, password, organization):
        try:
            user = User.objects.get(username=organization.code + '__' + username, organization=organization)
        except User.DoesNotExist:
            user = User()
            user.username = organization.code + '__' + username
            user.organization = organization
            user.kerberosPassword = password
            user.set_password(settings.SECRET_KEY)
            user.save()
        return user
