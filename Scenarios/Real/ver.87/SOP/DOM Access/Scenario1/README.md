# Scenario 1

The child iframe was able to access the parent iframe's DOM.

## Environment

* Args

  * --disable-web-security
  
    * --user-data-dir="\<path\>"
  
  * --disable-site-isolation-trials

* Chrome version = 87 (latest)  

* URL

  * parent = ```http://localhost:8001```
  
  * child = ```http://localhost:8002```
