# My Scrapy Crawler

## getting start

```
docker-compose up -d --build
```

## 実行コマンド

コンテナに入る

```
docker-compose run --rm {contaier name} bash
```

クローラー開始コマンド

```
scrapy crawl {spider name}_spider
```

## テスト

```
falke8 ./
```

## デバッグ

該当箇所に以下のデバッガー置く。
```python
import pdb; pdb.set_trace()
```
