from django.contrib.admin import ModelAdmin, register
from django.contrib import admin
from import_export import resources
from import_export.fields import Field
from import_export.admin import ImportExportActionModelAdmin
from django.contrib.auth.admin import UserAdmin
from . models import PersonInfo, User

# Admin settings
admin.site.site_header = "DDC-PRO"
admin.site.site_title = "Department of Social Welfare and Community Development"


class PersonInfoResource(resources.ModelResource):
    delete = Field()

    def for_delete(self, row, instance):
        return self.fields['delete'].clean(row)

    class Meta:
        model = PersonInfo


class UserResource(resources.ModelResource):
    delete = Field()

    def for_delete(self, row, instance):
        return self.fields['delete'].clean(row)

    class Meta:
        model = User


class PersonInfoAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'full_name', 'date_of_birth', 'today_date', 'gender', 'id_type', 'id_number', 'mobile_number', 'disability_type',
                    'community_name', 'street_name', 'land_mark', 'house_number', 'caregiver_name', 'caregiver_number', 'passport_pic',)
    list_filter=('id', 'disability_type', 'id_type', 'caregiver_name',)
    search_fields=('id', 'disability_type', 'id_type',
                   'id_number', 'caregiver_name',)
    resource_class=PersonInfoResource
    icon_name='person'


admin.site.register(PersonInfo, PersonInfoAdmin)


class UserAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display=('username', 'email', 'first_name', 'last_name',
                    'zonal_council', 'date_joined', 'is_active', 'is_staff',)
    list_filter=('username', 'zonal_council', 'is_staff',)
    search_fields=('username', 'zonal_council', 'is_staff',)
    resource_class=UserResource
    icon_name='person'


admin.site.register(User, UserAdmin)
