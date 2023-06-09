======
IAM
======



----------------
role
----------------

::
     aws iam create-role --role-name SampleRole --assume-role-policy-document file://policy.json



-----------------
tagによる権限制御
-----------------

* リソースにタグをつけて、identity-policyにtagの条件をつける

::
    aws ec2 create-tags --resources i-0526648a5974cf1c2 --tags Key=Environment,Value=Prod 



* iam userにもtagをつけてリソースのタグと一致するときのみ操作を許す。
(例:project:ABCに参加してる人のみに,ABCで使ってるリソースを操作させたい場合など)
