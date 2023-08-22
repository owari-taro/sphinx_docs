=================
step functions
=================



--------------------
tip
--------------------

作成後すぐに実行するとエラーがでる
=================================

作成後すぐに実行するとエラーがでるので少し待ったほうがいい


SNS連携
====================
attributeの設定
====================
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