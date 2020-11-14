# Scenario #2

The parent iframe was able to access the child iframe's DOM.

## Environment

* Chrome version = 87 (latest)

* Args

  * --disable-web-security
  
    * --user-data-dir="\<path\>"
  
  * --disable-site-isolation-trials

* URL

  * parent = ```http://localhost:8001```
  
  * child = ```http://localhost:8002```
  
## Behavior

* SOP 에 따르면 parent iframe 은 child iframe's DOM 에 접근이 불가능합니다

* 따라서, img 가 parent 에서 load 되면 안됩니다

* 하지만 --disable-web-security, --disable-site-isolation-trials 와 같은

* Args 를 사용함으로써 이를 위반할 수 있었습니다


## Description

* --disable-site-isolation-trials 를 추가적으로 사용한 이유

  * --disable-web-security + (--user-data-dir) 만으로는
  
  * parent iframe 이 child iframe's DOM 을 Access 할 수 없었습니다

  * 구글링 결과, --disable-site-isolation-trials 를 넣으면 가능하다길래

  * 넣었더니, 그제서야 SOP 를 위반할 수 있었습니다
