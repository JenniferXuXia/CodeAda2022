import pandas as pd

zone_hardiness = pd.read_csv(r"C:\Users\jennifer\Downloads\phm_us_zipcode.csv")
plant_by_zone = pd.read_csv(r"C:\Users\jennifer\Downloads\plant_by_zone.csv")
plant_by_zone = plant_by_zone.replace(to_replace="\xa0", value=None)


def get_zip() -> int:
    num_rows = len(zone_hardiness.index)

    zipcode = -1
    is_valid_zip = False

    while not is_valid_zip:
        temp = int(input("What is your zipcode?: "))

        if temp < 0 or temp > zone_hardiness['zipcode'][num_rows - 1]:
            print("Zipcode must be in range 0 and " + str(zone_hardiness['zipcode'][num_rows - 1]))
        else:
            zipcode = temp
            is_valid_zip = True
    return zipcode


def zone_from_zip(zipcode):
    # index = zone_hardiness.index[zone_hardiness['zipcode'] == zipcode]
    # zone = str(zone_hardiness['zone'][index])
    # zone = zone.split("    ")
    # zone = zone[1][0]
    zone = zone_hardiness.loc[zone_hardiness['zipcode'] == zipcode, 'zone'].values[0]
    simple_zone = zone[0]
    return simple_zone


def get_plants(zone):
    zone_plants = []
    zone_dates = plant_by_zone[zone]
    for date in zone_dates[zone_dates.notnull()]:
        plant = plant_by_zone.loc[plant_by_zone[zone] == date, 'Plant'].values[0]
        # plant = plant_by_zone['Plant'].where(plant_by_zone[zone] == date).dropna().values[0]
        zone_plants.append(plant)
    return zone_plants


my_zipcode = get_zip()
my_zone = zone_from_zip(my_zipcode)
print(my_zone)
print(get_plants(my_zone))
