import factory
from factory import fuzzy
import string
from django.contrib.auth import get_user_model
from bookstore.models import Book
from datetime import datetime
from datetime import datetime
import pytz

def get_good_old_time():
    time_zone = pytz.timezone('UTC')
    dt = datetime(year=1970, month=1, day=1,
                  hour=0, minute=0, second=0, microsecond=0,
                  tzinfo=time_zone)
    return dt

class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book
    id=factory.Faker("uuid4")#uuid
    title = fuzzy.FuzzyText(
        length=30,
        chars=string.ascii_lowercase + string.ascii_uppercase + string.printable,
    )
    published_at = fuzzy.FuzzyDateTime(start_dt=get_good_old_time(), force_microsecond=0)
    version = fuzzy.FuzzyChoice([1,2,3,4,5,6])#https://stackoverflow.com/questions/36641568/factory-boy-random-choice-for-a-field-with-field-option-choices
