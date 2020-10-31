# Test Details

## Same-Origin Policy

The same-origin policy (SOP) is arguably the most important principle in browser security. In this category, we test the browser's SOP implementation for DOM access, cookies, and requests using the XMLHttpRequest API.

---

### # DOM access

In all document object model (DOM) tests, we are always testing whether one page can access the DOM of another. In each test we refer to a parent and a child, where the child is an \<iframe\> inside the parent. When a parent accesses its child frame, it uses the contentWindow property. When a child frame accesses its parent, it does so with the window.parent property. In each test, one page tries to access the document.location.protocol property of the other. This is one of many properties for which access should be restricted by the same-origin policy.

DOM access should be denied by the browser whenever the origins of the two pages are different. An origin is usually a (scheme, host, port) tuple, except Internet Explorer doesn't compare the port when comparing two origins. The vast majority of the SOP for DOM tests below test cross-origin requests in which the hosts are different.

We also test that the document.domain can be used to loosen the same-origin policy restrictions. This property allows two co-operating pages to allow cross-origin DOM access between them. Any page may set document.domain to be a subset of its current hostname. If two pages each set their document.domain properties to the same value, they will appear to have the same origin and so DOM access between them will be granted. It is not sufficient for just one of the two pages to set their document.domain value, and the value must be a fully-qualified right-hand fragment of the page's current hostname. We test a wide range of legal and illegal document.domain values, and that DOM access is always correctly allowed or blocked.

---

### # DOM access - child accessing parent (Case 1)

* parent : <https://browseraudit.com>
* child : <https://test.browseraudit.com>

---

### # DOM access - parent accessing child (Case 1)

* parent : <https://browseraudit.com>
* child : <https://test.browseraudit.com>

---

### # DOM access - child accessing parent (Case 2)

* parent : <https://test.browseraudit.com>
* child : <https://browseraudit.com>

---

### # DOM access - parent accessing child (Case 2)

* parent : <https://test.browseraudit.com>
* child : <https://browseraudit.com>

---

### # XMLHttpRequest

The same-origin policy applies to the XMLHttpRequest API in a very similar manner to the DOM. That is, a client-side script may only make HTTP requests using the XMLHttpRequest API to the origin it originated from. The key difference when comparing the SOP for XMLHttpRequest to the SOP for DOM is that the document.domain property has no effect on origin checks for XMLHttpRequest. This means that it is impossible for two cooperating websites to agree for there to be cross-origin requests between them. The other main difference is that Internet Explorer takes the port into account when comparing origins for XMLHttpRequest requests, whereas this is ignored in its SOP checks for DOM access.

We test the SOP for the XMLHttpRequest API below. We check that requests are allowed when the origins match, and that they are blocked when either the host or scheme does not match. We don't currently test for differing ports.

---

### Cookies - domain scope

The same-origin policy for cookies defines when a browser should send a cookie with an HTTP request. Cookies often contain private and sensitive data, and so should only be sent with requests to the intended origin. The scope of a cookie (that is, the requests it will be sent with) can be broadened with the Domain parameter. It can be set to any fully-qualified right-hand segment of the qualified hostname, up to one level below the TLD. This means that a page at payments.secure.example.com may tell the browser to send a cookie to \*.secure.example.com or \*.example.com but not to www.payments.secure.com (since this is more specific than the page's current hostname) or *.com (since this is too broad).

We test that the browser's SOP for cookies behaves correctly when domain scope is set with the Domain parameter. We also test that illegal values are not allowed.

---

### Cookies - illegal domain values

---

### Cookies - path scope

Whilst the Domain parameter of a cookie can be used to broaden its scope, the Path property can be used to restrict a cookie's scope. It specifies a path prefix, telling the browser to send the cookie only with requests matching that path. The paths are matched from the left, so a cookie with a path of /user will be sent with requests to both /user/status and /user/account. We test this behaviour below.

---
