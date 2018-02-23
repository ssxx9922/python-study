#_*_ coding:utf-8 _*_
__author__ = 'Harryue'
__date__ = '2018/2/23 PM6:01'

import xadmin
from courses.models import Courses, Lesson, Video, CourseResoure


class CoursesAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums']
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums']

xadmin.site.register(Courses, CoursesAdmin)

class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'add_time']

xadmin.site.register(Lesson, LessonAdmin)


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']

xadmin.site.register(Video, VideoAdmin)


class CourseResoureAdmin(object):
    list_display = ['course', 'course', 'download', 'add_time']
    search_fields = ['course', 'course', 'download']
    list_filter = ['course', 'course', 'download', 'add_time']

xadmin.site.register(CourseResoure, CourseResoureAdmin)
