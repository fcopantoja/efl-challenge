Program that transform the incoming data from payload.json so that it can be imported into the assessmentResponse table

Instructions
=======

Run with python3 ```python transform.py```
  
Example of console output
=======
```
(1, 'idCard_scan', '1', 'nationalId', None, 2, "['0', '1']")
(2, 'idCard', '1', 'nationalId', None, 2, "['0', '1']")
(3, '_nationalId', None, 'nationalId', None, 1, None)
(4, 'twitter', '0', 'social', None, None, "['0']")
(5, 'linkedin', '0', 'social', None, None, "['1', '0']")
(6, 'facebook', '1', 'social', None, None, "['1']")
(7, '_social', None, 'social', None, 1, None)
(8, 'pinDrop', None, 'location', None, 1, None)
(9, 'cellData', None, 'cellData', None, None, None)
```