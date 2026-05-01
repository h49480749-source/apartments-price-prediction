import requests
from bs4 import BeautifulSoup
import pandas as pd

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept-Language": "en-US,en;q=0.9"
}


def scrape():
    data = []

    for i in range(1, 100):
        print(f"Scraping page {i}")

        url = f"https://www.dubizzle.com.eg/en/properties/apartments-duplex-for-sale/5th-settlement/?page={i}&filter=type_eq_1"

        try:
            response = requests.get(url, headers=HEADERS, timeout=10)
            soup = BeautifulSoup(response.text, "lxml")
        except Exception as e:
            print(f"Failed to load page {i}: {e}")
            continue

        items = soup.find_all("article")

        for item in items:
            try:
                link = item.find("a")["href"]
                full_url = "https://www.dubizzle.com.eg" + link

                response = requests.get(full_url, headers=HEADERS, timeout=10)
                soup = BeautifulSoup(response.text, "lxml")

                # -------- Basic fields --------
                price = soup.find("span", attrs={"aria-label": "Price"})
                price = price.text if price else None

                Posted_by = soup.find("span", string="Posted by")
                Posted_by = Posted_by.find_next_sibling("span").text if Posted_by else None

                Area = soup.find("span", string="Area (m²)")
                Area = Area.find_next_sibling("span").text if Area else None

                Bedrooms = soup.find("span", string="Bedrooms")
                Bedrooms = Bedrooms.find_next_sibling("span").text if Bedrooms else None

                payment = soup.find("span", string="Payment Option")
                payment = payment.find_next_sibling("span").text if payment else None

                status = soup.find("span", string="Completion status")
                status = status.find_next_sibling("span").text if status else None

                ownership = soup.find("span", string="Ownership")
                ownership = ownership.find_next_sibling("span").text if ownership else None

                Bathrooms = soup.find("span", string="Bathrooms")
                Bathrooms = Bathrooms.find_next_sibling("span").text if Bathrooms else None

                Location = soup.find("span", attrs={"aria-label": "Location"})
                Location = Location.text if Location else None

                # -------- Amenities --------
                amenities = {
                    "PrivateGarden": 0,
                    "Pool": 0,
                    "Electricity_Meter": 0,
                    "Water_Meter": 0,
                    "Natural_Gas": 0,
                    "Landline": 0,
                    "Covered_Parking": 0,
                    "Security": 0,
                    "Balcony": 0,
                }

                for span in soup.find_all("span"):
                    text = span.get_text(strip=True)

                    if "Private Garden" in text:
                        amenities["PrivateGarden"] = 1
                    if "Pool" in text:
                        amenities["Pool"] = 1
                    if "Electricity Meter" in text:
                        amenities["Electricity_Meter"] = 1
                    if "Water Meter" in text:
                        amenities["Water_Meter"] = 1
                    if "Natural Gas" in text:
                        amenities["Natural_Gas"] = 1
                    if "Landline" in text:
                        amenities["Landline"] = 1
                    if "Covered Parking" in text:
                        amenities["Covered_Parking"] = 1
                    if "Security" in text:
                        amenities["Security"] = 1
                    if "Balcony" in text:
                        amenities["Balcony"] = 1

                print(price)

                data.append({
                    "Area": Area,
                    "Payment": payment,
                    "Posted_by": Posted_by,
                    "Ownership": ownership,
                    "Status": status,
                    "Bedrooms": Bedrooms,
                    "Bathrooms": Bathrooms,
                    "Location": Location,
                    "price": price,
                    **amenities
                })

            except Exception as e:
                print(f"Error scraping item: {e}")
                continue

        # Stop if no next page
        nxt = soup.find("div", title="Next")
        if nxt and not nxt.find_parent("a"):
            break

    return data


if __name__ == "__main__":
    results = scrape()

    df = pd.DataFrame(results)
    df.to_csv("data.csv", index=False)

    print(f"\nScraping finished. Saved {len(df)} rows to data.csv")