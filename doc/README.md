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
