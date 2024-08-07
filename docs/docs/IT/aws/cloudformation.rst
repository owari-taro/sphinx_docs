============================
cloudformation
============================

------------------
tutorial
------------------
まずはvpc/private&public　subnet/InternetGateWay(IGW)をcloudformationを使って作ってみる。


VPCの作成
==============================
まずはcloudformationを使ってVPCだけを作る。

templateの作成
---------------------------
まずは作りたいVPCの設定を記載したtemplateを作る。templateはyaml/jsonのいずれかに対応している・
::  
   
    AWSTemplateFormatVersion: 2010-09-09
    Description: Template for VPC
    
    Resources:
      CFnVPC:
        Type: AWS::EC2::VPC
        Properties:
          CidrBlock: 10.0.0.0/16
          InstanceTenancy: default
          EnableDnsSupport: true
          EnableDnsHostnames: true
          Tags:
            - Key: Name
              Value: cfn-t

.. attention::

   regionはtemplate内では指定できない。.aws/configのregionで指定する(`参考 <https://serverfault.com/questions/1103642/how-to-specify-aws-region-in-cloudformation-vpc>`__)



スタック作成
---------------------------

:: 

  $ aws cloudformation create-stack --stack-name test --template-body file://vpc.yaml 

スタックの削除
-----------------------------
作成したリソースを削除したい場合は↓のコマンドで削除できる。実行しても特に標準出力には何も表示されない。

::
  
    aws cloudformation delete-stack --stack-name test

subnet/internetgatewayなどを追加
===================================================



TransferFamily(おまけ)
=================================================
おまけとしてTransferFamilyを追加する。

.. attention:: 

   stopしただけでは料金が課金されつづけるので要注意！！！！

secret managerからsecret情報の取得方法
=================================================
下記の形式で記載すれば取得できる ( `公式ドキュメント <https://docs.aws.amazon.com/secretsmanager/latest/userguide/cfn-example_reference-secret.html>`__)

* secret-id以外はオプショナル

::

      {{resolve:secretsmanager:secret-id:SecretString:json-key:version-stage:version-id}}



----------------------------
参考文献
----------------------------
`【初心者向け】AWS CloudFormation で VPC を構築する
 <https://staff-blog.faith-sol-tech.com/%E3%80%90%E5%88%9D%E5%BF%83%E8%80%85%E5%90%91%E3%81%91%E3%80%91aws-cloudformation-%E3%81%A7-vpc-%E3%82%92%E6%A7%8B%E7%AF%89%E3%81%99%E3%82%8B/>`__

`mastering aws cloudformation packt publishing<https://www.packtpub.com/product/mastering-aws-cloudformation/9781789130935>`__

`stack overflow(cloudformation) <https://stackoverflow.com/questions/64775766/how-to-create-an-aws-sftp-server-with-internet-facing-vpc-endpoint-with-cloudfor>`__
