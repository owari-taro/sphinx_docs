# pandas自作cheetsheet
毎回忘れるので備忘録。扱うデータも小規模なのでパフォーマンス的には最善でないかもしれないが
## indexをつけなおしたい
フィルタしたあとにindexがもとのままなので、直したい時などに使う 

```
df.reset_index(drop=True, inplace=True)
```

### for-loopで内容を確認したあとに値を設定したい
```
df.at[i,"A"]=value
```
### フィルタしたあとに値を取り出したい！

```
##nameがtaroの行のemailの値のみを取り出す
df[df["name"]=="taro"].email.values[0]
```
