===========================
django-admin
===========================

-----------------
ModelAdmin
-----------------


ログインユーザーごとに一覧表示の範囲を制御したい
=======================================================
get_querysetを書き換える `公式 <https://docs.djangoproject.com/en/4.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.get_queryset>`__



一覧ページでまとめて処理したい
===============================================
デフォルトではまとめて削除があるが同じように、まとめてstatusを変えるみたいなのが自作できる

`dj-admin-action<https://www.google.com/search?client=firefox-b-d&q=django+admi+actrion>`__





ユーザー作成時・編集時の項目を変えたい
===========================================
作成時に指定する項目と編集時に指定する項目はそれぞれ別々のfieldで設定する必要があ\\\

作成時
------------------
add_fieldsetsを書き換える

編集時
--------------
fieldssets

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
                        #"roles",
                        "is_staff",
                        "is_superuser",
                        "groups",
                        "user_permissions",
                    ),
                },
            ),
            (_("Important dates"), {"fields": ("last_login", "date_joined")}),
        )
        add_fieldsets = (
            (
                None,
                {
                    "classes": ("wide",),
                    "fields": ("username", "password1", "password2",),#"origin_group"
                },
            ),
        )


.. dropdown::  編集すべき場所の探し方

    検索・ドキュメント見てもすぐわからない場合は、
    継承している親クラスを探してみるとわかることがある。

    今回の場合だとdefaultの作成画面で表示される,usernamne,password,password2とadd_fieldsetsの中身が一致してたので
    見つけることができた


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

方法１：urls.pyのadminの属性を変える
------------------------------------

`How to change site title, site header and index title in Django Admin?(stackoverflow) 
<https://stackoverflow.com/questions/4938491/how-to-change-site-title-site-header-and-index-title-in-django-admin>`__


.. code-block:: python
    :emphasize-lines: 4-6
    
    from django.contrib import admin
    ....

    admin.site.site_header="管理画面"
    admin.site.site_title="Title"
    admin.site.index_title="indexだよ"
    # Setup the URLs and include login URLs for the browsable API.
    urlpatterns = [
        path("admin/", admin.site.urls),
        path("o/", include("oauth2_provider.urls", namespace="oauth2_provider")),
    ]

.. note:: 
    
    タイトル表記を変えたいだけならば方法１のほうが簡単


方法2:AminSiteを継承
-----------------------------
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

