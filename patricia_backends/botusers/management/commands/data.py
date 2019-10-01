from datetime import datetime

# Heritage data to populate database.
HERITAGE_DATA = [
    {
        'name': 'NSW Lancers Barracks and Museum',
        'description': 'The museum, the Australian mainland’s longest continuous military installation, houses a '
                       'collection of photographs, diaries, weapons seized from enemy soldiers, vintage armored '
                       'vehicles and an overview of the history of the Lancers. The Lancer Barracks is made up of '
                       'several historic buildings built in 1820, including the Georgian building of Linden House – '
                       'home to the Lancer Museum. Can visit on open days '
                       ' and by appointment on any day for groups of 10 or more.',
        'open_time': datetime.time(datetime.strptime("10:00", "%H:%M")),
        'close_time': datetime.time(datetime.strptime("16:00", "%H:%M")),
        'open_days': ['Sunday'],
        'location': '2 Smith Street Parramatta 2150'
    },
    {
        'name': 'Philip Ruddock Heritage Centre',
        'description': 'Building for the V hotel by Crown Group in 2005 uncovered a series of archeological remains '
                       'from the early settlement of Parramatta. View the well-preserved remnants that include footings'
                       ' of a convict hut, footings of a colonial period cottage (including a well) and the remains of'
                       ' the Wheatsheaf Hotel – which formerly occupied the site. The centre perfectly captures the '
                       'connection between Parramatta’s heritage and its future. Visit on open days at'
                       '10:00am – 11:30am and 2:30pm – 4:00pm, Free admission. Visit the V Heritage Centre website.',
        'open_days': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
        'location': '45 Macquarie Street (Corner Marsden Street) Parramatta 2150'
    },
    {
        'name': 'Harris Park National Heritage Area',
        'description': 'A suburb of the City of Parramatta, the Harris Park Heritage Area encompasses important '
                       'historic landmarks such as Experiment Farm Cottage, Elizabeth Farm Cottage and Hambledon '
                       'Cottage. The Harris Park Heritage Walk is a self-guided tour that begins at the Parramatta '
                       'Wharf and continues through the suburb – follow the signposts – for 2.4kms or approximately '
                       '45minutes (not including time spent visiting each landmark house). '
                       'Open: Self-guided walk open 7 days. See listings for Experiment Farm Cottage, Elizabeth Farm '
                       'Cottage and Hambledon Cottage for individual opening times.  Read more about the Harris Park '
                       'National Heritage Walk '
    },
    {
        'name': 'Hambledon Cottage',
        'description': 'Built in 1824, this well-preserved and beautifully furnished home sits on the Elizabeth Farm '
                       'Estate. The house was built by John Macarthur, a British army officer and pioneer of the '
                       'Australian wool industry, and was most notably occupied by his governess Penelope Lucas in '
                       '1827. The cottage was built in the Colonial Georgian style, common at that time, using rendered'
                       ' sand stock brick.  Today home to Parramatta Historical Society.'
                       'Can visit on open days or by appointment on any day for groups of 15 or more.  Visit the '
                       'Parramatta Historical website for more information.',
        'open_days': ['Thursday', 'Friday', 'Saturday', 'Sunday'],
        'open_time': datetime.time(datetime.strptime("11:00", "%H:%M")),
        'close_time': datetime.time(datetime.strptime("16:00", "%H:%M")),
        'location': '47 Hassall Street Harris Park 2150'
    },
    # {
    #     'name': 'Elizabeth Farm',
    #     'description': 'The oldest surviving European dwelling in Australia, once occupied by John and Elizabeth '
    #                    'Macarthur and their children. Visitors can truly experience what life was like living at '
    #                    'Elizabeth Farm. This house museum is open to the public to experience hands-on. Walk the '
    #                    'grounds, sit in the drawing room chairs in front of the fire and explore the house as if it '
    #                    'were your own. 70 Alice Street Rosehill 2142, 02 9635 9488. Open: Wednesday to Sunday '
    #                    '10:00am – 4:00pm and daily during NSW school holidays.  Visit Sydney Living Museums website for'
    #                    ' more information.'
    # },
    # {
    #     'name': 'Experiment Farm Cottage ',
    #     'description': 'The cottage sits on the site of the first land grant in Australia, given to James Ruse, an '
    #                    'ex-convict who had been brought to Australia on the First Fleet to carry out his sentence in '
    #                    '1787. Upon completing his sentence Ruse asked Governor Arthur Philip for an allotment of land '
    #                    'to prove he could farm the land and be self-sufficient, which he successfully achieved in 1791 '
    #                    'by cultivating a 30acre piece of land. Surgeon John Harris built the Indian-style bungalow that'
    #                    ' occupies the land today. 9 Ruse Street Harris Park 2150, 02 9635 5655. Open: Wednesday to '
    #                    'Sunday 10:30am – 3:30pm. Last tour at 3:00pm. Available for group bookings Mondays and '
    #                    'Tuesdays.  Visit the National Trust website for more information.'
    # },
    # {
    #     'name': 'Whitlam Institute at the former Female Orphan School',
    #     'description': 'The building was commissioned in 1813 by Governor Macquarie to provide a place to prepare '
    #                    'orphaned, convict and Indigenous females for life as domestic servants. The building became a'
    #                    ' mental hospital in the 1880s for a century, before falling into disrepair in the mid 1980s. '
    #                    'The present day refurbished building has become an integral part of Western Sydney University '
    #                    '– a wing of which is dedicated to the Whitlam Institute and displays a model of former Prime '
    #                    'Minister Gough Whitlam’s office. Building EZ, corner James Ruse Drive and Victoria Road '
    #                    'Rydalmere 2116, 02 9685 9210. Open: Thursday and Friday 10:00am – 4:00pm. Group bookings are '
    #                    'available on request throughout the week.  Visit the Whitlam Institute website for more '
    #                    'information.'
    # },
    # {
    #     'name': 'Parramatta Female Factory',
    #     'description': 'Follow in the footsteps of the female convicts, within this National Heritage Precinct. Stories'
    #                    ' of convict women’s incarceration experience; earliest dedicated women’s health service; '
    #                    'first worker’s action in Australia and mental health history. The site officially became the '
    #                    'Parramatta Lunatic Asylum in 1850. Over the years the name and function went through many '
    #                    'iterations. Finally, in 1983 the name was changed to Cumberland Hospital, now operating as the'
    #                    ' campus for the Institute of Psychiatry. 5 Fleet Street North Parramatta 2150. Guided tours: '
    #                    'First Friday of the month. Groups by appointment – bookings essential. Visit the Parramatta '
    #                    'Female Factory website for more information.'
    # },
    # {
    #     'name': 'Newington Armoury',
    #     'description': 'What once served as a naval armaments depot has now gained a new life as an arts precinct. '
    #                    'Visit the Armoury Gallery, which was used as an explosives store during WWII and is now used '
    #                    'as a 500sqm contemporary gallery. A great way to take it all in is on the Heritage Railway, '
    #                    'which operates on weekends. Jamieson Street Sydney Olympic Park 2127. Open: Saturday and '
    #                    'Sunday 10:00am – 4:00pm. '
    # },
    # {
    #     'name': 'Parramatta Town Hall',
    #     'description': 'Governor Phillip designated the land for Parramatta’s Town Hall in his early plan for the area '
    #                    'and foundations were laid in 1792. The space around Town Hall was used as a Market Place from '
    #                    '1812 – with the weekly Farmer’s Markets still operating in this space today. Governor Macquarie'
    #                    ' designated the site in front of Town Hall for the Annual Meeting of the Aboriginal Tribes in'
    #                    ' Parramatta from 1816 to 1833. The building still serves the community of Parramatta today.'
    #                    'Centenary Square 182 Church Street Parramatta 2150.'
    # },
    # {
    #     'name': 'Lennox Bridge',
    #     'description': 'Lennox Bridge was completed in 1839 and was designed by David Lennox, then Superintendent of '
    #                    'Bridges for NSW. The bridge replaced two earlier wooden bridges on the same site and is built '
    #                    'from sandstone sourced from the Parramatta Female Factory quarry. Adjacent to 349–351 Church '
    #                    'Street, Parramatta'
    # },
    # {
    #     'name': 'Park Gatehouses',
    #     'description': 'There are six gatehouses in Parramatta Park located at entrances on George Street (the Tudor '
    #                    'Gatehouse), Ross Street, Park Road, Macquarie Street, Great Western Highway at Mays Hill and '
    #                    'Queens Road. These gatehouses date from the 1870s and, as a group, make an important '
    #                    'contribution to the cultural landscape values of the Park. Four of the gatehouses have been '
    #                    'conserved and three are tenanted. The style of the gatehouses reflects their strategic '
    #                    'location, ranging from the grand entrances of the Tudor-style George Street Gatehouse and the '
    #                    'Gothic-style Macquarie Street Gatehouse, to the humble utilitarian entrances of the Park. The '
    #                    'George Street Gatehouse is a key entry point for the Park and an iconic landmark in Parramatta.'
    #                    '  It was built by the Parramatta Park Trust in 1885, on the site of Governor Macquarie’s small '
    #                    'stone lodge. The architect was Scottish born Gordon McKinnon and it was built by local builders'
    #                    ' Hart and Lavors. The wrought iron gates were made by local blacksmith T Forsyth.'
    # },
    # {
    #     'name': 'The Observatory Transit Stones',
    #     'description': 'The observatory was built by Governor Brisbane in 1822 and was used to make some of the most '
    #                    'important early astronomical observations in the southern hemisphere. Two marker trees were '
    #                    'planted to the south of the transit stones with two additional trees in the southern domain '
    #                    '(in the May’s Hill area).  All four trees marked a north-south alignment across the Governor’s '
    #                    'Domain. The observatory building fell into ruin and was demolished in 1848, with only the '
    #                    'transit stones on their plinth left standing.'
    # },
    # {
    #     'name': 'The Bath House',
    #     'description': 'The Bath House was completed in 1823 for Governor Brisbane. It is believed that, due to his war '
    #                    'wounds, the Governor wanted a private place with warm baths. This building has been associated'
    #                    ' with the two colonial architects Francis Greenway and Standish Harris. The Bath House contains'
    #                    ' archaeological remains related to the pumping system which was developed to bring water to the'
    #                    ' Bath House, as well as to heat the water. In 1886 the Park Trustees converted the Bath House '
    #                    'to a pavilion, which is the form in which the building still survives today.'
    # },
    # {
    #     'name': 'Boer War Memorial',
    #     'description': 'The Boer War Memorial was erected in 1904. The memorial is of regional significance for its '
    #                    'commemoration of the first overseas military engagement in which troops representing Australia,'
    #                    ' as distinct to Britain, took part, and is particularly significant as the first of the '
    #                    'Australian troops to arrive in Africa in 1899 to take part in the Boer War came from the Lancer'
    #                    ' Barracks, Parramatta. 100 Lancers from the surrounding districts took part in engagements.'
    # },
    # {
    #     'name': 'Memorial to William (Billy) E. Hart',
    #     'description': 'William E. Hart was the first Australian to fly a plane and the first qualified pilot in '
    #                    'Australia. This memorial commemorates an early pioneering cross country flight, the first in '
    #                    'Australia, from Penrith to Parramatta Park on 4 November 1911 by Hart. Flying against Wizard '
    #                    'Stone of America, Hart won in 23 minutes after Stone lost his way and landed at Lakemba. The '
    #                    'memorial is of cultural significance commemorating an important and enterprising pioneer in '
    #                    'Australian aviation history.'
    # },
    # {
    #     'name': 'Lady FitzRoy Memorial',
    #     'description': 'This memorial was erected to commemorate the place where Lady FitzRoy and the Governor’s Aide, '
    #                    'Lieutenant Charles Masters, were killed when their carriage, driven by Governor FitzRoy, '
    #                    'overturned and hit a tree within the Park in 1847. The event was widely viewed at the time as '
    #                    '‘an irreparable misfortune to the colony’ and marked the beginning of a period of decline of '
    #                    'Government House and the area known as Government Domain.'
    # },
    # {
    #     'name': 'The Settlement at Rose Hill',
    #     'description': 'Governor Phillip knew the success of the colony depended on becoming self sufficient so, after '
    #                    'the failure of the first farm - located at Farm Cove (now the Royal Botanic Gardens, Sydney), '
    #                    'explored the vast harbour in search of fertile land. In April 1788 he discovered the lightly '
    #                    'timbered, open country at the head of the Parramatta River, which offered the prospect of easy '
    #                    'cultivation. A settlement was established on 2nd November 1788, and named Rose Hill in honour '
    #                    'of George Rose, the English Secretary of the Treasury.'
    # },
    # {
    #     'name': 'The Government Farm',
    #     'description': 'The Government Farm was the first successful farm established in the colony.  Henry Edward '
    #                    'Dodd, one of the few experienced farmers in the colony, oversaw the farm and in the spring and'
    #                    ' summer of 1788, 70 acres were cleared and planted.  A barn, a house and a granary were also '
    #                    'established.  In December 1789, the first season produced a "plentiful and luxuriant" vegetable'
    #                    ' crop as well as two hundred bushels of wheat, sixty bushels of barley and a small quantity of '
    #                    'flax, Indian corn and oats.  While this was a pleasing first crop, most of the crop was '
    #                    'reserved for seed, and it was in no way sufficient to feed the colony, which was still '
    #                    'dependent on supply vessels.'
    # }
]

# User data to populate database.
USER_DATA = [
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

# Event data to populate database
EVENT_DATA = [
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

# News Data to populate database
NEWS_DATA = [
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