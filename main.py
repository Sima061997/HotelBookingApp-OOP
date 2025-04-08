import pandas

df = pandas.read_csv("hotels.csv")
df_cards = pandas.read_csv("cards.csv", dtype=str).to_dict(orient="records")
df_card_security = pandas.read_csv("card_security.csv", dtype=str)


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


class Creditcard:

    def __init__(self, number):
        self.number = number

    def validate(self, expiration, holder, cvc):
        card_data = {"number":self.number, "expiration":expiration,
                     "holder":holder, "cvc":cvc}
        if card_data in df_cards:
            return True
        else:
            return False


#Inheritance from Creditcard superclass
class SecureCreditCard(Creditcard):
    def authenticate(self, given_password):
        password = df_card_security.loc[df_card_security["number"] == self.number, "password"].squeeze()
        if password == given_password:
            return True
        else:
            return False


print(df)
hotel_name = input("Give the name of the Hotel: ")

if hotel_name not in df["name"].values:
    print(f"{hotel_name} is not Available!")
else:
    hotel = Hotel(hotel_name)
    if hotel.available():
        credit_card = SecureCreditCard("123456789")
        if credit_card.validate("12/26", "JOHN SMITH", "123"):
            if credit_card.authenticate(given_password="mypass"):
                hotel.book()
                customer_name = input("Give your name: ")
                reserve_hotel = Reservation(customer_name, hotel)
                print(reserve_hotel.reserve())
            else:
                print("Credit Card authentication failed")
        else:
            print("Credit Card not valid")
    else:
        print("All rooms are already reserved! Sorry!!")

