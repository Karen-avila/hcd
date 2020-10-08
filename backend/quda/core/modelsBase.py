from django.contrib.auth.models import AbstractUser, Permission, Group
from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.models import Site
from django.db import models, transaction
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.db.models import *


from mptt.models import MPTTModel, TreeForeignKey
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from localflavor.mx.models import MXRFCField, MXZipCodeField, MXCURPField

from rest_framework import serializers

import django_filters
import json
import datetime
import uuid

from itertools import chain


APP = 'core'

def MakePermissions(VARS):
    permissions = []
    if not 'excludePermissions' in VARS:
        exclude_permissions = []
    else:
        exclude_permissions = VARS['excludePermissions']
    if not 'all' in exclude_permissions:
        if not 'view' in exclude_permissions:
            permissions.append(('Can_View__' + VARS['model'], 'Ve ' + VARS['plural'].lower()))
        if not 'create' in exclude_permissions:
            permissions.append(('Can_Create__' + VARS['model'], 'Crea ' + VARS['plural'].lower()))
        if not 'update' in exclude_permissions:
            permissions.append(('Can_Update__' + VARS['model'], 'Modifica ' + VARS['plural'].lower()))
        if not 'delete' in exclude_permissions:
            permissions.append(('Can_Delete__' + VARS['model'], 'Elimina ' + VARS['plural'].lower()))
    if 'extendPermissions' in VARS:
        for permission in VARS['extendPermissions']:
            permissions.append(permission)
    return permissions

########################################################################################
VARS = {
    'model': 'ModelBase',
    'name': 'ModelBase',
    'plural': 'ModelBase',
    #'newName': 'nuevo',
    #'newGender': 'un nuevo',
    #'this': 'este',
    #'excludePermissions': ['all'],
    #'extendPermissions': [],
}
class ModelBase(models.Model):
    active = models.BooleanField(default=True)
    VARS = VARS
    class Meta():
        verbose_name = VARS['name']
        verbose_name_plural = VARS['plural']
        permissions = MakePermissions(VARS)
        abstract = True
    @property
    def getProperties(self):
        try:
            return VARS
        except:
            return {}

########################################################################################
class Basic_Serializer(serializers.ModelSerializer):
    class Meta:
        model = None
        fields = ('__all__')
        exclude = ()
class Base_Serializer(Basic_Serializer):
    #url_list = serializers.ReadOnlyField()
    #url_add = serializers.ReadOnlyField()
    #url_update = serializers.ReadOnlyField()
    #url_delete = serializers.ReadOnlyField()
    #url_detail = serializers.ReadOnlyField()
    #str_obj = serializers.ReadOnlyField()
    class Meta(Basic_Serializer.Meta):
        model = None
        fields = ('__all__')
