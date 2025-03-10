import googlemaps 
from data import navigate_website
from scrape import find_wait_times
from tabulate import tabulate
API_KEY = "" # Please insert your own google maps API key
origin = input("Origin: ")
destination = input("Destination: ")
departure_time = input("Departure time (in H:MM format): ") 
# origin = "Montreal, QC"
# destination = "Boston, MA"
departure_time = departure_time.split(":")
departure_time = int(departure_time[0])


gmaps = googlemaps.Client(key=API_KEY)

# Finds long and lat given location
def geocode_address(address):
    geocode_result = gmaps.geocode(address)
    location = geocode_result[0]['geometry']['location']
    return location

# Finds travel time in {H:MM} format and seconds in a dictionary
def travel_time(origin, destination, mode="driving"):
    time = gmaps.distance_matrix(origin, destination, mode)
    seconds = time['rows'][0]['elements'][0]['duration']
    return seconds
 
# Main function
def get_directions(origin, destination, departure_time):
    brr = []
    # Finds different paths to destination
    directions = gmaps.directions(origin, destination, alternatives=True, mode='driving') #gives directions and all that
    boo = False
    for i in range(len(directions)):
        boo = False
        steps = directions[i]['legs'][0]['steps'] # gives instructions step by step on how to get from a to b
        
        # Filters through steps to check which border is crossed
        for step in steps: 
            if 'Entering the United States of America' in step['html_instructions']: #checking in the instructions when border is crossed
                
                # Checks for nearby borders and ranked by distance
                nearby = gmaps.places_nearby(location=step['end_location'], name="U.S. Customs and Border Protection", rank_by='distance') 
                
                # Iterating through nearest results
                for result in nearby['results']: 
                    arr = []
                    # Uses first border found
                    if 'U.S. Customs and Border Protection' in result['name'] and 'Patrol Station' not in result['name']: #making sure they're actually us borders
                        # result['name'] is like "U.S. Customs and Border Protection - Rouses Point Port of Entry"
                        coords = geocode_address(result['name'])
                        
                        # Calculates time for this path by time to border + border to destination + border wait times
                        to_border = travel_time(origin, coords)
                        b_to_dest = travel_time(coords, destination)
                        total_time = to_border['value'] + b_to_dest['value']
                        # print(f"Time before: {total_time}")

                        # Converts to readable time
                        hours = total_time//3600
                        minutes = (total_time - ((total_time//3600)*3600))//60
                        if minutes <=9:
                            minutes=f"0{minutes}"
                        time = f"{hours}:{minutes}" 
                        arr.append(time)

                        rez = result['name']
                        
                        # print(f"Border before: {rez}")
                        rez = rez.replace("U.S. Customs and Border Protection", "")
                        rez = rez.replace(" Port of Entry", "") 
                        # print(f"Border after : {rez}")

                        # Finds link of times for given border
                        # nav = navigate_website(rez)
                        urls = navigate_website(rez)
                        
                        
                        wait_times = 0
                        if urls == None:
                            arr.append(rez)
                        else:
                            url = urls[0]
                            # print(urls[1])
                            arr.append(urls[1])
                            time_at_border = int(departure_time) + int(to_border['text'].split()[0])
                            if time_at_border == 12:
                                time_at_border = "Noon"
                            elif time_at_border > 12:
                                time_at_border -=12
                                time_at_border = f"{time_at_border}:00 PM"
                            else:
                                time_at_border = f"{time_at_border}:00 AM"
                            # print(f" Time at border: {time_at_border}")
                            
                            # With border specific wait time link + time to reach border, wait times are returned                            
                            wait_times = find_wait_times(url, time_at_border)
                            wait_times = int(wait_times)
                            wait_times*=60
                            # print(f"Wait times: {wait_times}")
                            total_time += wait_times
                        arr.append(f"{wait_times//60} minutes")
                        # print(f"Total time after: {total_time}")
                        hours = total_time//3600
                        minutes = (total_time - ((total_time//3600)*3600))//60
                        if minutes <=9:
                            minutes=f"0{minutes}"
                        final_time = f"{hours}:{minutes}"
                        arr.append(final_time)
                        # print(final_time)
                        boo = True
                        break
            
            if boo:
                break
        # print('----------------------------------')   
        if arr in brr:
            pass
        else:
            brr.append(arr) 
          
    return brr        
a = get_directions(origin, destination, departure_time)
table = tabulate(
    a, 
    headers=["Time Without Border", "Border Name", "Wait Times", "Final Time"], 
    tablefmt="grid"
)
print(table)