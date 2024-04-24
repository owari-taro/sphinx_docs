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

   regionはtemplate内では指定しない(`参考 <https://serverfault.com/questions/1103642/how-to-specify-aws-region-in-cloudformation-vpc>`__)


スタック作成
---------------------------

:: 

  $ aws cloudformation create-stack --stack-name test --template-body file://vpc.yaml 

スタックの削除
-----------------------------
作成したリソースを削除したい場合は↓のコマンドで削除できる。実行しても特に標準出力には何も表示されない。

::
  
    aws cloudformation delete-stack --stack-name test

  
