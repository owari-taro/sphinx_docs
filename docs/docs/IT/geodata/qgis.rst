==================================
qgis
==================================
-------------
マップ操作
-------------

----------------------
トラブルシューティング
----------------------
属性テーブルが重すぎて開けない！
==================================
事象
--------------
blobでgeotifが16,000近く含まれているテーブルを『属性テーブルを開く』いたときに発生。最終的にはkilledされた

解決策
------------------
とりあえずは属性テーブルを開く前にフィルターでしぼる。ちょっと手間だがこれくらいしか解決策が見つからなかった。

手順
-------------
1. レイヤで右クリックしてフィルタ
2. 条件有力して件数を減らす
3. 属性テーブルを開く

https://gis.stackexchange.com/questions/333705/qgis-slow-on-show-attribute-table-of-a-large-shapefile-and-dies-on-showing-selec