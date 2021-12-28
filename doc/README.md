# Scrapyについて

## spiderについて

Spiderクラスはscrapy.Spiderのオーバーライド  

## Chromデベロッパーツールについて

- 開発者ツールを開くショートカットキー   
`command + option + i`

## xpath

- xpath playground  
https://scrapinghub.github.io/xpath-playground/

- 前方後方一致   
  starts-with(@属性, 値)  
  ends-with(@属性, 値) (Chromeではサポートされていない)

- リストの要素取得  
  positionを使えば複数取得できる。  
  `//ul/li[position()=2 or position()=3]`  
  以下はできない  
  `//ul/li[2 or 3]`  

## Selector

```python
res = response.xpath
# <Selector xpath='', data=[]>
res.getall()
# data=[]
```

## settings.pyの設定

- HTTP CACHE
```python
HTTPCACHE_ENABLED = True
# キャッシュの有効期限（秒単位）
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
```

- USER-AGENT  
response.request.headers['User-Agent']

## リンクの辿り方

- scrapy.Request(URL, callback=コールバックメソッド)  
URLは絶対URLのみ

- response.follow(URL/Selector, callback=コールバックメソッド)  
相対URLにも対応  
a要素のSelectorから自動的にhref属性からリンクを取得  

## ログ

- python loggging  
  loggging.info(出力内容)  

- ログレベル  
  1. CRITICAL
  2. ERROR
  3. WARNING
  4. INFO
  5. DEBUG

## ファイル出力

- %(name)s：スパイダー名
- %(time)s：時間

```
scrpay crawl [spider名] -o %(name)s_%(time)s.json
```