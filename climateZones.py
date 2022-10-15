import pandas as pd

zone_hardiness = pd.read_csv(r"C:\Users\jennifer\Downloads\phm_us_zipcode.csv")
# plant_by_zone = pd.read_csv(r"C:\Users\jennifer\Downloads\plant_by_zone.csv")


def get_zip() -> int:
    num_rows = len(zone_hardiness.index)

    zipcode = -1
    is_valid_zip = False

    while not is_valid_zip:
        temp = int(input("What is your zipcode?: "))

        if temp < 0 or temp > zone_hardiness["zipcode"][num_rows - 1]:
            print("Zipcode must be in range 0 and " + str(zone_hardiness["zipcode"][num_rows - 1]))
        else:
            zipcode = temp
            is_valid_zip = True
    return zipcode


def zone_from_zip(zipcode):
    my_index = zone_hardiness.index[zone_hardiness["zipcode"] == zipcode]
    return zone_hardiness["zone"][my_index]


def get_plants(zipcode):
    print(zipcode)


my_zipcode = get_zip()
my_zone = zone_from_zip(my_zipcode)
print(str(my_zone)[1])
