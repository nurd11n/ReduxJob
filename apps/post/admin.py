from django.contrib import admin
from .models import Post, CompanyPost, CompanyVacancy, Forum, ErCode
#
#
# class PostAdmin(admin.ModelAdmin):
#     list_display = ['name', 'type_post', 'created_at']
#     list_filter = ['type_post', 'celery']
#     search_fields = ['name', 'description', 'celery']
#
#
# class ForumAdmin(admin.ModelAdmin):
#     list_display = ['name', 'created_at']
#     search_fields = ['name', 'description']
#
#
# class ErCodeAdmin(admin.ModelAdmin):
#     list_display = ['name', 'created_at']
#     search_fields = ['name', 'description']
#
#
# class PostCompAdmin(admin.ModelAdmin):
#     list_display = ['name', 'type_post', 'created_at']
#     list_filter = ['type_post', 'celery']
#     search_fields = ['name', 'description', 'celery']
#
#
# class CompanyVacancyAdmin(admin.ModelAdmin):
#     list_display = ['title', 'type_work', 'created_at']
#     list_filter = ['type_work', 'celery']
#     search_fields = ['title', 'type_employment', 'type_work','description', 'celery']
#
#
# admin.site.register(Post, PostAdmin)
# admin.site.register(Forum, ForumAdmin)
# admin.site.register(ErCode, ErCodeAdmin)
# admin.site.register(CompanyPost, PostCompAdmin)
# admin.site.register(CompanyVacancy, CompanyVacancyAdmin)


admin.site.register(Post)
admin.site.register(Forum)
admin.site.register(ErCode)
admin.site.register(CompanyPost)
admin.site.register(CompanyVacancy)