=============================
awsネットワーク入門 第二版
=============================
-------------------
第１章
-------------------
awsサービス単位
===============




--------------------------
第4章 インターネット接続
--------------------------

* サブネットにルートテーブル設定しないとvpcに紐づくメインルートテーブルが適用される
* VPC内のすべてのサブネットに共通化したいならメインルートテーブルを変更うすればよい
* ルートテーブルを作成した直後はVPC内にしか通信が通信できなくなっている

* ec2にはprivateIPが割り振られている

:: 

    [ec2-user@ip-10-0-0-154 ~]$ ifconfig
    eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
            inet 10.0.0.154  netmask 255.255.255.0  broadcast 10.0.0.255
            inet6 fe80::4e2:6dff:fe02:4485  prefixlen 64  scopeid 0x20<link>
            ether 06:e2:6d:02:44:85  txqueuelen 1000  (Ethernet)
            RX packets 64579  bytes 92756095 (88.4 MiB)
            RX errors 0  dropped 0  overruns 0  frame 0
            TX packets 19957  bytes 1149987 (1.0 MiB)
            TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

    lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
            inet 127.0.0.1  netmask 255.0.0.0
            inet6 ::1  prefixlen 128  scopeid 0x10<host>
            loop  txqueuelen 1000  (Local Loopback)
            RX packets 0  bytes 0 (0.0 B)
            RX errors 0  dropped 0  overruns 0  frame 0
            TX packets 0  bytes 0 (0.0 B)
            TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0



elasticIP
===========

* publicIPを固定したいときに使う
* デフォルトではregionで最大5個。申請すれば増やせる
* 

