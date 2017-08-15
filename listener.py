import pika
from threading import Thread
from downloader import Downloader


class Listener(Thread):

    def __init__(self):
        self._address = 'amqp://qxyexflk:2tQMYESQNKyFmgXqJf2Nq9g9qWd5G1N1@orangutan.rmq.cloudamqp.com/qxyexflk'
        self._queue = 'mytube'
        self._timeout = 5
        self._downloader = Downloader('D:/Work')

    def run(self):
        parameters = pika.URLParameters(self._address)
        parameters.socket_timeout = self._timeout
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
        channel.queue_declare(queue=self._queue, durable=True)
        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(self.on_message, queue=self._queue)
        channel.start_consuming()
        print('Waiting for messages...')

    def on_message(self, channel, method, properties, body):
        print('Received Message')
        try:
            self._downloader.download(body.decode('ascii'))
            channel.basic_ack(delivery_tag=method.delivery_tag)
            print('Processed Message')
        except:
            channel.basic_nack(delivery_tag=method.delivery_tag, requeue=False)
            print('Failed To Process')

