========================
Linuxのしくみ(技術評論社)
========================

-------------------
第一章
-------------------
メモ
===========================

::
      
   #
    sar -P ALL 1 10

`<https://qiita.com/maiyama18/items/956ac41c4cf6cf85ae12>`__

自作問題（？）
========================
1. **かネール**とは?カーネルはなぜ必用？
2. **システムコール** とは？いつ何によって発行されるのか？
3. 書籍ではgo/pythonのシステムコールをstraceで見ていた,rustで同じことを実行してみよ。
   
::

    //インストールは↓
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

    #なおpyとrustでくらべると行数もかなり違う・・・・  
    $ wc -l hello*.log
     697 hello_py.log
      68 hello_rust.log


4. 


------------------------
第二章
------------------------

自作問題
========================
1. **fork/execv関数** の違いは？
2. プロセスの状態を３つ列挙せよ
3. 特定のプロセスの状態を確認するにはどういうコマンドを使う？
4. **ゾンビプロセス** とはなにか？
5. **シグナル** とは？
6. **SIGINT** 以外のシグナルにはなにがある？あとSIGINTってなに？



