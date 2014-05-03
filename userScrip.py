from django.contrib.auth.models import User
from core.models import DimCustomerUnit as Units
import unicodedata

'''
EJECUTAR:
---------
python manage.py shell
>>>  execfile('userScrip.py')
'''

unitsVector = Units.objects.all()

usernames = []

for element in unitsVector:
	usernames.append(element.customer.replace(" ", ""))

usernames = list(set(usernames))


USERS = []
for nameU in usernames:
	nameU = nameU[0:29]
	nameU = nameU.encode('ascii','ignore')
	emailU = nameU + "@mail.com"
	passwordU = "1234"
	u = User(username=nameU, password=passwordU, email=emailU) 
	try:
		u.save()
	except:
		print nameU