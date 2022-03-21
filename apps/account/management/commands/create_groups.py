import logging

from django.contrib.auth.models import Group, Permission
from django.core.management import BaseCommand

GROUPS = {
    'doctor':
        [
            {
                'model': 'board',
                'permissions': ['view', 'add', 'change', 'delete']
            }
        ],
    'patient': {}
}


class Command(BaseCommand):
    help = 'Creates read only default permission groups for users'

    def handle(self, *args, **options):
        for key, group in GROUPS.items():
            new_group, created = Group.objects.get_or_create(name=key)
            if created:
                for item in group:
                    for permission in item.get('permissions'):
                        name = 'Can {} {}'.format(permission, item.get('model'))
                        print("Creating {}".format(name))

                        try:
                            model_add_perm = Permission.objects.get(name=name)
                        except Permission.DoesNotExist:
                            logging.warning("Permission not found with name '{}'.".format(name))
                            continue
                        new_group.permissions.add(model_add_perm)

        print("Created default group and permissions.")
