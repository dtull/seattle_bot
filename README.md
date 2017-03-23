# seattle_bot
Tell seattle_bot what neighborhood you live in, and it'll tell you all the online communities for your area!


Given a user’s ‘Seattle Neighborhood’ input, this bot lists out the number of online communities in that Seattle neighborhood along with the names and website links to each online community.

Data for this bot is provided by the City of Seattle's open data portal. The dataset "Seattle Communities Online Inventory" was created by the City of Seattle's Department of Information Technology.
It provides a list of websites, blogs, wikis, Twitter feeds, and Facebook pages associated with neighborhood-specific groups and organizations.

Inspiration for this bot stemmed from our research into data available in Seattle. On the official City of Seattle website there are pages with information on how to connect with community members online.
They claim to be moving the city forward into the digital world. Their “Neighborhoods on the Net” projects aims to connect neighbors through the web. We designed the bot to add convenience to the hunt for online communities in Seattle.
We figure someone moving to Seattle would appreciate some help in finding ways to socialize through online communities.

Finding this data wasn’t difficult. However, we faced some trouble in parsing the data, which was only available in json. We had to read up on json notation.
As you will see in the code we grab the urls for a given community then provide the list in our make_story function with the number and names of the communities.
If a user's input is not a neighborhood in Seattle we provide a list of the neighborhoods.  

To help with our bot here is a list of neighborhoods in Seattle:

Admiral
Alki
Arbor Heights
Ballard
Beacon Hill
Belltown
Blue Ridge
Brighton
Broadview
Capitol Hill
Central District
Chinatown International District
Colman
Columbia City
Crown Hill
Delridge
Downtown
Duwamish
Eastlake
Fauntleroy
First Hill
Fremont
Fremont
Genesee-Schmitz
Georgetown
Green Lake
Greenwood
Haller Lake
Hawthorne Hills
Highland Park
Hillman City
Industrial District
Junction
Lake City
Lake Union
Lakewood/Seward Park
Laurelhurst
Leschi
Lewis Park
Licton Springs
Lockmore
Madison Park
Madrona
Magnolia
Magnolia Queen Anne
Maple Leaf
Meadowbrook
Miller Park
Morgan Junction
Mount Baker
North Beacon Hill
Northeast Seattle
Northgate
Northwest
Othello
Phinney Ridge
Pinehurst
Pioneer Square
Queen Anne
Rainier Beach
Rainier Valley
Ravenna
Regional Sites
Roosevelt
Roxhill
Seward Park
South Lake Union
South Park
Thornton Creek
University District
Uptown
Wallingford
Wedgwood
Wedgwood
West Seattle
West Woodland
Westwood
White Center


How to use this bot:

import bot
bot.bot(Beacon Hill')

output:
There are 5 online communities in Beacon Hill. Here are the names and links to the websites:
['Beacon BIKES', 'https://www.facebook.com/pages/Beacon-BIKES/123320897689573?sk=info&ref=page_internal'],
['Beacon Hill Blog', 'http://beaconhill.seattle.wa.us/'],
['Beacon Hill Merchants Association', 'http://www.beaconhillmerchants.com/'],
['North Beacon Hill Council', 'http://www.northbeaconhillcouncil.org/'],
['North Beacon Hill Council Facebook Page', 'https://www.facebook.com/NorthBeaconHillCouncil']
