from kafkaTest import *

kafka = kafkaTest(8081)
print("### sending events ###")
kafka.producer()
print()
print('### consume events ###')
kafka.consumer()
print()

print('### verify all events consumed ###')
kafka.check_all_events_consumed(kafka.producer_events, kafka.consumer_events)


print(kafka.producer_events)
print(kafka.consumer_events)

print()
print('### Check delivery order for consumed events')
kafka.check_delivery_order(kafka.producer_events, kafka.consumer_events)
