## Pub / Sub Redis in Python

Project for basic redis PUB/Sub in Flask Project Python.

### Required ###
1. Install Windows SubSystem for Linux (WSL) ubuntu 18.04 LTS in Microsoft Store. 
2. Install redis in ubuntu. [Follow this link](https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-redis-on-ubuntu-18-04)
3. Install create all required in virtual env.
  - pip install flask
  - pip install redis
  - pip install request
  
  Active your virtual enviroment and run (in directory file).
  - python init.py

### Subscribe(Sub) Redis using SSE

Here simple explaination about SSE. Server-sent events open a single long-lived HTTP connection. The server then unidirectionally sends data when it has it, there is no need for the client to request it or do anything but wait for messages.

I using SSE for check any subscription of event. 

```markdown
@app.route("/stream")
def stream():
    return Response(event_stream(), mimetype="text/event-stream")


def event_stream():
    pubsub = r.pubsub(ignore_subscribe_messages=True)
    pubsub.subscribe('notification')                ###//subscription of notification event name
    for message in pubsub.listen():
        yield 'data: %s\n\n' % message['data']
```

### Publish(Pub) Redis using HTTP

```markdown
@app.route('/post', methods=['POST'])
def post():
    message = request.form['message']
    r.publish('notification', message)    ###set name of event as sample is notification.
    return Response(status=204)
```

### More about redis

Click this [link](https://redis.io/topics/pubsub)
