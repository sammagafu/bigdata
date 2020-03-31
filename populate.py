import os,django,random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bigdata.settings')


django.setup()

from customer.models import CustomerHouseHold, Transaction, MetreReading
from transformer.models import Transformer, TransformerReading

from faker import Faker

# def create_customer_household(N):
#     fake = Faker()
#     for _ in range(N):
#         customerRefno = random.randint(100, 9999)
#         customerMetreno = random.randint(10000, 9999999)
#         customerAccno = random.randint(10000, 9999999)
#         customerFirstName = fake.name()
#         customerLastName = fake.name()
#         customerLat = fake.latitude()
#         customerLong = fake.longitude()
#         customerPhone = fake.msisdn()
#         CustomerHouseHold.objects.create(customerRefno=customerRefno, customerMetreno=customerMetreno, customerAccno=customerAccno,
#     customerFirstName=customerFirstName,customerLastName=customerLastName,customerLat=customerLat,customerLong=customerLong,customerPhone=customerPhone
#     )

# def meter_reding(N):
#     fake = Faker()

#     for _ in range(N):
#         id = random.randint(1, 10)
#         bought = fake.date_time_this_year(before_now=True, after_now=False, tzinfo=None)
#         units = random.randint(10, 80)
#         Transaction.objects.create(buyer_id=id, date=bought, units=units)
# # create_customer_household(15)       
# meter_reding(200)

# def meter_reding(N):
#     fake = Faker()
#     for _ in range(N):
#         id = random.randint(1, 10)
#         date = fake.date_time_this_year(before_now=True, after_now=False, tzinfo=None)
#         voltage = random.randint(110, 240)
#         current = random.randint(100, 200)
#         consumption = random.randint(0, 240)
#         MetreReading.objects.create(owner_id=id,date=date,voltage=voltage,current=current,consumption=consumption)        

# meter_reding(1000)

# def transformerrea(N):
#     fake = Faker()
#     for _ in range(N):
#         transname = fake.name()
#         transloclat = fake.latitude()
#         transloclong = fake.longitude()
#         kvarating = fake.pyfloat(left_digits=2, right_digits=3, positive=True)
#         phyaddress = fake.street_address()
#         Transformer.objects.create(transname=transname,transloclat=transloclat,transloclong=transloclong,kvarating=kvarating,phyaddress=phyaddress)

# transformer(60)

def transformerrea(N):
    fake = Faker()
    for _ in range(N):
        id = random.randint(51,60)
        time = fake.date_time_this_year(before_now=True, after_now=False, tzinfo=None)
        phasevred = random.randint(100, 200)
        phasevblue = random.randint(100, 200)
        phasevyellow = random.randint(100, 200)
        phasecred = random.randint(100, 200)
        phasecblue = random.randint(100, 200)
        phasecyellow = random.randint(100, 200)
        TransformerReading.objects.create(transformer_id=id, time=time, phasevred=phasevred, phasevblue=phasevblue,
        phasevyellow=phasevyellow,phasecred=phasecred,phasecblue=phasecblue,phasecyellow=phasecyellow)

transformerrea(5000)