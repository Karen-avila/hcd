from django.contrib.auth.backends import ModelBackend
from .models import User, Organization
import pexpect

class CoreBackend(ModelBackend):
    def authenticate(self, request, **kwargs):
        try:
            organization, username = kwargs['username'].split('__', 1)
            proc = pexpect.spawn(("kinit {0}").format(username))
            proc.expect('Password for .*: ')
            proc.sendline(("{0}").format(kwargs['password']))
            proc.expect(pexpect.EOF, timeout=5)
            if proc.before.decode('UTF8') == '\r\n':
                return User().getUser(username, kwargs['password'], organization, backend='kerberos')
            return None
        except:
            return None
    def getUser(self, userId):
        try:
            return User.objects.get(pk=userId)
        except User.DoesNotExist:
            return None
