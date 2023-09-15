======================
日記
======================
技術関連ITなどのことについてのメモとか日記のようなもの

-------------------------------
2023/8
-------------------------------

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
--------------------------
sourceコードをreplから見る方法。デバッグしたいときにその場で見れる
https://maku77.github.io/p/xbucsaq/

::

    >>> import inspect
    >>> import os
    >>> print(inspect.getsource(os.path.abspath))
    

documentツール
--------------------------
とりあえずmkdocsも触ってみた感想

mkdocsのいい点
__________________________
* クラスメソッドなどはsphinxじゃなくて、mkdocsを社内で使ってるよう。markdownのほうがrstより使い慣れている人が多いからとかいう記載があった
* 両方使ってみたが、themeの多さはsphinxのほうが強いところか、
* materialのtab表示は便利かなと思う [#]_
* ただsphinxで書いてしまった既存documentを移行するのはそれなり大変そうではある

.. image:: img/mk_tab.png
  
.. [#] shpinxも一応materialがthemeとして存在しているが、このタブ機能はないっぽい


sphinxのほうがいい点
__________________________
* themeの多さはsphinx
* ナイトモードがあるthemeがあるのもsphinx
* 長く使われてるライブラリはsphinxが多い印象django/pytest/celery etc


restframework
--------------------------
* viewsetで書いてみたが確かに省略できるようにはなるのだが、たまにしかいじらない場合わかりにくい
* 初心者に少しやりにくさがある
* django-ninjaとかfastapiのほうが直観的でわかりやすい

django-adminの二要素認証
--------------------------
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


2023/8/22
=====================
documentツール
----------------------------
* sphinxの公開をread-the-docsに移行した。mkdocsですでに実施していたので同じ要領ですぐできた
* `ray <https://docs.ray.io/en/latest/>`__ のドキュメントがいい感じだったので調べたらsphinxせいだった
* rayは `mystmd <https://mystmd.org/guide/dropdowns-cards-and-tabs>`__ 使ってmarkdownで書かれていた.
* sphinxだと最新に対応してないライブラリとかthemeが意外とおおかった

2023/8/23
=======================
.. todo::  読んでおくと良さそうなdocument

  | https://docs.python.org/3/library/multiprocessing.html
  | https://docs.python.org/ja/3/library/queue.html
  | https://docs.geoserver.org/latest/en/user/



* queue.put(1,block=False) のblockの意味
* mp.async_map()のasync_mapとか



2023/8/24
===============================
documentツール
----------------------------
* sphinxでsvgを表示する方法

https://stackoverflow.com/questions/34777943/insert-clickable-svg-image-into-sphinx-documentation


.. todo:: 
  https://numpy.org/doc/stable/reference/generated/numpy.ndarray.view.html

2023/8/30
========================

documentツール
-----------------------
* fluent-pythonのサイトをみたらたまたま見つける、goで書かれているらしいが、ちょっとマイナー（？）

aws
--------------------
* s3で大量のファイルをアップロードするとき（合計40GB）を送るとき、aws-cli のcp recursiveでするのが一番早かった。
* aioboto3で非同期にすれば早いかと思ったが、awscliのほうがファイス数が増えるにしたがって早くなっていった。
* 

.. todo::  

  aws s3 cpのrecursiveの実装を確認してみる.
  さっとgithubで検索してみたがすぐにはわからなかった・・・・

fluent python
-------------------
* 前記のuploadの速度に関連して fluent pythonを読んでいたら `httpx <https://www.python-httpx.org/async/>`__ なるlibraryが記載されていた
* requetsと違って、asyncにも対応しているらしく良さそうなので試してみる 
* ちなみにドキュメントはmkdocsで書かれていた。

その他
----------------
これを書いているときちょうどsphinxのvscode previewが一時的に↓のようなエラーがでて
previewが使えなくなったが、.vscode/settings.jsonから **,** がぬけてjsonが壊れていたのが原因だった。
* vscodeのextentionのとかやったが関係なかった・・・

::

  command restructuredtext.showpreviewtoside not found


2023/8/31
==================


fluent python
--------------

tqdm
______________
* for文などののprogressbarに使えるtqdmが参考になった。見た目もきれいなのでよい
* コマンドラインに-vで詳細をだすかなども参考になった。
  pytestなどにも使われていることを思い出した。
  コマンドラインツールで適度に表示を出す方法として使えそう

.. code-block:: python
  
  from tqdm import tqdm
  import time

  for i in tqdm(range(100)):
      time.sleep(1)
  #100%|██████████| 100/100 [01:40<00:00,  1.00s/it]

POSTGIS
---------------
* 不正なポリゴンをなおすのにst_buffer(geom,0)で解決ができることがある。ちょうど8の字がたになっているときに、使えるらしい・・・
  一応オフィシャル `document <https://postgis.net/documentation/manual/>`__ [#]_ にも次のような記載がある

::


  e input object is much larger than a UTM zone or crosses
  the dateline Buffer output is always a valid polygonal geometry. 
  Buffer can handle invalid inputs, so buffering by distance 0
  is sometimes used as a way of repairing invalid polygons.
   can also be used for this purpose. Buffering is sometimes used to
  perform a within-distance search. For this use case it is more efficient to use .
   This function ignores the Z dimension. It always gives a 2D result even when used on a 3D geometry.


.. [#] 詳細理由はよくわかってない。ただドキュメント自体は900p近くあってかなりしっかりしてるので読む価値はありそう。例えばspatial indexなどは
       geodjangoまかせで使ってるのでいいかも


----------------------------
2023/9
----------------------------


2023/9/1
=========================

QGIS
------------------------------
*  単純にintersectsとりたいだけならqgisのほうがよい。map上での確認もできるのでミスにも気づきやすい。 `参考 <https://gis.stackexchange.com/questions/18453/create-a-new-layer-from-overlap-between-two-layers>`__



2023/9/2
====================
fluent python
-----------------
* pythonの実装見たいときは `cpython <https://github.com/python/cpython>`__ を参照するといい
* 

2023/9/4
===========================
fluent python
-------------------
* dict/listなど直接継承すると一貫性のない動作をすることがある。 `pypy <https://doc.pypy.org/en/latest/cpython_differences.html#subclasses-of-built-in-types>`__ 記載の例だと



.. code-block:: python

    class D(dict):
    def __getitem__(self, key):
        if key == 'print':
            return print
        return "%r from D" % (key,)

  class A(object):
      pass

  a = A()
  a.__dict__ = D()
  a.foo = "a's own foo"
  print(a.foo)
  # CPython => a's own foo
  # PyPy => 'foo' from D

  print('==========')

  glob = D(foo="base item")
  loc = {}

   
aws
--------------------
* s3のevent通知はtag変更とかでもできる `Supported event destinations <https://docs.aws.amazon.com/AmazonS3/latest/userguide/notification-how-to-event-types-and-destinations.html#supported-notification-destinations>`__


2023/9/5
======================
aws
-------------------------
* ルートテーブルとAClの違いは何かとふと思ったが、 `stackoverflow <https://stackoverflow.com/questions/60211533/what-is-the-diference-between-network-acl-and-route-tables-in-aws>`__ が参考になった
* cloud9はprivate subnetでも使える。gatewayのせっていが必要 `参考 <https://www.bioerrorlog.work/entry/private-subnet-cloud9>`__]


python
----------------------------
* offline環境でpythonのversionを上げようとして、最初pyenvを検討したが一番らくなのは公式のtgzをコンパイルインストールする形式っぽい `参考 <http://infra-se-no.blog.jp/archives/16962028.html>`__ [#]_ 


::

      #https://www.python.org/ftp/python/
      #tar xvzf Python-3.8.0a1.tgz

      #cd Python-3.8.0a1

      #./configure --prefix=/usr/local/python

      #make

      #make install

      #vi ~/.bash_profile 

      export PATH=$PATH:〜〜〜〜〜〜の後ろに「:/usr/local/python/bin」を追記して保存する。

      #ln -s /usr/local/python/bin/python3 /usr/local/bin/python

      #python




.. [#] オフライン下でのpyenvも詳細に書かれたblogがあったが手順が長すぎて断念した



2023/9/6
===============================

消去したユーザーがオーナーのリソースの扱い方
--------------------------------------------------
created_byで指定されたユーザーを消したとき、messageを残しておくべきかという問題。

::

    #イメージ
    class Message(Model):
        created_by=models.ForeignKey(User...
        message=models.CharField(max_length=250,.....


| チャットツールとかだと(teamsとか)削除されたユーザーもメッセージは残している。残さないと会話の意味とかが分からなくなるからだろう。
| ただしこの場合削除されたユーザーが再度登録した場合(emailがユニークかつ必須の条件のとき)どのように扱えばいいのかがちょっと謎。
| 削除フラグかつ同じemailがあるときは再登録できるようにコマンドを変えてあげればいいのだろうか？
 

`参考 <https://ux.stackexchange.com/questions/10329/whats-the-best-way-to-handle-deleted-user-accounts-on-a-social-app>`__



2023/9/7
===================================================
code-commitのクロスアカウントでの使用
--------------------------------------
vpc endpointを使えばできる、ただグループポリシーとかの指定があると引っ掛かるかの静画あるぞ



2023/9/10
==========================

コンテナセキュリティ
-----------------------

* コンテナ側もホストと同じOSを共有している.『共通のOSで別のディスとリビューしょんを動かしているようにふるまっているだけ・・・』[#]_ 
 

::

    docker run --rm -it fedora:38 /bin/bash

    [root@53ccc165b45b /]# uname -a
    Linux 53ccc165b45b 5.15.90.1-microsoft-standard-WSL2 #1 SMP Fri Jan 27 02:56:13 UTC 2023 x86_64 GNU/Linux



.. [#] `基礎から学ぶコンテナセキュリティ<https://gihyo.jp/book/2023/978-4-297-13635-2>`__

* alpineの場合はbashでなくash
::

    docker run -it --rm myimage:test  /bin/ash

.. todo:: 

  docker公式のsecurityの項目読んでおく
  https://docs.docker.com/develop/security-best-practices/#check-your-image-for-vulnerabilities


2023/9/11
===========================
aws
------------------
gateway endpoint設定してもs3に接続できない(access denied)
_____________________________________________________________________
* 最初はec2のロールが不足していたので、s3fullacessをロールにたしてみたが、変わらなかったので再起動したが変わらず。
* デフォルトで適用されている一時クレデンシャルを無効化したらできた [#]_ 
  
.. [#]  https://www.yamamanx.com/cloud9-default-setting-access


cloud9でlocalアップロードしたファイルがunzipできない
_______________________________________________________

* s3からブラウザ経由でダウンロードして、cloud9のlocalファイルのアップロードをおこなったファイルだとなぜかunzipできない
* 結局,s3から直接cliでダウンロードしたら問題なくunzipできた。

trend-micro cloud oneのエイリアス設定
_________________________________________
| 圧縮されたファイルに含まれるファイル数の上限設定時にエイリアスに反映する必要があるが、デフォルトで設定されているエイリアス名をversioningで更新する必要がある
| ドキュメントにははっきり書いていなかったので、新しくエイリアスを作っていた




  
2023/9/12
====================================

aws
--------------------------
awscliが使えない
_________________________________________

pythonのpipように使ってるproxy環境変数を消したら使えるようになった。NO_PROXYで指定しているのだがなぜかよくわからない

::

    export -n http_proxy
    export -n https_proxy
    
    export NO_PROXY=169.254.169.254


cloud9のdiskが足りない
__________________________
https://blog.proglus.jp/4574/ の記載の通りinstanceをいったん停止してec2 consoleからdiskを増やしただけで、root voluemeが増加する。（ubunuで試した）




2023/9/15
=======================================
django unittestが失敗
---------------------------------
**django.db.utils.ProgrammingError: permission denied to create extension "postgis"** で失敗する。
unittest字に別のデータベースを作るときにpostgisをinstallする権限がないのが原因、
とりあえずtemplate1にpostgisを追加するようにしたら動いた。

https://stackoverflow.com/questions/35209013/testing-django-app-with-postgis-backend
https://postgresweb.com/what-is-template1

.. todo:: 
  
    django `公式docのテスト <https://docs.djangoproject.com/en/4.2/topics/testing/overview/>`__ を見ておく  


unittestのpatchについて
----------------------------
いままで各テストでmockのdecoratorを使っていたが、
全部のTestClassのすべてのテストケースで使うような場合だったら、pytestのfixtureにまとめてしまったほうが見やすい。[#]_

またpytest-mock使えばimportせず似たように使える。



`stack-overflow <https://stackoverflow.com/questions/59045200/proper-way-to-return-mocked-object-using-pytest-fixture>`__ のコード例
.. code-block:: python

    @pytest.fixture()
    def mocked_worker():
        with patch('test.test_module.os.getcwd', return_value="Testing"):
          result = Worker()
          yield result



.. info::

  effective pythonのmockクラスとpatchの使い分けも参考になる。



.. [#] djangoアプリで、setupとして(1)token取得(2)自分のユーザー情報取得してから、各エンドポイントをテストする必要があったが、毎回mockを書くのもめんどくさかったので探したらみつかった
