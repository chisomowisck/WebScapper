import requests
import csv
from bs4 import BeautifulSoup
def myCustomScrap(carMake, makeNumber, rangeStart, rangeEnd):
    page = range(rangeStart, rangeEnd)
    car_make = carMake
    make_number = makeNumber
    tracker = 0
    with open(f'{car_make}.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["MAKE", "MODEL", "YEAR", "REGIST,ERED_ON", "MILEAGE",
                            "ENGINE", "TRANSMISSION", "PRICE", "TOTAL_PRICE"])
    for i in page:
        try:
            URL = f"https://www.beforward.jp/stocklist/make={make_number}/page={i}/sortkey=n"
            page = requests.get(URL)
            row_data = [6]
            soup = BeautifulSoup(page.content, "html.parser")
            results = soup.find(class_="cars-box-stocklist-renewal")
            cars = results.find_all("td", class_="description-col")
            prices = results.find_all("td", class_="price-col")
            print(car_make + " Page " + str(i) + " is done!") 

            for car in range(len(cars)):
                try:
                    #   print(i, a[i])
                    # for car in cars:
                    car_model = cars[car].find("a", class_="vehicle-url-link")
                    car_model = " ".join(car_model.text.split())
                    car_price = cars[car].find(class_="total-price")
                    car_details = cars[car].find_all("p", class_="val")
                    car_year = (car_details[1]).text.strip()
                    car_mileage = (car_details[0]).text.strip()
                    car_engine = (car_details[2]).text.strip()
                    car_transmission = (car_details[3]).text.strip()

                    year = car_model[0:4]
                    make = car_model[5:5 + len(car_make)]
                    model = car_model[6+len(car_make):]

                    row_data = [make, model, year, car_year, car_mileage,
                                car_engine, car_transmission, 1, 1]

                # for price in prices:
                    vehicle_price = (prices[car].find(class_="vehicle-price")).text.strip()
                    total_price = (prices[car].find(class_="total-price")).text.strip()
                    row_data[7] = vehicle_price
                    row_data[8] = total_price

                    # print(total_price)
                    with open(f'{car_make}.csv', 'a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow(row_data)
                except:
                    print("Data Maniputation exception occurred")
        except:
            print("Connection exception occurred")

    print("All " + car_make + " pages are scrapped!!!")


myCustomScrap("TOYOTA", 1, 1, 1644)
myCustomScrap("HONDA", 2, 1, 757)
myCustomScrap("NISSAN", 3, 1, 912)
myCustomScrap("MAZDA", 4, 1, 333)
myCustomScrap("SUZUKI", 7, 1, 1044)
myCustomScrap("MITSUBISHI", 5, 1, 324)
myCustomScrap("ISUZU", 8, 1, 115)
myCustomScrap("SUBARU", 94, 1, 276)
myCustomScrap("DAIHATSU", 10, 1, 879)
myCustomScrap("LEXUS", 68, 1, 121)
myCustomScrap("HINO", 103, 1, 61)
myCustomScrap("MERCEDES-BENZ", 106, 1, 416)
myCustomScrap("BMW", 83, 1, 492)
myCustomScrap("VOLKSWAGEN", 48, 1, 206)
myCustomScrap("AUDI", 47, 1, 136)
myCustomScrap("JAGUAR", 79, 1, 45)
myCustomScrap("LAND ROVER", 52, 1, 254)
myCustomScrap("PEUGEOT", 73, 1, 102)
myCustomScrap("FORD", 50, 1, 81)
myCustomScrap("KIA", 313, 1, 450)
myCustomScrap("HYUNDAI", 44, 1, 544)
myCustomScrap("SSANGYONG", 244, 1, 26)
myCustomScrap("RENAULT SAMSUNG", 263, 1, 9)
myCustomScrap("VOLVO", 57, 1, 85)
myCustomScrap("JEEP", 205, 1, 88)
myCustomScrap("CHEVROLET", 72, 1, 49)
# myCustomScrap("INFINITI", 11, 1, 3)
# myCustomScrap("PORSCHE", 16, 1, 3)
# myCustomScrap("MINI", 19, 1, 3)
# myCustomScrap("ROVER", 20, 1, 3)
# myCustomScrap("CITROEN", 22, 1, 3)
# myCustomScrap("DAEWOO", 26, 1, 3)
# myCustomScrap("CHRYSLER", 28, 1, 3)
# myCustomScrap("DODGE", 29, 1, 3)
# myCustomScrap("RAM", 31, 1, 3)
# myCustomScrap("GMC", 32, 1, 3)
# myCustomScrap("BUICK", 33, 1, 3)
# myCustomScrap("CADILLAC", 34, 1, 3)
# myCustomScrap("OLDSMOBILE", 35, 1, 3)
# myCustomScrap("PONTIAC", 36, 1, 3)
# myCustomScrap("SAAB", 37, 1, 3)
# myCustomScrap("ALFA ROMEO", 39, 1, 3)
# myCustomScrap("FIAT", 40, 1, 3)
# myCustomScrap("LAMBORGHINI", 41, 1, 3)
# myCustomScrap("MASERATI", 42, 1, 3)
# myCustomScrap("MCLAREN", 43, 1, 3)
# myCustomScrap("ROLLS-ROYCE", 44, 1, 3)
# myCustomScrap("BENTLEY", 45, 1, 3)
# myCustomScrap("ASTON MARTIN", 46, 1, 3)
# myCustomScrap("LOTUS", 47, 1, 3)
# myCustomScrap("TESLA", 48, 1, 3)
# myCustomScrap("SMART", 49, 1, 3)
# myCustomScrap("OTHERS", 50, 1, 3)