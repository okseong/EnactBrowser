# Test Details

## Content Security Policy

In this category, we test that the browser correctly implements Content Security Policy 1.0 (Sterne, Brandon, and Adam Barth, 2012). This means that we test the Content Security Policy (CSP) using only the Content-Security-Policy header, and not the X-Content-Security-Policy and X-WebKit-CSP headers used in experimental implementations in older browsers. A browser that implements the CSP using one of the latter two headers will fail many of the below tests.

The CSP is a mechanism used to mitigate cross-site scripting (XSS) attacks. It introduces the concept of source whitelists. A web developer can use the Content-Security-Policy header to explicitly specify the sources from which scripts, stylesheets and many other resources may be loaded. This can be done on a per-document basis by serving a different header value with each page.

We test a variety of origin mismatches for many resource types. At present, we only check origins that differ in host/domain. We do not test for origins that differ in scheme or port. A test referring to a “remote” resource is referring to a resource loaded from our subdomain test.browseraudit.com. A “local“ resource is one loaded from the same origin as this page.

The number of tests executed below depends on your browser. For example, some tests will only be executed if a Flash plugin is installed.

---

### # stylesheets

---

### # scripts

---

### # 'unsafe-inline'

---

### # 'unsafe-eval'

---

### # objects

---

### # images

---

### # media

---

### # frames

---

### # fonts

---

### # connect-src

---

### # sandbox

The "sandbox" directive enforces a sandbox policy on iframe elements. It is an optional part of the Content Security Policy 1.0 specification: web browsers are not required to implement it.

---

### # report-uri

These tests check that the browser sends a POST request to the server when the CSP is violated and a report-uri has been specified in the header. Note that some anti-tracking browser addons may block these report requests. The browser should not follow any 3xx redirects when sending violation reports.

---
