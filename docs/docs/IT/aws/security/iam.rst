======
IAM
======


---------------
role/policy/IAM
---------------

role
=====================


 image/2023-06-27-16-26-49.png

::
    
     aws iam create-role --role-name SampleRole --assume-role-policy-document file://policy.json

権限管理
==================

--------------------
権限の管理方法
--------------------

tagによる権限制御
=====================


::
    aws ec2 create-tags --resources i-0526648a5974cf1c2 --tags Key=Environment,Value=Prod 



* iam userにもtagをつけてリソースのタグと一致するときのみ操作を許す。
(例:project:ABCに参加してる人のみに,ABCで使ってるリソースを操作させたい場合など)

master/manager方式
==================

権限を作成・変更・削除するロールと各リソースにアタッチできるロールを分ける方法

