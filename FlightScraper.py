from FlightData import FlightData

class FlightScraper:
    #Trip information
    departure: str
    destination: str
    d_date: str
    r_date: str
    budget: float
    fliers: int
    rental: bool

    SELECTORS = {
        "airline": "div.sSHqwe.tPgKwe.ogfYpf",
        "departure_time": 'span[aria-label^="Departure time"]',
        "price": "div.FpEdX span"}

    #Function to return flight data
    async def GetFlightData(self, page, params: FlightData) -> list[FlightData]:
        ticket_type = page.locator("div.VfPpkd-TkwUic[jsname='oYxtQd']").first
        await ticket_type.click()
        await page.wait_for_selector("ul[aria-label='Select your ticket type.']")
        await page.locator("li").filter(has_text="Two way").nth(0).click()

        from_input = page.locator("input[aria-label='Where from?']")
        await from_input.click()
        await from_input.fill("")
        await page.keyboard.type(FlightScraper.departure)

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

        await page.wait_for_selector("li.pIav2d", timeout=30000)
        await self._load_all_flights(page)

        flights = await page.query_selector_all("li.pIav2d")
        flights_data = []

        for flight in flights:
            flight_info = {}
            for key, selector in self.SELECTORS.items():
                element = await flight.query_selector(selector)
                flight_info[key] = await self._extract_text(element)
                flights_data.append(FlightData(**flight_info))
        return flights_data




