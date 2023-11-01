================
celery入門
================


----------------
Hello world
----------------
1. tasks.pyを作る

* Celeryの引数に認証情報を入れる

::


    from celery import Celery

    #認証情報@hostを書く
    app=Celery("tasks",broker="amqp://user:password@localhost:5672/")

    @app.task
    def add(x,y):
        print("desktop application")
        print("waaaaaaaaaaaaaaaaaa")
        return x+y


2. celeryを起動する
   

   ::
        > celery -A tasks worker --loglevel=INFO

            -------------- celery@LAPTOP-04BSFD95 v5.3.4 (emerald-rush)
            --- ***** -----
            -- ******* ---- Linux-5.15.90.1-microsoft-standard-WSL2-x86_64-with-glibc2.35 2023-10-20 18:53:41
            - *** --- * ---
            - ** ---------- [config]
            - ** ---------- .> app:         tasks:0x7ffa571f36d0
            - ** ---------- .> transport:   amqp://user:**@localhost:5672//
            - ** ---------- .> results:     disabled://
            - *** --- * --- .> concurrency: 16 (prefork)
            -- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
            --- ***** -----
            -------------- [queues]
            


3. 別のterminalを立ち上げて、でceleryにtaskを投げる
    
同時にtaskの実行プロセス側のログに表示される

    :: 

        from tasks import add

        add.delay(1,3)



4. 
