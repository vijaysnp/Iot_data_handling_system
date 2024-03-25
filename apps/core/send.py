
import pika
# from apps.api.services.mqtt_data_handling_services import MqttdataService


class RabbitmqConfigure():

    def __init__(self, queue='hello', host='localhost', routingKey='hello', exchange=''):
        """ Configure Rabbit Mq Server  """
        self.queue = queue
        self.host = host
        self.routingKey = routingKey
        self.exchange = exchange


class RabbitMq():

    def __init__(self, server):

        """

        :param server: Object of class RabbitmqConfigure
        """

        self.server = server

        self._connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.server.host))
        self._channel = self._connection.channel()
        self._channel.queue_declare(queue=self.server.queue)

    def publish(self, payload: dict):

        """

        :param payload: JSON payload
        :return: None
        """

        self._channel.basic_publish(exchange=self.server.exchange,
                      routing_key=self.server.routingKey,
                      body=str(payload))

        print("Published Message: {}".format(payload))
        self._connection.close()


# if __name__ == "__main__":
#     server = RabbitmqConfigure(queue='hello',
#                                host='localhost',
#                                routingKey='hello',
#                                exchange='')

#     rabbitmq = RabbitMq(server)
#     di = {
#             "city": "pune",
#             "temperature": 38,
#             "email": "test@example.com"
#             }
#     rabbitmq.publish(di)