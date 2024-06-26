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

concurrency
===============

`AWS公式DOC <https://docs.aws.amazon.com/pdfs/lambda/latest/dg/lambda-dg.pdf#configuration-concurrency>`__

reserved concurrency
-------------------------
* ひとつのruntimeの秒感で処理できるのは10がmax
* 追加のコストはかからない
* defaultで1regionで1000が最大のconcurrency

provisioned cocurrency
----------------------------
* defaultで必要なinitのフェーズを飛ばせて高速化（ただし費用がかかる）
* 関数に割り当てられたprovisioned concurrencyを超えて起動する場合はcold startの環境が使われる。

.. warning::

     | 設定してから使えるようになるまで数分かかる(docのexampleでは5000allocateするのに5分かかかると記載)
     | また設定が完了するまでの間はリクエストを受け付けない

  

同期呼び出し？非同期呼び出し？
==================================
トリガーでことなる `公式 <https://docs.aws.amazon.com/lambda/latest/dg/lambda-services.html#listing-of-services-and-links-to-more-information>`__

`耐久静のある設計 <https://aws.amazon.com/jp/blogs/news/designing-durable-serverless-apps-with-dlqs-for-amazon-sns-amazon-sqs-aws-lambda/>`__


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

image.png
image/2023-08-09-05-50-32.png




