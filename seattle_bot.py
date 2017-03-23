from seattle_scraper import get_urls_for_hood
from seattle_scraper import get_data
import requests

def make_story(user_location, items):
    storytemplate = """There are {count} online communities in {hood}. Here are the names and links to the websites:
    {info}"""

    info = ', \n'.join(str(v) for v in items)
    story = storytemplate.format(count=len(items),
        hood=user_location,
        info=info
        )
    print(story)

def bot(user_location):
    items = get_urls_for_hood(user_location)

    list_of_hoods = ['Admiral', 'Alki', 'Arbor Heights', 'Ballard', 'Beacon Hill', 'Belltown', 'Blue Ridge', 'Brighton', 'Broadview', 'Capitol Hill', 'Central District', 'Chinatown International District', 'Colman', 'Columbia City', 'Crown Hill', 'Delridge', 'Downtown', 'Duwamish', 'Eastlake',
    'Fauntleroy', 'First Hill', 'Fremont', 'Fremont', 'Genesee-Schmitz', 'Georgetown', 'Green Lake', 'Greenwood', 'Haller Lake', 'Hawthorne Hills', 'Highland Park', 'Hillman City', 'Industrial District', 'Junction', 'Lake City', 'Lake Union', 'Lakewood/Seward Park', 'Laurelhurst', 'Leschi', 'Lewis Park', 'Licton Springs', 'Lockmore', 'Madison Park', 'Madrona',
    'Magnolia', 'Queen Anne', 'Maple Leaf', 'Meadowbrook', 'Miller Park', 'Morgan Junction', 'Mount Baker', 'North Beacon Hill',
    'Northeast Seattle', 'Northgate', 'Northwest', 'Othello', 'Phinney Ridge', 'Pinehurst', 'Pioneer Square', 'Queen Anne', 'Rainier Beach', 'Rainier Valley',
    'Rainier Valley', 'Rainier Beach', 'Ravenna', 'Regional Sites', 'Roosevelt', 'Roxhill', 'Seward Park', 'South Lake Union', 'South Park',
    'Thornton Creek', 'University District', 'Uptown', 'Wallingford', 'Wedgwood', 'West Seattle', 'West Woodland', 'Westwood', 'White Center']

    mylist = ', \n'.join(str(v) for v in list_of_hoods)
    if user_location in list_of_hoods:
        make_story(user_location, items)
    else:
        print("That's not a neighborhood in Seattle! Here is a list of Seattle neighborhoods:", '\n', mylist)
