
=====================
sphinx-tips
=====================
---------------------
sphinxとは？
---------------------
python製ドキュメントツール。基本的な使い方は以下のshpinx本とか公式docを参照。



---------------------
よく使う機能の一覧
---------------------
使用頻度高いが忘れそうな機能一覧を記載した。

自動ビルド
=================

毎回コマンドを打つのは面倒なので以下をインストールして実行すれば
rstが保存されるたびにbuildしてくれる

.. code-block:: 

   pip isntall sphinx-autobuild
   #出力dirを指定
   sphinx-autobuild . ../docs/


.. _theme:

sphinx背景テーマの変更
=========================
`sphinx-themes <https://sphinx-themes.org/>`__ に記載


:: 
   
   pip install cloud-sptheme
   #conf.pyに書き込み↓
   html_theme = 'cloud'


サンプル
==================
html-themeの各ページにお手本を参考にすると早い `cloud <https://sphinx-themes.org/sample-sites/cloud-sptheme/>`__ の場合

リンク
======================
外部リンク
-----------

(1)文中に直接埋め込むパターン: `sphinx0-user.jp <https://sphinx-users.jp/>`__ の紹介リンク

.. _amazonjp: https://amazon.co.jp

(2)一旦定義しておいて使い回すパターン: `amazonjp`_

::


   (1)
   `sphinx0-user.jp <https://sphinx-users.jp/>`__ の紹介リンク  
   
   .. _amazonjp: https://amazon.co.jp
   (2)一旦定義しておいて使い回すパターン: `amazonjp`_


リンク先を新タブで開く
_______________________
デフォルトではクリックしても新タブで開かれない。新タブで開くには以下の設定が必要
(`stackoverflow <https://stackoverflow.com/questions/11716781/open-a-link-in-a-new-window-in-restructuredtext>`__ )

:: 
   
   #conf.py
   html_js_files = [
     'js/custom.js'
   ]

_static下にjsフォルダを作成し、custom.jsに以下をコピペ保存
:: 

   #_static/js/custom.js
   $(document).ready(function () {
    $('a.external').attr('target', '_blank');
    });



.. _internal_link:

内部リンク
-----------
sphinxドキュメント内でのリンク: :ref:`theme` 

::

  #一行開ける（）
  .. _theme:

  sphinx背景テーマの変更
  =========================   
  
  :ref:`theme` 


注釈
=============
番号指定
---------

sphinx [1]_ を使うにはpython [2]_ をインストールしてください

.. [1] 脚注１
.. [2] 脚注２

::

   sphinx [1]_ を使うにはpython [2]_ をインストールしてください

   .. [1] 脚注１
   .. [2] 脚注２


番号自動指定
------------
注 [#]_ の番号を自動にすることもできる [#]_

.. [#] 注のテスト
.. [#] またテスト

::
      
   注 [#]_ の番号を自動にすることもできる [#]_

   .. [#] 注のテスト
   .. [#] またテスト



名前指定
-----------
sphinx [#sphinx]_ を使うにはpython [#python]_ をインストールしてください

.. [#sphinx] sphinxについて下記kます
.. [#python] pythonについて書きます 

:: 
      
   sphinx [#sphinx]_ を使うにはpython [#python]_ をインストールしてください

   .. [#sphinx] sphinxについて下記kます
   .. [#python] pythonについて書きます 



画像挿入
=======================

figure-directiveを使う。画像のパスは↓のように相対パス or /img/* のようにルートディレクトリからのパターン



:: 
   
   .. figure:: img/kiddykong.jpg

      お猿さん

.. figure:: img/kiddykong.jpg

   お猿さん




conf.pyに以下を記述しておくと図番号が表示される
:: 

   numref=True


:ref:`internal_link` を組み合わせれば画像にもリンクができる。
:numref:`kong` みたいに


.. _kong:

.. figure:: img/kiddykong.jpg

   （もう一回）お猿さん



::
  
  :numref:`kong` みたいに

  .. _kong:

  .. figure:: img/kiddykong.jpg

jupyter連携
================

todo etc
==============

todo
-----------

 .. todo:: ここにtodoを書く

.. todo:: 

   | 改行してかくこともできる
   | ここで改行

**conf.py** に次を設定し、
::

   todo_include_todos=True
   extensions = ['sphinx.ext.todo' ]



rstファイルでtodoを次のように書く
::

    .. todo:: ここにtodoを書く

   .. todo:: 

      | 改行してかくこともできる
      | ここで改行


warning
------------
書き方はtodoと同じく。conf.pyに指定はいらない。`参考 <https://sphinx-themes.org/sample-sites/cloud-sptheme/kitchen-sink/admonitions/>`__


.. warning:: ここに注意


::

   .. warning:: ここに注意


.. warning::
   | 複数行も書けるかの？
   | どういうことだ？
   
   ::

      from aws_cdk import (
      # Duration,
      Stack,
      aws_s3,
      RemovalPolicy,
      )
      class LoadS3Stack(Stack):

         def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
            super().__init__(scope, construct_id, **kwargs)
            bucket = aws_s3.Bucket(
                  self,
                  "test_for_trigger_lambdad",
                  removal_policy=RemovalPolicy.DESTROY,  # Stack削除と同時にバケットを削除する
            )



::

   .. warning::
   | 複数行も書けるかの？
   | どういうことだ？

.. error:: ここに注意


::
  
  .. error:: ここに注意

表の挿入
=================

.. csv-table:: exampleテーブル
   :file: csv/example.csv

csvファイルをからテーブルを作成
::

   .. csv-table:: exampleテーブル
      :file: csv/example.csv   

直接書きたい場合は
::
      
   .. csv-table:: exampleテーブル
      :header-orws: 1

      id,name
      1,Taro
      2,Trump
      3,Biden


conf.pyに↓を書いておく表に番号が自動で入る。
::

   numref=True



clickのドキュメント化
======================

| clickで作ったモジュールは :ref:`docstring` だとdocumentの生成ができない。
| sphinx-clickをインストールしたうえで次を実行する必要がある

1. `sphinx-lik <https://sphinx-click.readthedocs.io/en/latest/usage/>`__ のinstall

::

   pip isntall sphinx-click

2. conf.py編集
::

   extensions = ['sphinx_click']


3. rstファイルの作成し、次のように入力。（通常のmoduleのように自動では生成されないので注意
   
::  

   # 一行目でモジュール名関数名を入力
   #progは表用のラベルなので自由に設定。
   .. click:: hello_world:greet
   :prog: sphinx_click_test
   :show-nested:

django-clickの場合などネストしている場合はパスを **.** でつないで各必要がある

::  

   # 一行目でモジュール名関数名を入力
   #progは表用のラベルなので自由に設定。
   .. click:: management.commands.hello_world:greet
   :prog: sphinx_click_test
   :show-nested:

.. error:: 読み込みでエラーがでたときはsys.path使ってどこまでパスが通っているかを確認する

.. _docstring:

docstringの生成
====================
**shinx-apidoc** でdocstringからドキュメントを作ることができる。


1. conf.pyの編集

.. code-block:: python

   import os
   import sys
   sys.path.insert(0, os.path.abspath('../src'))
   #必要に応じてparentdirも追加しておく
   #sys.path.insert(0, os.path.abspath('../../'))


   extensions = [
    # docstringからドキュメント生成
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon"

2. コマンド

.. code-block:: shell

   #rst生成
   #-o {出力先} {対象dir}
   sphinx-apidoc -f -o ./docs/src  src
   
   #html生成 
   ./auto.sh
   #もしくは
   make html


comment out
=======================
comentoutは **..** にスペースをつけて書けばよい


.. aoiifasdf
   adslkjfalkdfalsd


::

   ..  adfasdfasd;aksdjflaskjflkasjdasd
      fdfl;l;lkjadflkasdflkjasdl
      


github noteとの連携
============================
* hoge


.. epigraph::

   No matter where you go, there you are.

   -- Buckaroo Banzai



.. compound::

   The 'rm' command is very dangerous.  If you are logged
   in as root and enter ::

       cd /
       rm -rf *

   you will erase the entire contents of your file system.

checkbox
==========================
markdownみたいなチェックボックスが作れる

.. todo:: This is a checkbox example.

   - [ ] Unchecked item
   - [x] Checked items

::

       'sphinx_markdown_checkbox',



ソースコードファイルを読み込む
==============================
ソースコードファイルを直接読見込んで表示できる。 **languge** はoptional.

::
    
   .. literalinclude:: ./sphinx_dummy.py
      :language: python



.. literalinclude:: ./sphinx_dummy.py
   :language: python

code表示
=============

特定の行だけ協調したい
-------------------------
下のようにcode-blockディレクティブをつかって emphasize-linesを使う。ファイル形式は特に指定しなくてもできる（yaml,pythonなど）

::

      
   .. code-block:: yaml
      :emphasize-lines: 7-12

      {
      "Type": "Task",
      "Resource": "arn:aws:states:::sns:publish",
      "Parameters": {
         "Message.$": "$",
         "TopicArn": "arn:aws:sns:ap-northeast-1:**********:MyTopic",
         "MessageAttributes": {
         "env": {
               "DataType": "String",
               "StringValue": "dev"
         }
      }
      },
      "End": true
      }


.. code-block:: yaml
    :emphasize-lines: 7-12

    {
    "Type": "Task",
    "Resource": "arn:aws:states:::sns:publish",
    "Parameters": {
        "Message.$": "$",
        "TopicArn": "arn:aws:sns:ap-northeast-1:**********:MyTopic",
        "MessageAttributes": {
        "env": {
            "DataType": "String",
            "StringValue": "dev"
        }
    }
    },
    "End": true
    }


------------------
Error解決
------------------

buildエラー
=========================
venvを使ってるならconf.pyからexcludeしておく
https://github.com/sphinx-doc/sphinx/issues/2066



--------------------------------------------------------------------------------------------------
`sphinx-design <https://sphinx-design.readthedocs.io/en/pydata-theme/index.html>`__
--------------------------------------------------------------------------------------------------
::

   pip  install sphinx-design


tab
=======================

.. tab-set::

    .. tab-item:: patternA

        **このように** なります

    .. tab-item:: Pattern2

        違いがわかります？

書き方↓。ちなみに `mkdocsの場合 <https://squidfunk.github.io/mkdocs-material/reference/content-tabs/#c_1>`__

::

   .. tab-set::

    .. tab-item:: Label1

        Content 1

    .. tab-item:: Label2

        Content 2

dropdown
===========

.. dropdown:: ドロップダウンだよ

    | 中身はこんな風です
    | **太字とか** も普通につかえるよ 
