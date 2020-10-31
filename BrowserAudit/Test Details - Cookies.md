# Test Details

## Cookies

A lot of cookie security relates to the same-origin policy, and the setting of cookie scope through the Domain and Path attributes. This is covered in the Same-Origin Policy section. In this section, we are testing two other aspects of cookie security: the HttpOnly and Secure attributes. We test the behaviour of these attributes as defined in RFC 6265 “HTTP state management mechanism” (Kristol, David M. and Lou Montulli, 2000).

---

### # HttpOnly flag

The HttpOnly attribute of a cookie instructs the browser to reveal that cookie only through an HTTP API. That is, the cookie may be transmitted to a server via an HTTP request, but should not be made available to client-side scripts. The benefit of this is that, even if a cross-site scripting (XSS) vulnerability is exploited, the cookie cannot be stolen.

HttpOnly cookies are supported by all major browsers. The notable exception is Android 2.3's stock browser.

We have three tests. In the first test, we simply check that an HttpOnly cookie sent from the server cannot then be accessed by JavaScript. The latter two tests are testing that HttpOnly cookies cannot be created by JavaScript.

---

### # Secure flag

When a cookie has the Secure attribute set, a compliant browser will include the cookie in an HTTP request only if the request is transmitted over a secure channel, i.e. an HTTPS request. This keeps the cookie confidential; an attacker would not be able to read it even if he were able to intercept the connection between the victim and the destination server.

The Secure flag is supported by all major browsers.

We have four tests, testing the behaviour of the Secure flag both when the cookies are set by the server and set by JavaScript. In each pair of tests, the first checks that a cookie with the Secure flag is sent to the server with an HTTPS request. The second test is the interesting one: it checks that a secure cookie is not sent with a request over plain HTTP.

---
