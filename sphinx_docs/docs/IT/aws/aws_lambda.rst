====================================
aws lambda
====================================

----------------------
『実践ガイド』まとめ
----------------------
１章
======
lambda制限
-----------

.. glossary::
   
   サイズ制限
     * zipファイルとzip展開時のそれぞれにサイズ制限ある。

       * djangoは向いてない？
       * データ登録とかだけならばok? 
     * コンテナにすれば10GBまで対応。ただlambdaで使えるように実装する必要あり

   最大実行時間
     **15分** 


.. warning:: コンソールでlambda作成してsamをダウンロードしてもトリガーがなぜか反映されていない。本だとコンソール上から作成したものがsamにはんえいされるはずなのだが

第5章
========


::

    #build
    sam build --user-container
    #local test
    sam local invoke -e event/s3-event.json HellloWorldFunction

