=======================
django-database
=======================

-----------------
制約
-----------------
* test

文字列の種類の制限
======================

https://stackoverflow.com/questions/44341153/force-charfields-choices
clean()に書けばできる



-------------------------
model関連
-------------------------
..
    https://stackoverflow.com/questions/7250939/in-postgres-how-do-you-restrict-possible-values-for-a-particular-column
    https://stackoverflow.com/questions/30682264/how-to-apply-in-constraint-to-the-fields-of-django-models


テーブル制約を入れたい
==============================
日付制約
===============

.. code-block:: 

    





テーブル名を指定したい
==========================
**Meta** クラスを作ってdb_tableで指定する
::

    from django.db import models
    class Employee(models.Model):
        first_name = models.CharField()
        last_name = models.CharField()

        class Meta:
            db_table = '従業員'             # テーブル名：'従業員

複合ユニーク制約
=====================
Metaクラス内にconstraintsを指定する。複数指定も可能。

::


    class Lesson(models.Model):
    """レッスンモデル(生徒が同日に同じ先生のレッスンを受講できるのは1回まで。)"""

    teacher = models.CharField("先生", max_length=50)
    student = models.CharField("生徒", max_length=50)
    date = models.DateField("レッスン実施日")

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["teacher", "student", "date"],
                name="lesson_unique"
            ),
        ]





choiceで指定した文字列以外を禁止したい
===============================================
下のコードのようにMetaクラス内に **CheckConstraint** 制約を入れる
::

    class Status(models.TextChoices):
        """_summary_

        :param _type_ models: _description_
        """

        finished = "finished"
        waiting = "waiting"


    class Project(models.Model):
        """_summary_

        :param _type_ models: _description_
        """

        pid = models.CharField(max_length=250)
        step_num = models.IntegerField()
        status = models.CharField(choices=Status.choices, max_length=250)
        created_at = models.DateTimeField(auto_now_add=True)

        class Meta:
            constraints = [
                models.UniqueConstraint(fields=["pid", "step_num"], name="lesson_unique"),
                models.CheckConstraint(
                    name="%(class)s_status_check",
                    check=models.Q(status__in=Status.values),
                ),
            ]

なおpostgrews状で生成される制約は次のようになる。
::

    #postgres内に作られる制約(\d {table名}で確認できる)
    "project_status_check" CHECK (status::text = ANY (ARRAY['finished'::character varying, 'waiting'::character varying]::text[]))


migrationを戻したい
====================
間違えてmigrateしてしまった時などには,

1. showmigrationsで戻したい個所を確認して
2. migrate {migrate_name}
3. 間違えて生成したマイグレーションファイルを削除


::
    
    python manage.py showmigrations
    admin
    [X] 0001_initial
    [X] 0002_logentry_remove_auto_add
    [X] 0003_logentry_add_action_flag_choices
    auth
    [X] 0001_initial
    [X] 0002_alter_permission_name_max_length
    [X] 0003_alter_user_email_max_length

    :~/git_repos/database/sample_dj$ python manage.py migrate sample 0015_rename_prc_amt_prc


raw-sqlで使用したい
===================





安全なmigrationしたい
======================
意図せぬmigrateを避けるために、migrate実行前に次の二点を確認する。

1. 実行されていないmigration
2. 1のmigrationの具体的な中身
  
.. caution::
    
   | makemigrationsしていないのにmigrateしてしまうということがある。
   | この現象はdjango-authtoolkitのverを切り替えたときに発生した。
   | 古いverではsecret_idを平文でdbに保存していたのがhash化されて保存されるように仕様が変わったのだが
   | この変更はmakemigrationsしていなくてもmigrateコマンドに含まれるため、意図せずmigrationが実行されてしまうのだ。
   


.. code-block::
    
    python  mamage.py makemigratins {app}



存在しないなら404
==========================

::

    from django.shortcuts import get_object_or_404
    #Userのところに対象のモデル
    get_object_or_404(User, pk=id)



-------------------------
関連ライブラリ
-------------------------
django-auth-toolkit
=====================
* `公式 <https://django-oauth-toolkit.readthedocs.io/en/latest/>`__

* **[2.2.0] 2022-10-18** からclient_secretはhashedされて保存されるようになったので注意。
   
   * 以前のversionから使っている場合はmigrateすればdbに保存されているsecretをhash化してくれる
   * 2.2.0以降から使う場合は特に対応の必要はない
  
The application client secret is now hashed upon save. You must copy it before it is saved. Using the hashed value will fail.