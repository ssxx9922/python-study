
import xadmin
from operation.models import UserAsk, CourseComments, UserFavorite, UserMessage, UserCourse


class UserAskAdmin(object):
    list_display = ['name', 'mobile', 'course_name', 'add_time']
    search_fields = ['name', 'mobile', 'course_name']
    list_filter = ['name', 'mobile', 'course_name', 'add_time']

xadmin.site.register(UserAsk, UserAskAdmin)


class CourseCommentsAdmin(object):
    list_display = ['user', 'course', 'commets', 'add_time']
    search_fields = ['user', 'course', 'commets']
    list_filter = ['user', 'course', 'commets', 'add_time']

xadmin.site.register(CourseComments, CourseCommentsAdmin)


class UserFavoriteAdmin(object):
    list_display = ['user', 'fav_id', 'fav_type', 'add_time']
    search_fields = ['user', 'fav_id', 'fav_type']
    list_filter = ['user', 'fav_id', 'fav_type', 'add_time']

xadmin.site.register(UserFavorite, UserFavoriteAdmin)


class UserMessageAdmin(object):
    list_display = ['user', 'message', 'has_read', 'add_time']
    search_fields = ['user', 'message', 'has_read']
    list_filter = ['user', 'message', 'has_read', 'add_time']

xadmin.site.register(UserMessage, UserMessageAdmin)


class UserCourseAdmin(object):
    list_display = ['user', 'user', 'add_time']
    search_fields = ['user', 'user']
    list_filter = ['user', 'user', 'add_time']

xadmin.site.register(UserCourse, UserCourseAdmin)