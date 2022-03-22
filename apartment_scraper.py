from bs4 import BeautifulSoup
import requests

html_info = requests.get("https://pennstate.craigslist.org/search/apa")

soup = BeautifulSoup(html_info.text, 'lxml')

listings = soup.find_all('li', class_="result-row")

input_choice = input('Do you want to live with roommates?: ')
if input_choice in ['yes', 'Yes', 'y', 'YES', 'Y']:
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


        print(f"\nDate Posted: {day_posted.text}"
              f"\nPosting:{post_of_flat.text}"
              f"Number of bedrooms: {bedroom_num}"
              f"\nPrice per month: {listing_price.text}"
              f"\nPrice per student: ${cost_per_person(bedroom_num, price_of_apartment)}"
              f"\nLink to main website: {main_website}")

else:
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



        print(f"\nDate Posted: {day_posted.text}"
              f"\nPosting:{post_of_flat.text}"
              f"Number of bedrooms: {bedroom_num}"
              f"\nPrice per month: {listing_price.text}"
              f"\nLink to main website: {main_website}")
