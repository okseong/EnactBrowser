# Scenario 1

The child iframe was able to access the parent iframe's DOM.

## Environment

* Chrome version = 87 (latest)

* Args

  * --disable-web-security
  
    * --user-data-dir="\<path\>"
  
  * --disable-site-isolation-trials

* URL

  * parent = ```http://localhost:8001```
  
  * child = ```http://localhost:8002```

## Description

* --disable-site-isolation-trials 를 추가적으로 사용한 이유

  * --disable-web-security + (--user-data-dir) 만으로는
  
  * child iframe 이 parent iframe's DOM 을 Access 할 수 없었습니다

  * 구글링 결과, --disable-site-isolation-trials 를 넣으면 가능하다길래

  * 넣었더니, 그제서야 SOP 를 위반할 수 있었습니다
