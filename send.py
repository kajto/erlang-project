__author__ = 'Clint'
import pika

# set the connection betwween app and broker
connection = pika.BlockingConnection(pika.ConnectionParameters(
               'localhost'))

channel = connection.channel()


# create a queue
channel.queue_declare(queue='hello')

# exchange
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')

print " [x] Sent 'Hello World!'"

# close the connection
connection.close()

