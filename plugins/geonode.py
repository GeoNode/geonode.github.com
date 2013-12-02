workshop_base = 'http://docs.geonode.org/en/latest/tutorials'
admin_workshop = workshop_base + '/admin/'
dev_workshop = workshop_base + '/devel/'
users_workshop = workshop_base + '/users/'


def preBuildPage(site, page, context, data):
        context['workshop_base'] = workshop_base
        context['admin_workshop'] = admin_workshop
        context['dev_workshop'] = dev_workshop
        context['users_workshop'] = users_workshop
        return context, data
