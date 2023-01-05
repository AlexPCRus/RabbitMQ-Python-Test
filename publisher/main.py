import os.path
import pika
import time
import sys
import traceback


def get_publishing_speed():
    setting_file = '/app/settings/publish-delay.cfg'
    textdata = '5'
    if os.path.isfile(setting_file):
        with open(setting_file, 'r', encoding='utf8') as f:
            textdata = f.readline()
    try:
        floatdata = float(textdata)
    except:
        floatdata = 1
    return floatdata


def start_publishing():
    print("Start publishing")
    i = 1
    while True:
        try:
            rmq_url_connection_str = 'amqp://rmuser:rmpassword@rabbitmq:5672/'
            rmq_parameters = pika.URLParameters(rmq_url_connection_str)
            rmq_connection = pika.BlockingConnection(rmq_parameters)
            rmq_channel = rmq_connection.channel()
            sleep_time = get_publishing_speed()
            rmq_channel.basic_publish(exchange='first', routing_key='testkey', body=str(i).encode("utf-8"))
            print(f'Sending message {i}')
            i = i + 1
            time.sleep(sleep_time)
            rmq_connection.close()
        except Exception:
            error_trace = traceback.format_exc()
            print(f'Ошибка:{error_trace}\n')
            sys.stderr.write(f'Ошибка:{error_trace}\n')

if __name__ == '__main__':
    print("Starting ...")
    start_publishing()
