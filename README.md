# sonypyapi
There are three different ways to call this function from the command line: </br>
* no arguments: the function will use "getAvailableApiList" as the default function

* one argument: the argument will be used as the method name

* more than one argument: first argument is the method name and the rest are the parameters for the method

```

$ python sonypyapi.py 
{"result":[["getVersions","getMethodTypes","getApplicationInfo","getAvailableApiList","getEvent","startRecMode","stopRecMode"]],"id":1}
$ python sonypyapi.py startRecMode
{"result":[0],"id":1}
$ python sonypyapi.py getIsoSpeedRate
{"result":["3200"],"id":1}
$ python sonypyapi.py setIsoSpeedRate 3200
{"result":[0],"id":1}

```
