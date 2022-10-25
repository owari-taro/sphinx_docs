.. intro documentation master file, created by
   sphinx-quickstart on Tue Oct 25 00:43:45 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.
=================================
Welcome to intro's documentation!
=================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:



------------------------
tips
------------------------
よく使う機能の一覧


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
---------------------
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
