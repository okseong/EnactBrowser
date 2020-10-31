# Test Details

## Cross-Origin Resource Sharing

In this category of tests we test the browser's implementation of Cross-Origin Resource Sharing (CORS) as specified by the W3C (Van Kesteren, Anne, 2014). CORS is an extension to the XMLHttpRequest API that allows a website to carry out cross-origin communications. This means that client-side JavaScript can send an XMLHttpRequest to a URL on a domain (or scheme or port) other than the one from which it originated – something that is not otherwise possible due to the same-origin policy.

Cross-origin resource sharing allows a request to be made to a server at a different origin only if the server receiving the request explicitly allows it. That is, the server states whether or not the origin of the requesting document is allowed to make a cross-origin request to that URL. To achieve this, CORS defines a mechanism that allows the browser and server to know just enough about each other so that they can determine whether or not to allow the cross-origin request. This is primarily achieved by two key headers: an Origin header sent by the browser with the request, and an Access-Control-Allow-Origin header sent in the server's response. There are other CORS-related headers whose implementations we also test.

---

### # Access-Control-Allow-Origin

---

### # Access-Control-Allow-Methods

---

### # Access-Control-Allow-Headers

---

### # Access-Control-Expose-Headers

---
