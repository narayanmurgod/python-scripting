import decimal  #import decimal: This imports the entire decimal module, which means you can use any functionality provided by the module by prefixing it with decimal.
#import decimal
#d = decimal.Decimal('3.14')

from decimal import Decimal #from decimal import Decimal: This imports the Decimal class directly from the decimal module, allowing you to use Decimal without the module prefix. This can make your code cleaner and more readable. For example:
#from decimal import Decimal
#d = Decimal('3.14')


v1=Decimal(4.5)
v2=Decimal(8.9)

print(v1+v2)