from django.contrib.admin import AdminSite

class CustomSite(AdminSite):
    site_header = 'DjangoBlog'
    site_title = 'DjangoBlog管理后台'
    index_title = '首页'

custom_site = CustomSite(name='cus_admin')