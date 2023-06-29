## Portswigger Exercises Blind Success

### Info 

#### URL labs: https://portswigger.net/web-security/all-labs#sql-injection
#### Install python (and extensions in VSC) and pip pwntools

usage: scripthk.py [-h] -u URL -t TRACKINGID -s SESSION -o OPTION

Blind SQL Injection with conditional responses-errors and time delays || portswigger labs.

options:
  -h, --help                                  show this help message and exit
  -u URL, --url URL                           Provide page "URL".
  -t TRACKINGID, --trakingid TRACKINGID       Provide the "TrackingId" of the request.
  -s SESSION, --session SESSION               Provide the "Session" code.
  -o OPTION, --option OPTION                  1- Responses, 2- Errors or 3 for Delay.