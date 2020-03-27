from flask import Flask, Response, render_template, request
import redis

app = Flask(__name__)
r = redis.Redis(host='localhost', port=6379, db=0, charset='utf-8', decode_responses=True)


@app.route("/")
def index():
    return render_template('hello.html')


@app.route('/post', methods=['POST'])
def post():
    message = request.form['message']
    r.publish('notification', message)
    return Response(status=204)


@app.route("/stream")
def stream():
    return Response(event_stream(), mimetype="text/event-stream")


def event_stream():
    pubsub = r.pubsub(ignore_subscribe_messages=True)
    pubsub.subscribe('notification')
    for message in pubsub.listen():
        yield 'data: %s\n\n' % message['data']


if __name__ == "__main__":
    app.run(debug=True)
