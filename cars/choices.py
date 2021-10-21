availibility_choices = (
    ("Rent", "For Rent"),
    ("Sale", "For Sale"),
    ("Not available", "Not available"),
)


details_choices={
    "Body Style": "body_style",  # exemple: Convertible,
    "Engine": "engine",  # exemple: 3.4L Mid-Engine V6,
    "Transmission": "transmission",  # exemple: 6-speed Manual,
    "Miles": "miles",  # exemple: 12,
    "Doors": "doors",  # exemple: 2,
    "Passengers": "passengers",  # exemple: 2,
    "Fuel Type": "fuel_type",  # exemple: Gasoline,
    "Condition": "condition",  # exemple: Brand New,
    "Color": "color",  # exemple: Black,
    
    "Fuel Mileage": None,  # exemple: 20 City / 28 Hwy,
    "Owners": None,  # exemple: N/A,
    "Waeeanty": None,  # exemple: 3 Years Limited    
    "Drivetrain": None,  # exemple: Rear Wheel Drive,
    "Exaterion": None,  # exemple: Lime Gold Metallic,
    "Interior": None,  # exemple: Agate Grey,
}
state_choices = (
    ("AL", "Alabama"),
    ("AK", "Alaska"),
    ("AZ", "Arizona"),
    ("AR", "Arkansas"),
    ("CA", "California"),
    ("CO", "Colorado"),
    ("CT", "Connecticut"),
    ("DE", "Delaware"),
    ("DC", "District Of Columbia"),
    ("FL", "Florida"),
    ("GA", "Georgia"),
    ("HI", "Hawaii"),
    ("ID", "Idaho"),
    ("IL", "Illinois"),
    ("IN", "Indiana"),
    ("IA", "Iowa"),
    ("KS", "Kansas"),
    ("KY", "Kentucky"),
    ("LA", "Louisiana"),
    ("ME", "Maine"),
    ("MD", "Maryland"),
    ("MA", "Massachusetts"),
    ("MI", "Michigan"),
    ("MN", "Minnesota"),
    ("MS", "Mississippi"),
    ("MO", "Missouri"),
    ("MT", "Montana"),
    ("NE", "Nebraska"),
    ("NV", "Nevada"),
    ("NH", "New Hampshire"),
    ("NJ", "New Jersey"),
    ("NM", "New Mexico"),
    ("NY", "New York"),
    ("NC", "North Carolina"),
    ("ND", "North Dakota"),
    ("OH", "Ohio"),
    ("OK", "Oklahoma"),
    ("OR", "Oregon"),
    ("PA", "Pennsylvania"),
    ("RI", "Rhode Island"),
    ("SC", "South Carolina"),
    ("SD", "South Dakota"),
    ("TN", "Tennessee"),
    ("TX", "Texas"),
    ("UT", "Utah"),
    ("VT", "Vermont"),
    ("VA", "Virginia"),
    ("WA", "Washington"),
    ("WV", "West Virginia"),
    ("WI", "Wisconsin"),
    ("WY", "Wyoming"),
)

from datetime import datetime

year_choices = [(r, r) for r in range(2000, (datetime.now().year + 1))]

features_choices = (
    ("Cruise Control", "Cruise Control"),
    ("Audio Interface", "Audio Interface"),
    ("Airbags", "Airbags"),
    ("Air Conditioning", "Air Conditioning"),
    ("Seat Heating", "Seat Heating"),
    ("Alarm System", "Alarm System"),
    ("ParkAssist", "ParkAssist"),
    ("Power Steering", "Power Steering"),
    ("Reversing Camera", "Reversing Camera"),
    ("Direct Fuel Injection", "Direct Fuel Injection"),
    ("Auto Start/Stop", "Auto Start/Stop"),
    ("Wind Deflector", "Wind Deflector"),
    ("Bluetooth Handset", "Bluetooth Handset"),
)


def integer_choices(min=0, max=10):
    return ((i, str(i)) for i in range(min, max + 1))
