========================
lambdaでvirus-check
========================

--------------------------
1.cdk-serverless-clamscan
--------------------------
概要
=====
.. _aws_blog: https://aws.amazon.com/jp/blogs/developer/virus-scan-s3-buckets-with-a-serverless-clamav-based-cdk-construct/
.. _github: https://github.com/awslabs/cdk-serverless-clamscan 
.. _storage制限: https://aws.amazon.com/jp/blogs/aws/aws-lambda-now-supports-up-to-10-gb-ephemeral-storage/ 

`aws_blog`_ で紹介されている方法で、CDKで簡単にデプロイできる。 [1]_

.. figure:: img/serverless_clamscan.png


主な機能としては

* clamavでウィルスチェックしタグに結果を出力
* s3に置かれた定義ファイルを12時間ごとに更新
* ウィルスチェック完了後にSNS・lambda・eventbridgeなどに連携(defaultはeventbridge)

.. admonition::  aws-cdk
    
    | awsリソース・デプロイをコードで書ける仕組み。python,typesciprtなどに対応している。
    | この `aws_blog`_ ではtypescript使った方法し書かれてない。
    | typescriptのほうは動作したが,pythonでやってみようとしたがdeployはできたもののウィルスチェックしてくれなかった...

    :: 

        #cdkのpythonで書いた例
        class CdkWorkshopStack(Stack):

        def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
            super().__init__(scope, construct_id, **kwargs)
    　　　　
            queue = sqs.Queue(
                self, "CdkWorkshopQueue",
                visibility_timeout=Duration.seconds(300),
            )

.. _lambdaコンテナ: https://gallery.ecr.aws/lambda/python
.. _lambda関数: https://github.com/awslabs/cdk-serverless-clamscan/tree/main/assets/lambda/code
.. _cloud9: https://aws.amazon.com/jp/cloud9/

メモ
========
* `lambda関数`_ は `lambdaコンテナ`_ 使ってpythonで書かれている。
* lambdaのファイル512MBファイルシステムの容量制限があったとき(2021年)に公開されたのだったので、EFS使用してるが,
  今は制限10GBに緩和されたので(10GBより大きいファイルは扱わないのであれば)EFSとか使わなくても実装できそう
* scaner自体が更新された場合はcdk使ってデプロイしなおす必要がある( `aws_blog`_ )
* cdk使える環境は `cloud9`_ 使えば最初からインストールされているので楽   
  


コスト
=======

deploy初回時しか使われないコストは小さいため無視する
* cloud9(ec2を10分くらい)
* 初回定義ファイルダウンロード(60sくらい)
  

* s3
* EFS
* SNS?
* lambda(ウィルスチェック実行)
  (1) 一回180kbで,59458ms
  (2) 初回のみ:1分
  (3)ウィルススキャン
  (4)動いてない
  (5)定義更新
  1分２回

* lambda(更新分)
* cloud9


* 月一1時間とかでいい
* 全国で画像枚数がどれだけあるか
* 
:: 

        IAM Statement Changes
    ┌───┬──────────────┬────────┬──────────────┬──────────────┬───────────────┐
    │   │ Resource     │ Effect │ Action       │ Principal    │ Condition     │
    ├───┼──────────────┼────────┼──────────────┼──────────────┼───────────────┤
    │ + │ ${BucketNoti │ Allow  │ sts:AssumeRo │ Service:lamb │               │
    │   │ ficationsHan │        │ le           │ da.amazonaws │               │
    │   │ dler050a0587 │        │              │ .com         │               │
    │   │ b7544547bf32 │        │              │              │               │
    │   │ 5f094a3db834 │        │              │              │               │
    │   │ /Role.Arn}   │        │              │              │               │
    ├───┼──────────────┼────────┼──────────────┼──────────────┼───────────────┤
    │ + │ ${Custom::S3 │ Allow  │ sts:AssumeRo │ Service:lamb │               │
    │   │ AutoDeleteOb │        │ le           │ da.amazonaws │               │
    │   │ jectsCustomR │        │              │ .com         │               │
    │   │ esourceProvi │        │              │              │               │
    │   │ der/Role.Arn │        │              │              │               │
    │   │ }            │        │              │              │               │
    ├───┼──────────────┼────────┼──────────────┼──────────────┼───────────────┤
    │ + │ ${rBucket.Ar │ Allow  │ s3:GetBucket │ AWS:${rClams │               │
    │   │ n}           │        │ *            │ can/Serverle │               │
    │   │ ${rBucket.Ar │        │ s3:GetObject │ ssClamscan/S │               │
    │   │ n}/*         │        │ *            │ erviceRole.A │               │
    │   │              │        │ s3:List*     │ rn}          │               │
    │   │              │        │              │ AWS:arn:${AW │               │
    │   │              │        │              │ S::Partition │               │
    │   │              │        │              │ }:sts::${AWS │               │
    │   │              │        │              │ ::AccountId} │               │
    │   │              │        │              │ :assumed-rol │               │
    │   │              │        │              │ e/${rClamsca │               │
    │   │              │        │              │ n/Serverless │               │
    │   │              │        │              │ Clamscan/Ser │               │
    │   │              │        │              │ viceRole}/${ │               │
    │   │              │        │              │ rClamscanSer │               │
    │   │              │        │              │ verlessClams │               │
    │   │              │        │              │ can3E6CD9D8} │               │
    │ + │ ${rBucket.Ar │ Allow  │ s3:DeleteObj │ AWS:${Custom │               │
    │   │ n}           │        │ ect*         │ ::S3AutoDele │               │
    │   │ ${rBucket.Ar │        │ s3:GetBucket │ teObjectsCus │               │
    │   │ n}/*         │        │ *            │ tomResourceP │               │
    │   │              │        │ s3:List*     │ rovider/Role │               │
    │   │              │        │              │ .Arn}        │               │
    ├───┼──────────────┼────────┼──────────────┼──────────────┼───────────────┤
    │ + │ ${rBucket.Ar │ Allow  │ s3:GetBucket │ AWS:${rClams │               │
    │   │ n}           │        │ *            │ can/Serverle │               │
    │   │ ${rBucket.Ar │        │ s3:GetObject │ ssClamscan/S │               │
    │   │ n}/*         │        │ *            │ erviceRole}  │               │
    │   │ ${rClamscan/ │        │ s3:List*     │              │               │
    │   │ VirusDefsBuc │        │              │              │               │
    │   │ ket.Arn}     │        │              │              │               │
    │   │ ${rClamscan/ │        │              │              │               │
    │   │ VirusDefsBuc │        │              │              │               │
    │   │ ket.Arn}/*   │        │              │              │               │
    ├───┼──────────────┼────────┼──────────────┼──────────────┼───────────────┤
    │ + │ ${rBucket.Ar │ Allow  │ s3:PutObject │ AWS:${rClams │               │
    │   │ n}/*         │        │ Tagging      │ can/Serverle │               │
    │   │              │        │ s3:PutObject │ ssClamscan/S │               │
    │   │              │        │ VersionTaggi │ erviceRole.A │               │
    │   │              │        │ ng           │ rn}          │               │
    │   │              │        │              │ AWS:arn:${AW │               │
    │   │              │        │              │ S::Partition │               │
    │   │              │        │              │ }:sts::${AWS │               │
    │   │              │        │              │ ::AccountId} │               │
    │   │              │        │              │ :assumed-rol │               │
    │   │              │        │              │ e/${rClamsca │               │
    │   │              │        │              │ n/Serverless │               │
    │   │              │        │              │ Clamscan/Ser │               │
    │   │              │        │              │ viceRole}/${ │               │
    │   │              │        │              │ rClamscanSer │               │
    │   │              │        │              │ verlessClams │               │
    │   │              │        │              │ can3E6CD9D8} │               │
    │ + │ ${rBucket.Ar │ Allow  │ s3:PutObject │ AWS:${rClams │               │
    │   │ n}/*         │        │ Tagging      │ can/Serverle │               │
    │   │              │        │ s3:PutObject │ ssClamscan/S │               │
    │   │              │        │ VersionTaggi │ erviceRole}  │               │
    │   │              │        │ ng           │              │               │
    │ + │ ${rBucket.Ar │ Deny   │ s3:GetObject │ AWS:*        │ "StringEquals │
    │   │ n}/*         │        │              │              │ ": {          │
    │   │              │        │              │              │   "s3:Existin │
    │   │              │        │              │              │ gObjectTag/sc │
    │   │              │        │              │              │ an-status": [ │
    │   │              │        │              │              │     "IN PROGR │
    │   │              │        │              │              │ ESS",         │
    │   │              │        │              │              │     "INFECTED │
    │   │              │        │              │              │ ",            │
    │   │              │        │              │              │     "ERROR"   │
    │   │              │        │              │              │   ]           │
    │   │              │        │              │              │ },            │
    │   │              │        │              │              │ "ArnNotEquals │
    │   │              │        │              │              │ ": {          │
    │   │              │        │              │              │   "aws:Princi │
    │   │              │        │              │              │ palArn": [    │
    │   │              │        │              │              │     "${rClams │
    │   │              │        │              │              │ can/Serverles │
    │   │              │        │              │              │ sClamscan/Ser │
    │   │              │        │              │              │ viceRole.Arn} │
    │   │              │        │              │              │ ",            │
    │   │              │        │              │              │     "arn:${AW │
    │   │              │        │              │              │ S::Partition} │
    │   │              │        │              │              │ :sts::${AWS:: │
    │   │              │        │              │              │ AccountId}:as │
    │   │              │        │              │              │ sumed-role/${ │
    │   │              │        │              │              │ rClamscan/Ser │
    │   │              │        │              │              │ verlessClamsc │
    │   │              │        │              │              │ an/ServiceRol │
    │   │              │        │              │              │ e}/${rClamsca │
    │   │              │        │              │              │ nServerlessCl │
    │   │              │        │              │              │ amscan3E6CD9D │
    │   │              │        │              │              │ 8}"           │
    │   │              │        │              │              │   ]           │
    │   │              │        │              │              │ }             │
    ├───┼──────────────┼────────┼──────────────┼──────────────┼───────────────┤
    │ + │ ${rClamscan/ │ Allow  │ lambda:Invok │ Service:even │ "ArnLike": {  │
    │   │ DownloadDefs │        │ eFunction    │ ts.amazonaws │   "AWS:Source │
    │   │ .Arn}        │        │              │ .com         │ Arn": "${rCla │
    │   │              │        │              │              │ mscan/VirusDe │
    │   │              │        │              │              │ fsUpdateRule. │
    │   │              │        │              │              │ Arn}"         │
    │   │              │        │              │              │ }             │
    ├───┼──────────────┼────────┼──────────────┼──────────────┼───────────────┤
    │ + │ ${rClamscan/ │ Allow  │ lambda:Invok │ AWS:${rClams │               │
    │   │ DownloadDefs │        │ eFunction    │ can/InitDefs │               │
    │   │ .Arn}        │        │              │ /ServiceRole │               │
    │   │ ${rClamscan/ │        │              │ }            │               │
    │   │ DownloadDefs │        │              │              │               │
    │   │ .Arn}:*      │        │              │              │               │
    ├───┼──────────────┼────────┼──────────────┼──────────────┼───────────────┤
    │ + │ ${rClamscan/ │ Allow  │ sts:AssumeRo │ Service:lamb │               │
    │   │ DownloadDefs │        │ le           │ da.amazonaws │               │
    │   │ /ServiceRole │        │              │ .com         │               │
    │   │ .Arn}        │        │              │              │               │
    ├───┼──────────────┼────────┼──────────────┼──────────────┼───────────────┤
    │ + │ ${rClamscan/ │ Allow  │ sts:AssumeRo │ Service:lamb │               │
    │   │ InitDefs/Ser │        │ le           │ da.amazonaws │               │
    │   │ viceRole.Arn │        │              │ .com         │               │
    │   │ }            │        │              │              │               │
    ├───┼──────────────┼────────┼──────────────┼──────────────┼───────────────┤
    │ + │ ${rClamscan/ │ Deny   │ sqs:*        │ AWS:*        │ "Bool": {     │
    │   │ ScanErrorDea │        │              │              │   "aws:Secure │
    │   │ dLetterQueue │        │              │              │ Transport": f │
    │   │ .Arn}        │        │              │              │ alse          │
    │   │              │        │              │              │ }             │
    ├───┼──────────────┼────────┼──────────────┼──────────────┼───────────────┤
    │ + │ ${rClamscan/ │ Deny   │ sqs:*        │ AWS:*        │ "Bool": {     │
    │   │ ScanErrorQue │        │              │              │   "aws:Secure │
    │   │ ue.Arn}      │        │              │              │ Transport": f │
    │   │              │        │              │              │ alse          │
    │   │              │        │              │              │ }             │
    │ + │ ${rClamscan/ │ Allow  │ sqs:GetQueue │ AWS:${rClams │               │
    │   │ ScanErrorQue │        │ Attributes   │ can/Serverle │               │
    │   │ ue.Arn}      │        │ sqs:GetQueue │ ssClamscan/S │               │
    │   │              │        │ Url          │ erviceRole}  │               │
    │   │              │        │ sqs:SendMess │              │               │
    │   │              │        │ age          │              │               │
    ├───┼──────────────┼────────┼──────────────┼──────────────┼───────────────┤
    │ + │ ${rClamscan/ │ Allow  │ events:PutEv │ AWS:${rClams │               │
    │   │ ScanResultBu │        │ ents         │ can/Serverle │               │
    │   │ s.Arn}       │        │              │ ssClamscan/S │               │
    │   │              │        │              │ erviceRole}  │               │
    ├───┼──────────────┼────────┼──────────────┼──────────────┼───────────────┤
    │ + │ ${rClamscan/ │ Allow  │ sts:AssumeRo │ Service:vpc- │               │
    │   │ ScanVPC/Flow │        │ le           │ flow-logs.am │               │
    │   │ Logs/IAMRole │        │              │ azonaws.com  │               │
    │   │ .Arn}        │        │              │              │               │
    │ + │ ${rClamscan/ │ Allow  │ iam:PassRole │ AWS:${rClams │               │
    │   │ ScanVPC/Flow │        │              │ can/ScanVPC/ │               │
    │   │ Logs/IAMRole │        │              │ FlowLogs/IAM │               │
    │   │ .Arn}        │        │              │ Role}        │               │
    ├───┼──────────────┼────────┼──────────────┼──────────────┼───────────────┤
    │ + │ ${rClamscan/ │ Allow  │ logs:CreateL │ AWS:${rClams │               │
    │   │ ScanVPC/Flow │        │ ogStream     │ can/ScanVPC/ │               │
    │   │ Logs/LogGrou │        │ logs:Describ │ FlowLogs/IAM │               │
    │   │ p.Arn}       │        │ eLogStreams  │ Role}        │               │
    │   │              │        │ logs:PutLogE │              │               │
    │   │              │        │ vents        │              │               │
    ├───┼──────────────┼────────┼──────────────┼──────────────┼───────────────┤
    │ + │ ${rClamscan/ │ Allow  │ lambda:Invok │ Service:s3.a │ "ArnLike": {  │
    │   │ ServerlessCl │        │ eFunction    │ mazonaws.com │   "AWS:Source │
    │   │ amscan.Arn}  │        │              │              │ Arn": "${rBuc │
    │   │              │        │              │              │ ket.Arn}"     │
    │   │              │        │              │              │ },            │
    │   │              │        │              │              │ "StringEquals │
    │   │              │        │              │              │ ": {          │
    │   │              │        │              │              │   "AWS:Source │
    │   │              │        │              │              │ Account": "${ │
    │   │              │        │              │              │ AWS::AccountI │
    │   │              │        │              │              │ d}"           │
    │   │              │        │              │              │ }             │
    ├───┼──────────────┼────────┼──────────────┼──────────────┼───────────────┤
    │ + │ ${rClamscan/ │ Allow  │ sts:AssumeRo │ Service:lamb │               │
    │   │ ServerlessCl │        │ le           │ da.amazonaws │               │
    │   │ amscan/Servi │        │              │ .com         │               │
    │   │ ceRole.Arn}  │        │              │              │               │
    ├───┼──────────────┼────────┼──────────────┼──────────────┼───────────────┤
    │ + │ ${rClamscan/ │ Deny   │ s3:*         │ AWS:*        │ "Bool": {     │
    │   │ VirusDefsAcc │        │              │              │   "aws:Secure │
    │   │ essLogsBucke │        │              │              │ Transport": f │
    │   │ t.Arn}       │        │              │              │ alse          │
    │   │ ${rClamscan/ │        │              │              │ }             │
    │   │ VirusDefsAcc │        │              │              │               │
    │   │ essLogsBucke │        │              │              │               │
    │   │ t.Arn}/*     │        │              │              │               │
    ├───┼──────────────┼────────┼──────────────┼──────────────┼───────────────┤
    │ + │ ${rClamscan/ │ Allow  │ s3:PutObject │ Service:logg │ "ArnLike": {  │
    │   │ VirusDefsAcc │        │              │ ing.s3.amazo │   "aws:Source │
    │   │ essLogsBucke │        │              │ naws.com     │ Arn": "${rCla │
    │   │ t.Arn}/*     │        │              │              │ mscan/VirusDe │
    │   │              │        │              │              │ fsBucket.Arn} │
    │   │              │        │              │              │ "             │
    │   │              │        │              │              │ },            │
    │   │              │        │              │              │ "StringEquals │
    │   │              │        │              │              │ ": {          │
    │   │              │        │              │              │   "aws:Source │
    │   │              │        │              │              │ Account": "${ │
    │   │              │        │              │              │ AWS::AccountI │
    │   │              │        │              │              │ d}"           │
    │   │              │        │              │              │ }             │
    ├───┼──────────────┼────────┼──────────────┼──────────────┼───────────────┤
    │ + │ ${rClamscan/ │ Deny   │ s3:DeleteBuc │ NOT AWS:arn: │               │
    │   │ VirusDefsBuc │        │ ketPolicy    │ ${AWS::Parti │               │
    │   │ ket.Arn}     │        │ s3:PutBucket │ tion}:iam::$ │               │
    │   │              │        │ Policy       │ {AWS::Accoun │               │
    │   │              │        │              │ tId}:root    │               │
    ├───┼──────────────┼────────┼──────────────┼──────────────┼───────────────┤
    │ + │ ${rClamscan/ │ Allow  │ s3:GetObject │ AWS:*        │               │
    │   │ VirusDefsBuc │        │ s3:ListBucke │              │               │
    │   │ ket.Arn}     │        │ t            │              │               │
    │   │ ${rClamscan/ │        │              │              │               │
    │   │ VirusDefsBuc │        │              │              │               │
    │   │ ket.Arn}/*   │        │              │              │               │
    │ + │ ${rClamscan/ │ Allow  │ s3:DeleteObj │ AWS:${Custom │               │
    │   │ VirusDefsBuc │        │ ect*         │ ::S3AutoDele │               │
    │   │ ket.Arn}     │        │ s3:GetBucket │ teObjectsCus │               │
    │   │ ${rClamscan/ │        │ *            │ tomResourceP │               │
    │   │ VirusDefsBuc │        │ s3:List*     │ rovider/Role │               │
    │   │ ket.Arn}/*   │        │              │ .Arn}        │               │
    │ + │ ${rClamscan/ │ Deny   │ s3:*         │ AWS:*        │ "Bool": {     │
    │   │ VirusDefsBuc │        │              │              │   "aws:Secure │
    │   │ ket.Arn}     │        │              │              │ Transport": f │
    │   │ ${rClamscan/ │        │              │              │ alse          │
    │   │ VirusDefsBuc │        │              │              │ }             │
    │   │ ket.Arn}/*   │        │              │              │               │
    │ + │ ${rClamscan/ │ Allow  │ s3:GetObject │ AWS:*        │ "StringEquals │
    │   │ VirusDefsBuc │        │ s3:ListBucke │              │ ": {          │
    │   │ ket.Arn}     │        │ t            │              │   "aws:Source │
    │   │ ${rClamscan/ │        │              │              │ Vpce": "${rCl │
    │   │ VirusDefsBuc │        │              │              │ amscan/ScanVP │
    │   │ ket.Arn}/*   │        │              │              │ C/S3Endpoint} │
    │   │              │        │              │              │ "             │
    │   │              │        │              │              │ }             │
    │ + │ ${rClamscan/ │ Allow  │ s3:Abort*    │ AWS:${rClams │               │
    │   │ VirusDefsBuc │        │ s3:DeleteObj │ can/Download │               │
    │   │ ket.Arn}     │        │ ect*         │ Defs/Service │               │
    │   │ ${rClamscan/ │        │ s3:GetBucket │ Role}        │               │
    │   │ VirusDefsBuc │        │ *            │              │               │
    │   │ ket.Arn}/*   │        │ s3:GetObject │              │               │
    │   │              │        │ *            │              │               │
    │   │              │        │ s3:List*     │              │               │
    │   │              │        │ s3:PutObject │              │               │
    │   │              │        │ s3:PutObject │              │               │
    │   │              │        │ LegalHold    │              │               │
    │   │              │        │ s3:PutObject │              │               │
    │   │              │        │ Retention    │              │               │
    │   │              │        │ s3:PutObject │              │               │
    │   │              │        │ Tagging      │              │               │
    │   │              │        │ s3:PutObject │              │               │
    │   │              │        │ VersionTaggi │              │               │
    │   │              │        │ ng           │              │               │
    ├───┼──────────────┼────────┼──────────────┼──────────────┼───────────────┤
    │ + │ ${rClamscan/ │ Deny   │ s3:PutObject │ NOT AWS:${rC │               │
    │   │ VirusDefsBuc │        │ *            │ lamscan/Down │               │
    │   │ ket.Arn}/*   │        │              │ loadDefs/Ser │               │
    │   │              │        │              │ viceRole.Arn │               │
    │   │              │        │              │ }            │               │
    │   │              │        │              │ NOT AWS:arn: │               │
    │   │              │        │              │ ${AWS::Parti │               │
    │   │              │        │              │ tion}:sts::$ │               │
    │   │              │        │              │ {AWS::Accoun │               │
    │   │              │        │              │ tId}:assumed │               │
    │   │              │        │              │ -role/${rCla │               │
    │   │              │        │              │ mscan/Downlo │               │
    │   │              │        │              │ adDefs/Servi │               │
    │   │              │        │              │ ceRole}/${rC │               │
    │   │              │        │              │ lamscanDownl │               │
    │   │              │        │              │ oadDefs4F9AF │               │
    │   │              │        │              │ D32}         │               │
    ├───┼──────────────┼────────┼──────────────┼──────────────┼───────────────┤
    │ + │ *            │ Allow  │ elasticfiles │ AWS:${rClams │ "StringEquals │
    │   │              │        │ ystem:Client │ can/Serverle │ ": {          │
    │   │              │        │ Mount        │ ssClamscan/S │   "elasticfil │
    │   │              │        │              │ erviceRole}  │ esystem:Acces │
    │   │              │        │              │              │ sPointArn": " │
    │   │              │        │              │              │ arn:${AWS::Pa │
    │   │              │        │              │              │ rtition}:elas │
    │   │              │        │              │              │ ticfilesystem │
    │   │              │        │              │              │ :${AWS::Regio │
    │   │              │        │              │              │ n}:${AWS::Acc │
    │   │              │        │              │              │ ountId}:acces │
    │   │              │        │              │              │ s-point/${rCl │
    │   │              │        │              │              │ amscanScanFil │
    │   │              │        │              │              │ eSystemScanLa │
    │   │              │        │              │              │ mbdaAP4BA65D3 │
    │   │              │        │              │              │ 5}"           │
    │   │              │        │              │              │ }             │
    │ + │ *            │ Allow  │ s3:PutBucket │ AWS:${Bucket │               │
    │   │              │        │ Notification │ Notification │               │
    │   │              │        │              │ sHandler050a │               │
    │   │              │        │              │ 0587b7544547 │               │
    │   │              │        │              │ bf325f094a3d │               │
    │   │              │        │              │ b834/Role}   │               │
    ├───┼──────────────┼────────┼──────────────┼──────────────┼───────────────┤
    │ + │ arn:${AWS::P │ Allow  │ elasticfiles │ AWS:${rClams │               │
    │   │ artition}:el │        │ ystem:Client │ can/Serverle │               │
    │   │ asticfilesys │        │ Write        │ ssClamscan/S │               │
    │   │ tem:${AWS::R │        │              │ erviceRole}  │               │
    │   │ egion}:${AWS │        │              │              │               │
    │   │ ::AccountId} │        │              │              │               │
    │   │ :file-system │        │              │              │               │
    │   │ /${rClamscan │        │              │              │               │
    │   │ ScanFileSyst │        │              │              │               │
    │   │ em3273544C}  │        │              │              │               │
    └───┴──────────────┴────────┴──────────────┴──────────────┴───────────────┘
    IAM Policy Changes
    ┌───┬──────────────────────────────────┬──────────────────────────────────┐
    │   │ Resource                         │ Managed Policy ARN               │
    ├───┼──────────────────────────────────┼──────────────────────────────────┤
    │ + │ ${BucketNotificationsHandler050a │ arn:${AWS::Partition}:iam::aws:p │
    │   │ 0587b7544547bf325f094a3db834/Rol │ olicy/service-role/AWSLambdaBasi │
    │   │ e}                               │ cExecutionRole                   │
    ├───┼──────────────────────────────────┼──────────────────────────────────┤
    │ + │ ${Custom::S3AutoDeleteObjectsCus │ {"Fn::Sub":"arn:${AWS::Partition │
    │   │ tomResourceProvider/Role}        │ }:iam::aws:policy/service-role/A │
    │   │                                  │ WSLambdaBasicExecutionRole"}     │
    ├───┼──────────────────────────────────┼──────────────────────────────────┤
    │ + │ ${rClamscan/DownloadDefs/Service │ arn:${AWS::Partition}:iam::aws:p │
    │   │ Role}                            │ olicy/service-role/AWSLambdaBasi │
    │   │                                  │ cExecutionRole                   │
    ├───┼──────────────────────────────────┼──────────────────────────────────┤
    │ + │ ${rClamscan/InitDefs/ServiceRole │ arn:${AWS::Partition}:iam::aws:p │
    │   │ }                                │ olicy/service-role/AWSLambdaBasi │
    │   │                                  │ cExecutionRole                   │
    ├───┼──────────────────────────────────┼──────────────────────────────────┤
    │ + │ ${rClamscan/ServerlessClamscan/S │ arn:${AWS::Partition}:iam::aws:p │
    │   │ erviceRole}                      │ olicy/service-role/AWSLambdaBasi │
    │   │                                  │ cExecutionRole                   │
    │ + │ ${rClamscan/ServerlessClamscan/S │ arn:${AWS::Partition}:iam::aws:p │
    │   │ erviceRole}                      │ olicy/service-role/AWSLambdaVPCA │
    │   │                                  │ ccessExecutionRole               │
    └───┴──────────────────────────────────┴──────────────────────────────────┘
    Security Group Changes
    ┌───┬────────────────────────┬─────┬─────────────┬────────────────────────┐
    │   │ Group                  │ Dir │ Protocol    │ Peer                   │
    ├───┼────────────────────────┼─────┼─────────────┼────────────────────────┤
    │ + │ ${rClamscan/ScanFileSy │ In  │ TCP 2049    │ ${rClamscan/Serverless │
    │   │ stemSecurityGroup.Grou │     │             │ Clamscan/SecurityGroup │
    │   │ pId}                   │     │             │ .GroupId}              │
    │ + │ ${rClamscan/ScanFileSy │ Out │ ICMP 252-86 │ 255.255.255.255/32     │
    │   │ stemSecurityGroup.Grou │     │             │                        │
    │   │ pId}                   │     │             │                        │
    ├───┼────────────────────────┼─────┼─────────────┼────────────────────────┤
    │ + │ ${rClamscan/Serverless │ Out │ TCP 443     │ Everyone (IPv4)        │
    │   │ Clamscan/SecurityGroup │     │             │                        │
    │   │ .GroupId}              │     │             │                        │
    │ + │ ${rClamscan/Serverless │ Out │ TCP 2049    │ ${rClamscan/ScanFileSy │
    │   │ Clamscan/SecurityGroup │     │             │ stemSecurityGroup.Grou │
    │   │ .GroupId}              │     │             │ pId}                   │
    └───┴────────────────────────┴─────┴─────────────┴────────────────────────┘
    (NOTE: There may be securit