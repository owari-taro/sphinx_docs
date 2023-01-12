
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


::

   pip isntall sphinx-autobuild
   sphinx-autobuild . _build/html


.. _theme:

sphinx背景テーマの変更
=========================
`sphinx-themes <https://sphinx-themes.org/>`__ に記載


:: 
   
   pip install cloud-sptheme
   #conf.pyに書き込み↓
   html_theme = 'cloud'


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


画像挿入
=======================
figureディレク底部を使う。画像のパスは↓のように相対パスor/img/*のようにルートディレクトリからのパターン




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


 
clickのドキュメント化
====================
| clickで作ったモジュールは通常の方法だとドキュメント科できない。
| sphinx-clickをインストールしたうえで次を実行する必要がある

1. conf.pyの編集
2. rstファイルの作成し、次のように入力。（通常のmoduleのように自動では生成されないので注意
   
::  

   # 一行目でモジュール名関数名を入力
   #progは表用のラベルなので自由に設定。
   .. click:: hello_world:greet
   :prog: sphinx_click_test
   :show-nested:


docstringの生成
====================
| docstringからhtmlドキュメントを作ることができる。
| **shinx-apidoc** で.pyファイルからrstを生成し、あとはいつもと同様にhtml出力すればよい。

:: 

   #rst生成
   #-o {出力先} {対象dir}
   sphinx-apidoc -f -o ./docs/src  src
   
   #html生成
   ./auto.sh


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