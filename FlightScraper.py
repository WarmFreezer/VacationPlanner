from FlightData import FlightData

class FlightScraper:
    #Trip information
    departure: str
    destination: str
    d_date: str
    r_date: str
    fliers: int

    #Flight information to collect
    SELECTORS = {
        "airline": "div.sSHqwe.tPgKwe.ogfYpf",
        "departure_time": 'span[aria-label^="Departure time"]',
        "price": "div.FpEdX span"}

    #Function to return a list of flights and their information
    async def GetFlights(self, page, params: FlightData) -> list[FlightData]:
        #Locates the ticket type button, clicks it, waits for the field to appear, and type in ticket type
        ticket_type = page.locator("div.VfPpkd-TkwUic[jsname='oYxtQd']").first
        await ticket_type.click()
        await page.wait_for_selector("ul[aria-label='Select your ticket type.']")
        await page.locator("li").filter(has_text="Two way").nth(0).click() #For the vacation planner, Im going with the assumption of round trips so I predefined two-way ticket

        #Locates the departure location field, clicks on it, and fills in the departure location
        from_input = page.locator("input[aria-label='Where from?']")
        await from_input.click()
        await from_input.fill("")
        await page.keyboard.type(self.departure)

        #If there are more flights not initially listed, locates and clicks the more flights button.
        #If there aren't more flights, continue
        while True:
            try:
                more_button = await page.wait_for_selector('button[aria-label*="more flights"]', timeout=5000)
                if more_button:
                    await more_button.click()
                    await page.wait_for_timeout(2000)
                else:
                    break
            except:
                break

        #Waits for more flights to appear if applicable and loads all flights on the page
        await page.wait_for_selector("li.pIav2d", timeout=30000)
        await self._load_all_flights(page)

        #Places all the flights into an array and creates an array that'll hold the formatted information
        flights = await page.query_selector_all("li.pIav2d")
        flights_data = []

        #Runs through each flight in flights and parses the information into the formatted array
        for flight in flights:
            flight_info = {}
            for key, selector in self.SELECTORS.items():
                element = await flight.query_selector(selector)
                flight_info[key] = await self._extract_text(element)
                flights_data.append(FlightData(**flight_info))
        #Returns flights_data as a list of flights
        return flights_data




