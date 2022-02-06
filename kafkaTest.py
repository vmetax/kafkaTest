from time import sleep
from json import dumps
from kafka import KafkaProducer
from json import loads
from kafka import KafkaConsumer
import random


class kafkaTest(object):
        producer_events = {}
        consumer_events = {}
        ip_port = 0

        def __init__(self, port):
                self.ip_port = port

        def producer(self):
                producer = KafkaProducer(
                bootstrap_servers=['localhost:9092'],value_serializer=lambda x: dumps(x).encode('utf-8'))

                for j in range(19):
                        n = random.randint(j,19)
                        print(j ,"-->", n)
                        data = {'counter': n}
                        producer.send('topic_test', value=data)
                        self.producer_events[j] = n
                        sleep(0.5)

        def consumer(self):
                consumer = KafkaConsumer('topic_test', bootstrap_servers=['localhost:9092'],
                auto_offset_reset='latest',enable_auto_commit=True, group_id='my-group-id',
                consumer_timeout_ms=10000, value_deserializer=lambda x: loads(x.decode('utf-8')))
                counter = 0
                for event in consumer:
                        event_data = event.value['counter']
                        print(counter, "-->", event_data)
                        #print(event)
                        self.consumer_events[counter] = event_data
                        counter = counter + 1
                        sleep(2)
                consumer.close()


        def check_all_events_consumed(self, producer_events_dict, consumer_events_dict):
                assert(len(producer_events_dict) == len(consumer_events_dict)), "All events did not consumed"
                print("All events consumed")

        def check_delivery_order(self, producer_events_dict, consumer_events_dict):
                assert(producer_events_dict == consumer_events_dict), "Events received with wrong order"
                print("Events received with correct order")
