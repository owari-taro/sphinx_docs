==================
linux-tips
==================


--------------------
ファイル関連
--------------------
ファイル検索
------------
:: 
    
    #ファイル名に"hogehoge"という文字列が含まれるファイルを探してくる
    find {path} -name "hogehoge"
    #hoge{*}.json名ファイルを探してくる
    find {path} -name "hoge*.json"
    #拡張子が".py"でコンテンツのimport行だけをsortして重複を削除して表示
    find . -name "*.py"  -exec cat {} \;|grep import|sort|uniq
