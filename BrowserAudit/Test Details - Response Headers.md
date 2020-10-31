# Test Details

## Response Headers

In this category, we test browser security features related to miscellaneous HTTP response headers that do not fit into any other category.

---

### # X-Frame-Options

X-Frame-Options is a server-side technique that can be used to prevent clickjacking (UI redressing) attacks. Its implementation in current browsers is documented in RFC 7034 “HTTP Header Field X-Frame-Options” (Ross, David, and Tobias Gondrom, 2013). X-Frame-Options is a response header that specifies whether or not the document being served is allowed to be rendered in a frame. More specifically, the header specifies the origin (scheme, host and port) that is allowed to render the document in a frame.

We test for correct behaviour of the DENY, SAMEORIGIN and ALLOW-FROM header values. Our tests use only \<iframe\> tags, although X-Frame-Options can also apply to \<frame\>, \<object\>, \<applet\> and \<embed\> tags.

X-Frame-Options is supported in all modern browsers, although the implementations across browsers differ. Some browsers behave differently when dealing with nested frames, so we do not test these cases at all as there is no defined correct behaviour. Note also that not all browsers support the ALLOW-FROM value.

---

### # Strict-Transport-Security

HTTP Strict Transport Security (HSTS) is a security mechanism that allows a server to instruct browsers only to communicate with it over a secure (HTTPS) connection for that domain. It exists primarily to defend against man-in-the-middle attacks in which an attacker is able to intercept his victim's network connection. The server sends this instruction with a Strict-Transport-Security header, defined in RFC 6797 “HTTP Strict Transport Security (HSTS)” (Hodges, Jeff, Collin Jackson, and Adam Barth, 2012).

When HSTS is enabled on a domain, a compliant browser must rewrite any plain HTTP requests to that domain to use HTTPS. This includes both URLs entered into the navigation bar by the user, and elements loaded by a webpage. The Strict-Transport-Security header should only be sent in an HTTPS response. If the browser receives the header in a response sent over plain HTTP, it should be ignored.

We test the basic behaviour of HSTS and the includeSubDomains option. We also ensure that the header is ignored when transferred with an insecure protocol, and that the HSTS state correctly expires based on the max-age value. All of these tests work by testing whether a request for an image at <http://browseraudit.com/set_protocol> is rewritten to use HTTPS or not.

Some of today's browsers support HSTS. The notable exception is Internet Explorer, which does not support it even in version 11. Safari has only supported HSTS since OS X Mavericks.

---
