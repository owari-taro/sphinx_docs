===========================
django-admin
===========================

-----------------
CustomUser
-----------------




ユーザー編集時の項目を変えたい
==============================

fieldsetsを書き換える

::
    
    class CustomUserAdmin(UserAdmin):
        filedssets=(
            ,
        )
        def get_queryset(self,request):
            qs = super().get_queryset(request)
            if request.user.is_superuser:
                return qs
            group_id=request.user.origin_group.group_id
            return qs.filter(origin_group__group_id=group_id)


::

        
    @admin.register(User)
    class UserAdmin(admin.ModelAdmin):
        add_form_template = "admin/auth/user/add_form.html"
        change_user_password_template = None
        fieldsets = (
            (None, {"fields": ("username", "password",)}),
            (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
            (
                _("Permissions"),
                {
                    "fields": (
                        "is_active",
                        "roles",
                        "is_staff",
                        "is_superuser",
                        "groups",
                        "user_permissions",
                    ),
                },
            ),
            (_("Important dates"), {"fields": ("last_login", "date_joined")}),
        )

------------------
表示データの制限
------------------



Groupによる制限
=====================


ユーザーの属性での制限
======================



----------------------
表記のカスタマイズ
----------------------





サイトタイトルの変更
====================

AdminSiteを継承することでadminページのタイトルヘッダーなどを書き換えることができる

::

    from django.contrib.admin import AdminSite
    class CustomAdminSite(AdminSite):
        title_header="test"
        site_header="test"
        index_title="test"


.. warning:: 
    AdminSiteを継承して作った場合はdefaultのGroupを別途追加しないと
    表示されなくなる `参考 <https://stackoverflow.com/questions/68225313/django-group-model-not-showing-up-in-django-admin>`__
    またデフォルトのようにpermissionsのフィルターが消えてしまうのでadmin.pyで登録する必要がある

    ::

        from django.contrib import admin
        from django.contrib.auth.models import User, Group
        from django.contrib.auth.admin import UserAdmin,GroupAdmin

        .....

        admin_site.register(Group,GroupAdmin)

    内部実装はこんな感じ
    ::

        @admin.register(Group)
        class GroupAdmin(admin.ModelAdmin):
            search_fields = ("name",)
            ordering = ("name",)
            filter_horizontal = ("permissions",)

            def formfield_for_manytomany(self, db_field, request=None, **kwargs):
                if db_field.name == "permissions":
                    qs = kwargs.get("queryset", db_field.remote_field.model.objects)
                    # Avoid a major performance hit resolving permission names which
                    # triggers a content_type load:
                    kwargs["queryset"] = qs.select_related("content_type")
                return super().formfield_for_manytomany(db_field, request=request, **kwargs)


-------------------
modelの表示
-------------------

list表示のカスタマイズ
======================

csvダウンロード
======================

#https://stackoverflow.com/questions/73681437/django-import-export-export-one-to-many-relationship-with-foreignkeywidget-r
