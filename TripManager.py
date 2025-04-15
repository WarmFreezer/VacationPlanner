#Internal libraries here
import WebSearchAI
import FlightScraper

def MainSearch():
    #budget 
    #departure
    destinationState = "Kentucky"
    d_date = "2025-05-09"
    r_date = "2025-05-16"
    vacationers = "2"
    #rental

    housingUrl = "www.airbnb.com/s/" + destinationState + "/homes?refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=" + d_date + "&monthly_length=3&monthly_end_date=" + r_date + "&price_filter_input_type=0&channel=EXPLORE&date_picker_type=calendar&checkin=" + d_date + "&checkout=" + r_date + "&adults=5"
    housingPrompt = "Extract the price and location dates of vacation rentals from this page."

    searchVacations = WebSearchAI.SearchWeb(housingUrl, housingPrompt)

"""
flightData #List for departing flights which need to be passed to WebSearchAI to find an itinerary on the destination city (Odd indexes should be departing flights)
vacationData #List for vacation info which will be combined with flightData to creat a list of trip objects
tripList #Will need to define a new object based on all departing flights, not returning ones
"""