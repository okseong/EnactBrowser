# Scenario #1

The child iframe was able to access the parent iframe's DOM.

## Environment

* Chrome version = 87 (latest)

* Args

  * --disable-web-security
  
    * --user-data-dir="\<path\>"
  
  * --disable-site-isolation-trials

* URL

  * parent = https://enact-parent.github.io/server-parent/staticpages/ver87/scenario1/parent.html
  
  * child = https://enact-child.github.io/server-child/staticpages/ver87/scenario1/child.html
  
## Behavior

* SOP 에 따르면 child iframe 은 parent iframe's DOM 에 접근이 불가능합니다

* 따라서, child 의 img 가 parent 에서 load 되면 안됩니다

* 하지만 --disable-web-security, --disable-site-isolation-trials 와 같은

* Args 를 사용함으로써 이를 위반할 수 있었습니다

## Description

* --disable-site-isolation-trials 를 추가적으로 사용한 이유

  * --disable-web-security + (--user-data-dir) 만으로는
  
  * child iframe 이 parent iframe's DOM 을 Access 할 수 없었습니다

  * 구글링 결과, --disable-site-isolation-trials 를 넣으면 가능하다길래

  * 넣었더니, 그제서야 SOP 를 위반할 수 있었습니다
