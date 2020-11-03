# Browseraudit

## No flags

/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome

## --disable-web-security

/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --disable-web-security --user-data-dir=“/Users/gglifer/UDD” --disable-site-isolation-trials

open -a Google\ Chrome --args --disable-web-security --user-data-dir="/Users/gglifer/UDD" --disable-site-isolation-trials

--user-data-dir="<아무경로>"

## --no-sandbox

/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --no-sandbox

## --disable-site-isolation-trials

/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --disable-site-isolation-trials

## --disable-web-security + --no-sandbox + --disable-site-isolation-trials

/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --disable-web-security --user-data-dir=“/Users/gglifer/UDD” --no-sandbox --disable-site-isolation-trials

---

## Block chrome automatic update

defaults write com.google.keystone.agent checkinterval 0
