import xadmin
from users.models import EmailVerifyRecord, Banner
from xadmin import views

class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_code', 'send_time']  # 添加要显示的列
    search_fields = ['code', 'email', 'send_code', 'send_time']  # 要查询的列
    list_filter = ['code', 'email', 'send_code', 'send_time']  # 要筛选的列

xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)


class BannerAdmin(object):
    list_display = ['title', 'url', 'index', 'add_time', 'image']
    search_fields = ['title', 'url', 'index', 'add_time', 'image']
    list_filter = ['title', 'url', 'index', 'add_time', 'image']

xadmin.site.register(Banner, BannerAdmin)


class GlobalSetting(object):
    site_title = 'mooc'  # 设置头标题
    site_footer = 'mooc'  # 设置脚标题

    menu_style = 'accordion'  # 菜单课收缩

xadmin.site.register(views.CommAdminView, GlobalSetting)


class BaseSetting(object):
    enable_themes = True  # 设置可更换主题
    use_bootswatch = True

xadmin.site.register(views.BaseAdminView, BaseSetting)