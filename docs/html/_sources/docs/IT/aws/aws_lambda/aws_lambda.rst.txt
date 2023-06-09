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




lambdaでs3のウィルスチェック
===============================

-------------------
その他
-------------------
trigger
==============
各トリガーのcontextに入るjsonの形式。


s3
-------------
::

  >>> evnet
  {'Records': [
    {'eventVersion': '2.1', 'eventSource': 'aws:s3', 'awsRegion': 'ap-northeast-1', 
  'eventTime': '2023-03-23T06:31:22.820Z', 'eventName': 'ObjectCreated:Put', 'userIdentity': {'principalId': 'AWS:AIDA5COF2NWBT6ATLMNOR'}, 'requestParameters': {'sourceIPAddress': '106.72.128.33'}, 'responseElements': {'x-amz-request-id': 'QWN8QPQG1ZCA28QM', 'x-amz-id-2': '1XWSYH1khYfZ7HX6u7q45+jdEzwgryPsnio+6pPl1yyeTW93E/Nm3zKAGNxUo4iGEREkK2tqlF9OxgP9Ia6XPUChocmLhAmS'}, 
  's3': {'s3SchemaVersion': '1.0', 'configurationId': 'e1f29ecc-ed48-4821-afda-b42471705b7d', 
  'bucket': {'name': 'hoge-geho-hoge', 'ownerIdentity': {'principalId': 'A698S378X0F02'}, 
  'arn': 'arn:aws:s3:::hoge-geho-hoge'}, 
    'object': {'key': 'img001.pdf', 'size': 1038579, 'eTag': 'a7940f79cf17d3bec1f424a037ac5cfc', 'sequencer': '00641BF23AA80C6788'}}}]}

  >>> event["Records"][0]["s3"]["bucket"]
  {'name': 'hoge-geho-hoge', 'ownerIdentity': {'principalId': 'A698S378X0F02'}, 'arn': 'arn:aws:s3:::hoge-geho-hoge'}
  
  >>> event["Records"][0]["s3"]["object"]["key"]
  'img001.pdf'