=========================
django tips
=========================
djangoのメモ

-------------------------
model関連
-------------------------


..
    https://stackoverflow.com/questions/7250939/in-postgres-how-do-you-restrict-possible-values-for-a-particular-column
    https://stackoverflow.com/questions/30682264/how-to-apply-in-constraint-to-the-fields-of-django-models

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


