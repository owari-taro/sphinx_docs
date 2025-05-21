# pandas自作cheetsheet
たまにしか使わず毎回pandasの操作方法を忘れるので備忘録として残す。　扱うデータも小規模だったのでパフォーマンス的には最善でないかもしれない。


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

## indexを抜いてcsv出力したい
index=Falseをいれよう
```
df.to_csv("data/final.csv",index=False)
```

## 特定の列の値に基づいて別の列の値を更新したい
### dictionaryで指定できるとき
```
# status列の値に基づいてmodeを設定する。
mode={"新規":"create","所属変更":"update","削除":"delete","登録済み":"unchange"}
# https://stackoverflow.com/questions/20250771/remap-values-in-pandas-column-with-a-dict-preserve-nans
merged["mode"]=merged["status"].map(mode)
```
### 関数で動的に生成するとき

```
merged["password"]=merged.apply(lambda row: create_password(15) if row['mode'] =="create" else "", axis=1)
```
