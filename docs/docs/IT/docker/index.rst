=============================
docker basic
=============================


------------------------
mount
------------------------

* bind mount
* volume mount

-------
起動
-------

使い捨て
=================

::

    docker run --rm  -it {image_name} /bin/bash

    docker run --rm it {image_name} -v data:/data/

----------------------
image作成
----------------------

Dockerfile作成
==================

------------------------
docker network
------------------------

bridge network
==================
| 指定なしでdocker runするとbridgeネットワークが割り当てられる  
| 確認するには

IP確認
----------

:: 

    docker run -dit --name web01 -p 8080:80 httpd:2.4
    docker run -dit --name web01 -p 8081:80 httpd:2.4
    #IPアドレス確認
    docker container inspect web01

    #
    docker network inspect bridge


::

    docker run --rm -it /bin/bash ubuntu
    #host側のipわかれば普通に通信できる
    > curl {docker host}:{port}