from datetime import datetime, timedelta
from django.core.management.base import BaseCommand, CommandError
# from ../../models import BotUser
from events.models import Event


class Command(BaseCommand):
    help = 'Sets up database with initial data.'

    def get_user_data(self):
        user_data = [
            {
                'username': 'admin',
                'email': 'rai.unknown@gmail.com',
                'is_active': True,
                'user_type': 'Admin',
                'first_name': 'Anjan',
                'last_name': 'Rai',
                'password': 'anjanrai',
            },
            {
                'username': 'anjanraiz',
                'email': 'anzaan.rai@gmail.com',
                'is_active': True,
                'user_type': 'User',
                'first_name': 'Anzan',
                'last_name': 'Rai',
                'password': 'Anj@nra1',
            },
            {
                'username': 'annie',
                'email': 'astha7828@gmail.com',
                'is_active': True,
                'user_type': 'User',
                'first_name': 'Anisha',
                'last_name': 'Shrestha',
                'password': 'anish@'
            }
        ]
        return user_data

    def get_news_data(self):
        news_data = [
            {
                'title': 'Parramatta Pulse 2019 Edition',
                'detail': 'Lord Mayor’s message\n This is the latest copy of Parramatta Pulse. There will be lots '
                          'of events, festivals and projects this spring. I am happy to tell you what will happen. '
                          'Celebrating the Royal Australian Navy On Saturday 14 September 2019 we will have a parade '
                          'called The HMAS Parramatta Freedom of Entry Parade. On that day 200 officers and sailors '
                          'from the ship HMAS Parramatta will walk through Parramatta'
            },
            {
                'title': 'EXPRESSION OF INTEREST - 353A TO 353C CHURCH STREET PARRAMATTA',
                'detail': 'The City of Parramatta Council is calling for Expressions of Interest (EOIs) for the short'
                          ' term lease of 353A to 353C Church Street Parramatta (Premises). With the additional benefit'
                          ' of being a part of Riverside Theatres on the Parramatta Riverfront, the Premises offers an'
                          ' opportunity for an experienced Food and Beverage/Live Entertainment Café/Bar Operator to'
                          ' realise a concept in Live Entertainment Café/Bar Restaurant in Parramatta’s most popular'
                          ' eating hub known as “Eat Street”. EOIs close at 3pm, Wednesday 28th August 2019. For a '
                          'copy of the EOI documentation, please complete the form on this page. For any enquiries, '
                          'content Council’s Manager Space Property Services and Space Management at '
                          'bbegg@cityofparramatta.nsw.gov.au.'
            },
            {
                'title': 'PUBLIC NOTICE - REGIONAL FOX BAITING PROGRAM',
                'detail': 'Please be advised that a fox baiting program will soon commence in the local area in '
                          'conjunction with Greater Sydney Local Land Services. The aim of the program is to protect '
                          'native wildlife including threatened species from fox predation. Foxoff poison baits '
                          '(containing 1080) will be buried in the following Reserves between Monday 12 August 2019 '
                          'to Friday 30 August 2019: Lake Parramatta Reserve, managed by City of Parramatta Council '
                          'Bidjigal Reserve, managed by The Hills Shire Council and The Bidjigal Reserve Trust '
                          'Excelsior Reserve, Ted Horwood Reserve, 13 Codwells Road Kenthurst, managed by The Hills '
                          'Shire Council The above listed bushland reserves will be closed to dogs (including dogs '
                          'walking on a lead), during and up to 4 weeks after the fox baiting program. 1080 poison is '
                          'lethal to dogs and cats. Dogs on leads can return to these reserves on Saturday 28 September'
                          ' 2019. In an emergency, contact City of Parramatta Council on 1300 617 058 or The Hills '
                          'Shire Council on 9843 0555 or 9843 0109. Foxoff is designed specifically for fox control. '
                          'Trained staff will undertake the baiting. Baits will be buried 10cm under the ground to '
                          'reduce the risk of non-target poisoning. Signs stating \'1080 FOX POISON LAID IN THIS AREA\''
                          ' and \'Dogs (& Cats) are prohibited\' will be displayed in the relevant parks and reserves '
                          'to notify the public about the program. FURTHER INFORMATION Please contact the following '
                          'agencies for further information, or if you notice that one or more of the signs has been '
                          'vandalised or is missing: City of Parramatta Council on 1300 617 058 The Hills Shire Council'
                          ' on 9843 0555 or 9843 0109 Greater Sydney Local Land Services on 1300 795 299'
            }
        ]
        return news_data

    def get_event_data(self):
        return [
            {
                'title': 'AUSLAN AND ENGLISH STORY TIME ( 3 - 5 YEARS )',
                'venue': 'Parramatta Library',
                'start_time': (datetime.today() + timedelta(days=1)).time(),
                'start_date': (datetime.today() + timedelta(days=1)).date(),
                'end_date': (datetime.today() + timedelta(days=1)).date(),
                'end_time': (datetime.today() + timedelta(days=1, minutes=30)).time(),
                'description': 'Auslan Story Time is aimed at children who sign or are learning to sign who enjoy '
                               'having stories told to them in Auslan. Story time fosters an early love of reading and'
                               ' social interaction in readiness for school. A fun, monthly story time session for '
                               'pre-school aged deaf and hearing children.',
                'organizer': 'Parramatta Library Community'
            },
            {
                'title': 'DEMENTIA TALK IN HINDI',
                'venue': 'Parramatta Library',
                'start_time': (datetime.today() + timedelta(days=1)).time(),
                'start_date': (datetime.today() + timedelta(days=1)).date(),
                'end_date': (datetime.today() + timedelta(days=1)).date(),
                'end_time': (datetime.today() + timedelta(days=1, hours=1, minutes=30)).time(),
                'description': 'Dementia is a result of changes that take place in the brain and affects the person’s'
                               ' memory, mood and behaviour. When a parent or loved one is diagnosed with dementia '
                               'there’s a thousand questions that come to mind, what drugs do we use used to calm them'
                               ' down?  How do we talk to them? How do we calm them down? Can it be prevented? Join us'
                               ' to have answers to your questions.\nThis program is in Partnership with MWNNA '
                               'Muslim Women’s National Network Australia.\nBookings are not required.',
                'organizer': 'Parramatta Library Community'
            },
            {
                'title': 'HEALTHY STORY TIME',
                'venue': 'Parramatta Library',
                'start_time': (datetime.today() + timedelta(days=5)).time(),
                'start_date': (datetime.today() + timedelta(days=5)).date(),
                'end_date': (datetime.today() + timedelta(days=5)).date(),
                'end_time': (datetime.today() + timedelta(days=5, minutes=30)).time(),
                'description': 'Come and celebrate health month with us as we share some songs and stories about food '
                               'and healthy eating! Make a healthy plate craft to take home.\nSuitable for ages 4 to '
                               '5 years.\nBookings not required.  Places are limited to the first 30 children. Please '
                               'arrive at least fifteen minutes prior to the session starting to secure your place. ',
                'organizer': 'Parramatta Library Community'
            },
            {
                'title': 'HOW TO PACK A HEALTHY LUNCHBOX',
                'venue': 'Parramatta Library',
                'start_time': (datetime.today() + timedelta(days=5, hours=3)).time(),
                'start_date': (datetime.today() + timedelta(days=5)).date(),
                'end_date': (datetime.today() + timedelta(days=5)).date(),
                'end_time': (datetime.today() + timedelta(days=5, hours=3, minutes=30)).time(),
                'description': 'Celebrate Health Month at Parramatta Library with a presentation by NSW Health.\n'
                               'This presentation for parents of school aged children, particularly kindergarten '
                               'students, will show how to pack a healthy lunch box.\nParents will receive an '
                               'information pack to take home.\nBookings are not required.',
                'organizer': 'Parramatta Library Community'
            }
        ]

    def handle(self, *args, **options):
        for event in self.get_event_data():
            new_event = Event(**event)
            new_event.save()