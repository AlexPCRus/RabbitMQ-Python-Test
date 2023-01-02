import os.path
import sys
import traceback
import pika
import time


def get_consuming_speed():
    setting_file = '/app/settings/consume-delay.cfg'
    textdata = '5'
    if os.path.isfile(setting_file):
        with open(setting_file, 'r', encoding='utf8') as f:
            textdata = f.readline()
    try:
        floatdata = float(textdata)
    except:
        floatdata = 1
    return floatdata


def prepare_rabbit_server():
    print("Making server configuration")
    rmq_url_connection_str = "amqp://rmuser:rmpassword@rabbitmq:5672/"
    rmq_parameters = pika.URLParameters(rmq_url_connection_str)
    rmq_connection = pika.BlockingConnection(rmq_parameters)
    rmq_channel = rmq_connection.channel()
    rmq_channel.exchange_declare(exchange="first", exchange_type="direct", durable=True)
    rmq_channel.queue_declare(queue="test", durable=True)
    rmq_channel.queue_bind(exchange="first", queue="test", routing_key="testkey")
    rmq_connection.close()


def start_consuming():
    print("Start consuming")
    rmq_url_connection_str = "amqp://rmuser:rmpassword@rabbitmq:5672/"
    rmq_parameters = pika.URLParameters(rmq_url_connection_str)
    rmq_connection = pika.BlockingConnection(rmq_parameters)
    rmq_channel = rmq_connection.channel()
    rmq_channel.basic_consume(on_message_callback=on_message, queue="test")
    try:
        rmq_channel.start_consuming()
    except KeyboardInterrupt:
        rmq_channel.stop_consuming()
    except Exception:
        rmq_channel.stop_consuming()
        error_trace = traceback.format_exc()
        print(f'Ошибка:{error_trace}\n')
        sys.stderr.write(f'Ошибка:{error_trace}\n')
    rmq_connection.close()


def on_message(channel, method_frame, header_frame, body):
    body_str = body.decode("utf-8")[:4000]
    print(f'Message body:{body_str}\r')
    channel.basic_ack(delivery_tag=method_frame.delivery_tag)
    sleep_time = get_consuming_speed()
    time.sleep(sleep_time)


if __name__ == '__main__':
    print("Starting ...")
    prepare_rabbit_server()
    start_consuming()
