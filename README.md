# MicroSingleton

A micro library for singleton pattern (both application and class level)

## Application level singleton
Only one application instance can run at same time.
`MicroSingleton` allow programmer to stop second instance or just kill existed instance.

### Demo
#### Code
This code is also stored in 'demo/webapp.py'

```python
from singleton.application.singleton import SingletonApplication
from singleton.application.action import Action

from flask import Flask
app = Flask(__name__)

SingletonApplication("./MicroSingleton.pid").action(Action.SINGLETON)


@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run()
```

#### First instance
Start first instance by execute:

```bash
python ./demo/webapp.py
```

You will get output message:

```text
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

#### Second instance
Start first instance by execute same code in other terminal:

```bash
python ./demo/webapp.py
```

You will get output message from second instance:

```text
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Then you will see console of first instance output message and return like:
```text
Terminated: 15
```

#### Conclude
After this demo, you should notice that this demo application are singleton at application level.