from datetime import datetime, date
from pyinvoice.models import InvoiceInfo, ServiceProviderInfo, ClientInfo, Item, Transaction
from pyinvoice.templates import SimpleInvoice

doc = SimpleInvoice('invoice.pdf')


doc.is_paid = True

doc.invoice_info = InvoiceInfo(11022, datetime.now(), datetime.now())  


doc.service_provider_info = ServiceProviderInfo(
    name='Xperia',
    city='Adoor',
    state='Kerala',
)


doc.client_info = ClientInfo(name='Abel', email='abel@gmail.com')


doc.add_item(Item('Iphone', '', 1, '65000'))



doc.set_item_tax_rate(23)  
doc.set_bottom_tip("Thanks for shopping with us!")
doc.finish()
