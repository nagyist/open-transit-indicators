""" Helper classes with GTFS functions and data definitions """
from django.utils.translation import ugettext_lazy as _


class GTFSRouteTypes(object):
    """ All available GTFS route types

    Used by transit_indicators.models.GTFSRouteType
    The integer for each choice must be unique

    """
    CHOICES = (
        (0, _('Tram, Light Rail, Streetcar')),
        (1, _('Subway, Metro')),
        (2, _('Rail')),
        (3, _('Bus')),
        (4, _('Ferry')),
        (5, _('Cable Car')),
        (6, _('Gondola, Suspended cable car')),
        (7, _('Funicular')),
        (100, _('Railway Service')),
        (101, _('High Speed Rail Service')),
        (102, _('Long Distance Trains')),
        (103, _('Inter Regional Rail Service')),
        (104, _('Car Transport Rail Service')),
        (105, _('Sleeper Rail Service')),
        (106, _('Regional Rail Service')),
        (107, _('Tourist Railway Service')),
        (108, _('Rail Shuttle (Within Complex)')),
        (109, _('Suburban Railway')),
        (110, _('Replacement Rail Service')),
        (111, _('Special Rail Service')),
        (112, _('Lorry Transport Rail Service')),
        (113, _('All Rail Services')),
        (114, _('Cross-Country Rail Service')),
        (115, _('Vehicle Transport Rail Service')),
        (116, _('Rack and Pinion Railway')),
        (117, _('Additional Rail Service')),
        (200, _('Coach Service')),
        (201, _('International Coach Service')),
        (202, _('National Coach Service')),
        (203, _('Shuttle Coach Service')),
        (204, _('Regional Coach Service')),
        (205, _('Special Coach Service')),
        (206, _('Sightseeing Coach Service')),
        (207, _('Tourist Coach Service')),
        (208, _('Commuter Coach Service')),
        (209, _('All Coach Services')),
        (300, _('Suburban Railway Service')),
        (400, _('Urban Railway Service')),
        (401, _('Metro Service')),
        (402, _('Underground Service')),
        (403, _('Urban Railway Service')),
        (404, _('All Urban Railway Services')),
        (405, _('Monorail')),
        (500, _('Metro Service')),
        (600, _('Underground Service')),
        (700, _('Bus Service')),
        (701, _('Regional Bus Service')),
        (702, _('Express Bus Service')),
        (703, _('Stopping Bus Service')),
        (704, _('Local Bus Service')),
        (705, _('Night Bus Service')),
        (706, _('Post Bus Service')),
        (707, _('Special Needs Bus')),
        (708, _('Mobility Bus Service')),
        (709, _('Mobility Bus for Registered Disabled')),
        (710, _('Sightseeing Bus')),
        (711, _('Shuttle Bus')),
        (712, _('School Bus')),
        (713, _('School and Public Service Bus')),
        (714, _('Rail Replacement Bus Service')),
        (715, _('Demand and Response Bus Service')),
        (716, _('All Bus Services')),
        (800, _('Trolleybus Service')),
        (900, _('Tram Service')),
        (901, _('City Tram Service')),
        (902, _('Local Tram Service')),
        (903, _('Regional Tram Service')),
        (904, _('Sightseeing Tram Service')),
        (905, _('Shuttle Tram Service')),
        (906, _('All Tram Services')),
        (1000, _('Water Transport Service')),
        (1001, _('International Car Ferry Service')),
        (1002, _('National Car Ferry Service')),
        (1003, _('Regional Car Ferry Service')),
        (1004, _('Local Car Ferry Service')),
        (1005, _('International Passenger Ferry Service')),
        (1006, _('National Passenger Ferry Service')),
        (1007, _('Regional Passenger Ferry Service')),
        (1008, _('Local Passenger Ferry Service')),
        (1009, _('Post Boat Service')),
        (1010, _('Train Ferry Service')),
        (1011, _('Road-Link Ferry Service')),
        (1012, _('Airport-Link Ferry Service')),
        (1013, _('Car High-Speed Ferry Service')),
        (1014, _('Passenger High-Speed Ferry Service')),
        (1015, _('Sightseeing Boat Service')),
        (1016, _('School Boat')),
        (1017, _('Cable-Drawn Boat Service')),
        (1018, _('River Bus Service')),
        (1019, _('Scheduled Ferry Service')),
        (1020, _('Shuttle Ferry Service')),
        (1021, _('All Water Transport Services')),
        (1100, _('Air Service')),
        (1101, _('International Air Service')),
        (1102, _('Domestic Air Service')),
        (1103, _('Intercontinental Air Service')),
        (1104, _('Domestic Scheduled Air Service')),
        (1105, _('Shuttle Air Service')),
        (1106, _('Intercontinental Charter Air Service')),
        (1107, _('International Charter Air Service')),
        (1108, _('Round-Trip Charter Air Service')),
        (1109, _('Sightseeing Air Service')),
        (1110, _('Helicopter Air Service')),
        (1111, _('Domestic Charter Air Service')),
        (1112, _('Schengen-Area Air Service')),
        (1113, _('Airship Service')),
        (1114, _('All Air Services')),
        (1200, _('Ferry Service')),
        (1300, _('Telecabin Service')),
        (1301, _('Telecabin Service')),
        (1302, _('Cable Car Service')),
        (1303, _('Elevator Service')),
        (1304, _('Chair Lift Service')),
        (1305, _('Drag Lift Service')),
        (1306, _('Small Telecabin Service')),
        (1307, _('All Telecabin Services')),
        (1400, _('Funicular Service')),
        (1401, _('Funicular Service')),
        (1402, _('All Funicular Service')),
        (1500, _('Taxi Service')),
        (1501, _('Communal Taxi Service')),
        (1502, _('Water Taxi Service')),
        (1503, _('Rail Taxi Service')),
        (1504, _('Bike Taxi Service')),
        (1505, _('Licensed Taxi Service')),
        (1506, _('Private Hire Service Vehicle')),
        (1507, _('All Taxi Services')),
        (1600, _('Self Drive')),
        (1601, _('Hire Car')),
        (1602, _('Hire Van')),
        (1603, _('Hire Motorbike')),
        (1604, _('Hire Cycle')),
        (1700, _('Miscellaneous Service')),
        (1701, _('Horse-drawn Carriage')),
    )
