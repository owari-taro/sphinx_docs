==================
CloudFormation(cfn)
==================

------------
hello world
------------

1.環境別でバケット作成
======================
test環境とprd環境のbucketが作れるtemplate.
prod環境には削除保護を付与している。


(1)テンプレートの確認
::

     aws cloudformation validate-template  template-body file://bucket_with_env.yml

(2)テンプレートでスタック作成
::

    $ aws cloudformation update-stack --stack-name my-new-bucket --template-body file://bucket_with_env.yml     

(3)環境変数を入れ替えてupdate実効。 

| **元のバケットは消えてしまう！。**  削除ガードしてないので間違えてきえることがある！！

::

    $ aws cloudformation update-stack --stack-name my-new-bucket --template-body file://bucket_with_env.yml --parameters ParameterKey=EnvironmentType,ParameterValue=prod 

----------------------
reference
----------------------

* `aws docs <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html>`__
* `packt publishing <https://github.com/PacktPublishing/Mastering-AWS-CloudFormation>`__
  