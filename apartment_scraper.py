from bs4 import BeautifulSoup
import requests
import json

html_info = requests.get("https://pennstate.craigslist.org/search/apa")

soup = BeautifulSoup(html_info.text, 'lxml')

listings = soup.find_all('li', class_="result-row")

json_file_full_rent = []
json_file_rent = []


for listing in listings:
    links = []

    day_posted = listing.find('time', class_='result-date')
    listing_price = listing.find('span', class_= 'result-price')
    post_of_flat = listing.find('h3', class_='result-heading')
    main_website = listing.a['href']
    num_bedrooms = listing.find('span', class_= 'shared-line-bubble')


    links.append(main_website)
    for link in links:
        html_in = requests.get(link)
        soup = BeautifulSoup(html_in.text, 'lxml')

        linkers= soup.find('p', class_="attrgroup")
        rooms = linkers.find('span', class_='shared-line-bubble')

        bedrooms = rooms.text
        bedroom_num = float(bedrooms[0:1])



    house_price = listing_price.text
    if ',' in house_price:
        price_of_apartment = float(house_price[1:].replace(',', ''))
    else:
        price_of_apartment = float(house_price[1:])


    def cost_per_person(num_rooms, num_prices):

        if num_rooms == 1 or num_rooms == 0:
            return str(num_prices)
        else:
            return num_prices/num_rooms

    json_listing = {
        "listings": {
        "Posting Date": day_posted.text,
        "Post Name": post_of_flat.text,
        "Number of Bedrooms": bedroom_num,
        "Price Per Month": listing_price.text,
        "Price Per Student": cost_per_person(bedroom_num, price_of_apartment),
        "Link to Main Post": main_website
        }
    }


    json_file_full_rent.append(json_listing)






for listing in listings:
    links = []

    day_posted = listing.find('time', class_='result-date')
    listing_price = listing.find('span', class_='result-price')
    post_of_flat = listing.find('h3', class_='result-heading')
    main_website = listing.a['href']
    num_bedrooms = listing.find('span', class_='shared-line-bubble')

    links.append(main_website)
    for link in links:
        html_in = requests.get(link)
        soup = BeautifulSoup(html_in.text, 'lxml')

        linkers = soup.find('p', class_="attrgroup")
        rooms = linkers.find('span', class_='shared-line-bubble')

        bedrooms = rooms.text
        bedroom_num = float(bedrooms[0:1])

    house_price = listing_price.text
    if ',' in house_price:
        price_of_apartment = float(house_price[1:].replace(',', ''))
    else:
        price_of_apartment = float(house_price[1:])


    def cost_per_person(num_rooms, num_prices):

        if num_rooms == 1 or num_rooms == 0:
            return str(num_prices)
        else:
            return num_prices / num_rooms

    json_listing2 = {
        "listings": {
        "Posting Date": day_posted.text,
        "Post Name": post_of_flat.text,
        "Number of Bedrooms": bedroom_num,
        "Price Per Month": price_of_apartment,
        "Link to Main Post": main_website
            }
        }
    json_file_rent.append(json_listing2)

# Serializing json
json_object = json.dumps(json_file_full_rent, indent=4)
json_object2 = json.dumps(json_file_rent, indent=3)

with open("listings_roommates.json", "w+") as outfile:
    outfile.write(json_object)
    outfile.close()

with open("listings.json", 'w+') as outfile2:
    outfile2.write(json_object2)
    outfile2.close()


