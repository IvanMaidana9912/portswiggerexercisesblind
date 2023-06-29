## Portswigger Exercises Blind Success

### Info 
- This script will help to solve the exercises blindfolded using Burp Suite. You have to get the TrackId, the session, the URL and the option you require.

#### URL labs: 
- https://portswigger.net/web-security/all-labs#sql-injection
#### Install 
- python (and extensions in VSC).
- pwntools (with command pip).


### Help:

usage: scripthk.py [-h] -u URL -t TRACKINGID -s SESSION -o OPTION

Blind SQL Injection with conditional responses-errors and time delays || portswigger labs.

options:
  1. -h, --help                                  (show this help message and exit).
  2. -u URL, --url URL                           (Provide page "URL").
  3. -t TRACKINGID, --trakingid TRACKINGID       (Provide the "TrackingId" of the request).
  4. -s SESSION, --session SESSION               (Provide the "Session" code).
  5. -o OPTION, --option OPTION                  (1- Responses, 2- Errors or 3 for Delay).

  ### Example:
  - python scripthk.py -u URL -t TRACKID -s SESSION -o OPTION