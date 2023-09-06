=================
step functions
=================
---------------------------
basic
---------------------------
Executions
==================
90日が期限で消える（それまでは同じnameは使えない。指定しなければ自動でUUIDが指定される）

--------------------
tip
--------------------
s3連携
==========================
s3からのイベント通知による起動
--------------------------------

objectの作成・タグ作成/更新etc [#]_ でstepfunctionを起動できる。なおタグの中身はinputにでてこないので注意 [#]_

::

    #タグ作成時のinput例
    {
    "version": "0",
    "id": "ceff8539-647a-386e-0251-cb098dfd0422",
    "detail-type": "Object Tags Added",
    "source": "aws.s3",
    "account": "********************",
    "time": "2023-09-05T02:32:07Z",
    "region": "ap-northeast-1",
    "resources": [
        "arn:aws:s3:::{bucket_name}"
    ],
    "detail": {
        "version": "0",
        "bucket": {
        "name": "{bucket_name}"
        },
        "object": {
        "key": "download.svg",
        "etag": "ef71823e383fd23ea6533c8155cd0129"
        },
        "request-id": "C9HBRQFZ0DTZYN4F",
        "requester": "*****************************************",
        "source-ip-address": "***********************"
    }
    }


.. [#] `Supported event destinations <https://docs.aws.amazon.com/AmazonS3/latest/userguide/notification-how-to-event-types-and-destinations.html#supported-notification-destinations>`__ に詳細あり

.. [#] `official docs <https://docs.aws.amazon.com/step-functions/latest/dg/tutorial-cloudwatch-events-s3.html>`__



jsonpath
=====================================

https://github.com/json-path/JsonPath

作成後すぐに実行するとエラーがでる
=================================

作成後すぐに実行するとエラーがでるので少し待ったほうがいい


SNS連携
====================

attributeの設定
----------------------
直接設定用のjsonnに **MessageAttributes** に書き足す必要がある

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

`stack overflow <https://stackoverflow.com/questions/57619197/how-to-pass-jsonpath-to-messageattribute-while-publishing-sns-message-from-a-ste>`__


