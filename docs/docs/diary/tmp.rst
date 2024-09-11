# djangoのvalidagtors
saveにfull_cleanをいれないとvalidatorsで指定した関数が実行されなかった（詳しいことはあとでdocumentをよんでみる）



::

      
  def restrict_num_per_group(group_pk: int):
      # https://stackoverflow.com/questions/24586223/limit-number-of-foreign-keys
      #full_cleanも追加する
      if TableA.objects.filter(group_id=group_pk).count() > 200:
          raise ValidationError(
              "モニタリングポイントの登録上限に達しました。既存のモニタリングポイント削除してから新規登録してください。"
          )
  
  
  class TableA:
      """モニタリングポイント（登録されたファイル単位）"""
      group = models.ForeignKey(
          "Group",
          on_delete=models.CASCADE,
          related_name="table_A",
          validators=(restrict_num_per_group,),
      )

  
    def save(self, force_insert=False, force_update=False, using=False, update_fields=None):
        self.full_clean()
        super(TableA, self).save()

