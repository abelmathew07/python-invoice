import datetime
from pyinvoice.models import InvoiceInfo, ServiceProviderInfo, ClientInfo, Item
from pyinvoice.templates import SimpleInvoice
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
customer_Name = input('Enter Customer\'s Name : ')

doc = SimpleInvoice('invoice.pdf')

now = datetime.datetime.now()

doc.invoice_info = InvoiceInfo(1729, now, datetime.timedelta(days=7))
doc.service_provider_info = ServiceProviderInfo(
   name='SmartHaven',
    street='Sansad Marg, Gokul Nagar, Janpath, Connaught Place, 110001.',
    city='New Delhi'
)

doc.client_info = ClientInfo(name = customer_Name)

while(True):
    item = input('Enter the name of the item : ')
    price = int(input('Enter price of the item : '))
    unit = int(input('Number of units sold : '))
    description = input('Enter the description of the item : ')
    doc.add_item(Item(item,description,unit,price))
    q = input("Do you want to add more items? (y/n)")
    if q=="n":
        break

message = 'Thank you for shopping with us today! Come back soon!'

doc.set_item_tax_rate(12)
doc.set_bottom_tip("Thank you for shopping with us today! Come back soon!")
doc.finish()

print("pdf saved as invoice.pdf")
