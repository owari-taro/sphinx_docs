==================================
rabbitmq
==================================
---------------
queue
---------------

queueのメッセージの紛失防止策
=================================

consumer側
===========
consumer側でmessageを受け取って処理している途中での失敗などした場合
queueから削除されずに再度queueで受け取れるようにする必要がある。
その際には下記の設定が必要

* auto_ack=Trueだと受け取った時点でokしてしまう
  https://www.rabbitmq.com/confirms.html#acknowledgement-modes


broker側
============
brokerの停止などによりmemory上のメッセージが消失してしまうリスク
