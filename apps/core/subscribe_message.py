import pika
import ast


class RabbitMqServerConfigure():

    def __init__(self, host='localhost', queue='hello'):

        """ Server initialization   """

        self.host = host
        self.queue = queue


class rabbitmqServer():

    def __init__(self, server):

        """
        :param server: Object of class RabbitMqServerConfigure
        """

        self.server = server
        self._connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.server.host))
        self._channel = self._connection.channel()
        self._tem = self._channel.queue_declare(queue=self.server.queue)
        self.payload = None

    @staticmethod
    def callback(ch,method, properties, body):

        self.Payload = body.decode("utf-8")
        processed_data = ast.literal_eval(self.Payload)
        # print(Payload)
        # return "Data Received : {}".format(Payload)

    def startserver(self):
        self._channel.basic_consume(
            queue=self.server.queue,
            on_message_callback=rabbitmqServer.callback,
            auto_ack=True)
        self._channel.start_consuming()


# if __name__ == "__main__":
#     serverconfigure = RabbitMqServerConfigure(host='localhost',
#                                               queue='hello')

#     server = rabbitmqServer(server=serverconfigure)
#     server.startserver()