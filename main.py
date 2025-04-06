import pandas

df = pandas.read_csv("hotels.csv")


class Hotel:
    def __init__(self, name):
        self.name = name
        self.city = df.loc[df["name"] == self.name, "city"].squeeze()

    def book(self):
        """Book a hotel by changing it's availability to no"""
        df.loc[df["name"] == self.name, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        availability = df.loc[df["name"] == self.name, "available"].squeeze()
        if availability == "yes":
           return True
        else:
            return False


class Reservation:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def reserve(self):
        content = f"""Thank you for your Booking!
        Here are your booking date:
        Name: {self.customer_name}
        Hotel Name: {self.hotel.name}
        City: {self.hotel.city}
        """
        return content


print(df)
hotel_name = input("Give the name of the Hotel: ")


if hotel_name not in df["name"].values:
    print(f"{hotel_name} is not Available!")

else:
    hotel = Hotel(hotel_name)

    if hotel.available():
        hotel.book()
        customer_name = input("Give your name: ")
        reserve_hotel = Reservation(customer_name, hotel)
        print(reserve_hotel.reserve())
    else:
        print("All rooms are already reserved! Sorry!!")

