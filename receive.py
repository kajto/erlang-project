__author__ = 'Clint'
import pika

# set the connection between program and broker
connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost'))
channel = connection.channel()

# create a queue, if there wasn't one in the broker
channel.queue_declare(queue='hello')

# declare callback function - function called after receiving the message
def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)

# receive messages from 'hello' queue using 'callback' function
channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

# activate infinite loop
print ' [*] Waiting for messages. To exit press CTRL+C'
channel.start_consuming()
