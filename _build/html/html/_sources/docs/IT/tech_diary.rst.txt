======================
技術日記
======================
技術関連ITなどのことについてのメモとか日記のようなもの

2023/7/31
===========================
* `aws workshop <https://catalog.us-east-1.prod.workshops.aws/workshops/2e48b9fc-f721-4417-b811-962b7f31b61c/en-US>`__ のcloudtrail目次だけ見る。良さそうなので時間見つけてやる
* テーブルの部分dumpでてこずる。日付のフォーマットがちがうとなってたが、どこが違うのかわからんかったのえ
  insert文をdjモデルと使って書く。（あまり効率的なやり方ではなさそうだが）

::
    f"insert into {table} ...{record.id},"


  geometryがはいると4,5GBになることも普通なので効率的なやりかた考えたほうがいい

* instanceに入れないレスポンス返さなくなったらalarm使ってインスタンスの再起動をするようにしたほうがいい
* aws backupが意外と中国本土のregionで提供されてない機能が多い


2023/8/3
===================
* pydanticをさわる、fastapi[all]でいれるとveresion2じゃなかった


2023/8/5
=======================
wslでvscodeが起動できなくなる。/etc/wsl.confをenable=Falseにして
wslを再起動すると解決した

https://github.com/microsoft/WSL/issues/8952



2023/8/16
==================

* target groupのtargetがすべてunhealthyだと普通にリクエストするらしい
  
  aws docの原文を最初読んだときは意味がわからなかったが、

  `class method blog <https://dev.classmethod.jp/articles/tsnote-alb-targetgroup-unhealthy-002/>`__


2023/8/17
=================

`django-ninja <https://django-ninja.rest-framework.com/>`__
-------------------------------------------------------------
* django pydanticで検索してたらたまたま見つける
* fastapiのようなinterfaceを備えたdjangoAPIを作れるツール。fastapi使いたいけどdjango-modelになれた人にとってはかなり使いやすそう
* 日本語でのページは少なく、まだ日本では広まってない？
* localで試そうとしたがなぜか表示がうまくいかず・・・・・
* restframeworkよりは気軽に書けそう
  

::

    from django.contrib import admin
    from django.urls import path
    from ninja import NinjaAPI

    api = NinjaAPI()

    @api.get("/add")
    def add(request, a: int, b: int):
        return {"result": a + b}


    urlpatterns = [
        path("admin/", admin.site.urls),
        path("api/", api.urls),
    ]


documentツール
-----------------
* fastapiやninjaのdocumentが同じ形式だったので調べたらはmkdocsで作られている
* 独自markdownでかけるのは、マイナなrst使うsphinxより強味かもしれない
* `sphinx theme<https://sphinx-themes.org/>`__ を見ていると同じようなのがだいたいそろってるのでoutputとしてそんなに変わらないかも

python multiprocess
--------------------
* chunk sizeについて `stack over flow <https://stackoverflow.com/questions/3822512/chunksize-parameter-in-multiprocessing-pool-map>`__

2023/8/18
=================
debug
==========
sourceコードをreplから見る方法。デバッグしたいときにその場で見れる
https://maku77.github.io/p/xbucsaq/

::

    >>> import inspect
    >>> import os
    >>> print(inspect.getsource(os.path.abspath))
    

documentツール
=================
とりあえずmkdocsも触ってみた感想

mkdocsのいい点
-----------------------
* クラスメソッドなどはsphinxじゃなくて、mkdocsを社内で使ってるよう。markdownのほうがrstより使い慣れている人が多いからとかいう記載があった
* 両方使ってみたが、themeの多さはsphinxのほうが強いところか、
* materialのtab表示は便利かなと思う [#]_
* ただsphinxで書いてしまった既存documentを移行するのはそれなり大変そうではある

.. image:: img/mk_tab.png
  
.. [#] shpinxも一応materialがthemeとして存在しているが、このタブ機能はないっぽい


sphinxのほうがいい点
-------------------------------
* themeの多さはsphinx
* ナイトモードがあるthemeがあるのもsphinx
* 長く使われてるライブラリはsphinxが多い印象django/pytest/celery etc


restframework
===============
* viewsetで書いてみたが確かに省略できるようにはなるのだが、たまにしかいじらない場合わかりにくい
* 初心者に少しやりにくさがある
* django-ninjaとかfastapiのほうが直観的でわかりやすい

django-adminの二要素認証
==========================
* `django-admin-two-factor-auth <https://django-admin-two-factor-auth.readthedocs.io/en/latest/>__`
* google-authenticatorを使っている、設定自体は簡単だがinstalled_appの書き順があるらしく、それを間違えていて手間取った。
* docで目立つように↓みたいに書いてくれたらよいのだが・・・・
* docを読む限り強制するとかはできないっぽい

.. warning:: 
    
    順番注意

2023/8/19
==========
documentツール
---------------
* docstringからの出力機能はmkdocsのほうが見やすい感じをsource-code自体もオンオフ表示できたりと
  使いやすい印象を受けた
* autonumberingがないのはmkdocsのマイナス
