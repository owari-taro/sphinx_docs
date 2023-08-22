=============================
AWS Cloud Development Kit
=============================
aws resourceをオブジェクト思考の枠組みでdeployできる仕組み.


----------------
hello world
----------------

sudo apt installでいれるとnodeのveersionが古いため動かない。とかで新しversionにしておく.,→https://qiita.com/cointoss1973/items/c000c4f84ae4b0c166b5

::
  
    npm install -g aws-cdk

    $ cdk --version
    2.69.0 (build 60a5b2a)
    $ aws sts get-caller-identity
    {
        "UserId": "AIDA5COF2NWBT6ATLMNOR",
        "Account": "898599906691",
        "Arn": "arn:aws:iam::898599906691:user/developer"
    }
    $ aws configure get region
    ap-northeast-1
    $ aws configure get region
    ap-northeast-1

    cdk bootstrap aws://898599906691/ap-northeast-1

---------------------------
hello world with lambda
---------------------------

.. https://qiita.com/t-kigi/items/8f9415e857dade8d848d



--------------------------
そのためも
--------------------------
* 3GBが今のところmaxなので巨大すぎるファイルはできない！ https://stackoverflow.com/questions/70943739/aws-lambda-memorysize-value-failed-to-satisfy-constraint






-------------------------
detail
-------------------------

IAM role
==============
* 細かい権限設定は通常のjson形式を読みこめばできてしまう。
  ..https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_iam/README.html」

* 公式documentにも乗ってたのp190あたりの許可の項目
　..https://docs.aws.amazon.com/ja_jp/cdk/v2/guide/awscdk.pdf#getting_started

.. https://github.com/hmrc/lambda-s3-bucket-clamav は古いpython2.7なのでつかわない