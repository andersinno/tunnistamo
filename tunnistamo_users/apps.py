from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin.apps import AdminConfig


class TunnistamoUsersConfig(AppConfig):
    name = 'tunnistamo_users'
    verbose_name = _("Tunnistamo Users")


class TunnistamoUsersAdminConfig(AdminConfig):
    default_site = 'tunnistamo_users.admin.AdminSite'
