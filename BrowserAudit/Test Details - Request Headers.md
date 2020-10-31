# Test Details

## Request Headers

In this category, we test browser security features related to miscellaneous HTTP request headers that do not fit into any other category.

---

### # Referer

The Referer header should not be included in a non-secure request if the referring page was transferred with a secure protocol. This behaviour is defined in RFC 2616 “Hypertext transfer protocol–HTTP/1.1” (Fielding, Roy, et al., 1999). This behaviour exists because the source of a link might be private information or might reveal an otherwise private information source.

We test this behaviour by loading an image with a non-secure request and checking that the Referer header was not sent to the server with request for the image.

---
