from flask import Flask
import time
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor()
app = Flask(__name__)


@app.route('/')
def update_redis():
    executor.submit(do_update)
    return 'ok',200


def do_update():
    time.sleep(3)
    print('start update cache')
    time.sleep(1)
    print("end")


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8089,debug=True)
