#_*_ coding:utf-8 _*_
__author__ = 'Harryue'
__date__ = '2018/2/23 下午11:36'

from organization.models import CityDict, courseOrg, Teacher
import xadmin

class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']

xadmin.site.register(CityDict, CityDictAdmin)


class courseOrgAdmin(object):
    list_display = ['name', 'desc', 'click_nums', 'fev_nums', 'image', 'address', 'city', 'add_time']
    search_fields = ['name', 'desc', 'click_nums', 'fev_nums', 'image', 'address', 'city']
    list_filter = ['name', 'desc', 'click_nums', 'fev_nums', 'image', 'address', 'city', 'add_time']

xadmin.site.register(courseOrg, courseOrgAdmin)


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years', 'work_company', 'work_postition', 'points', 'click_nums', 'fev_nums', 'add_time']
    search_fields = ['org', 'name', 'work_years', 'work_company', 'work_postition', 'points', 'click_nums', 'fev_nums']
    list_filter = ['org', 'name', 'work_years', 'work_company', 'work_postition', 'points', 'click_nums', 'fev_nums', 'add_time']

xadmin.site.register(Teacher, TeacherAdmin)

