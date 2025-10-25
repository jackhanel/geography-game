import requests
import csv
import io
import random
from itertools import permutations


def lifeExpectancy():
    url = "https://ourworldindata.org/grapher/life-expectancy.csv"
    response = requests.get(url)
    if response.status_code == 200:
        csv_file = io.StringIO(response.text)
        reader = csv.DictReader(csv_file)

        most_recent_data = {}
        for row in reader:
            if not row["Code"] or row["Code"] == "OWID_WRL":
                continue
            
            country = row["Entity"]
            year = row["Year"]
            data = row["Period life expectancy at birth"]
            if country not in most_recent_data or year > most_recent_data[country]["year"]:
                most_recent_data[country] = {
                    "country": country,
                    "code" : row["Code"],
                    "year" : year,
                    "data" : data
                }

        most_recent_data = list(most_recent_data.values())
        if most_recent_data is None:
            print(f'most recent data is "None" for {url}')
        print(f'life expectancy most recent data: {most_recent_data}')
        return most_recent_data


def population():
    url = "https://ourworldindata.org/grapher/population.csv"
    response = requests.get(url)
    if response.status_code == 200:
        csv_file = io.StringIO(response.text)
        reader = csv.DictReader(csv_file)

        most_recent_data = {}
        for row in reader:
            if not row["Code"] or row["Code"] == "OWID_WRL":
                continue
            
            country = row["Entity"]
            year = row["Year"]
            data = row["Population (historical)"]
            if country not in most_recent_data or year > most_recent_data[country]["year"]:
                most_recent_data[country] = {
                    "country": country,
                    "code" : row["Code"],
                    "year" : year,
                    "data" : data
                }
        most_recent_data = list(most_recent_data.values())
        if most_recent_data is None:
            print(f'most recent data is "None" for {url}')
        return most_recent_data


def co2Emissions():
    url = "https://ourworldindata.org/grapher/annual-co2-emissions-per-country.csv"
    response = requests.get(url)
    response.encoding = "utf-8"     
    if response.status_code == 200:
        csv_file = io.StringIO(response.text)
        reader = csv.DictReader(csv_file)

        most_recent_data = {}
        for row in reader:
            if not row["Code"] or row["Code"] == "OWID_WRL":
                continue
            
            country = row["Entity"]
            year = row["Year"]
            data = row["Annual CO₂ emissions"]
            if (
                country not in most_recent_data
                or year > most_recent_data[country]["year"]
            ):
                most_recent_data[country] = {
                    "country": country,
                    "code": row["Code"],
                    "year": year,
                    "data": data,
                }
        most_recent_data = list(most_recent_data.values())
        if most_recent_data is None:
            print(f'most recent data is "None" for {url}')
        return most_recent_data

def oilProduction():
    url = "https://ourworldindata.org/grapher/oil-production-by-country.csv"
    response = requests.get(url)
    response.encoding = "utf-8"     
    if response.status_code == 200:
        csv_file = io.StringIO(response.text)
        reader = csv.DictReader(csv_file)

        most_recent_data = {}
        for row in reader:
            if not row["Code"] or row["Code"] == "OWID_WRL":
                continue
            
            country = row["Entity"]
            year = row["Year"]
            data = row["Oil production (TWh)"]
            if (
                country not in most_recent_data
                or year > most_recent_data[country]["year"]
            ):
                most_recent_data[country] = {
                    "country": country,
                    "code": row["Code"],
                    "year": year,
                    "data": data,
                }
        most_recent_data = list(most_recent_data.values())
        if most_recent_data is None:
            print(f'most recent data is "None" for {url}')
        return most_recent_data


def wildfireBurnArea():
    url = "https://ourworldindata.org/grapher/annual-area-burnt-by-wildfires.csv"
    response = requests.get(url)
    response.encoding = "utf-8"     
    if response.status_code == 200:
        csv_file = io.StringIO(response.text)
        reader = csv.DictReader(csv_file)

        most_recent_data = {}
        for row in reader:
            if not row["Code"] or row["Code"] == "OWID_WRL":
                continue
            
            country = row["Entity"]
            year = row["Year"]
            data = row["Annual area burnt by wildfires"]
            if (
                country not in most_recent_data
                or year > most_recent_data[country]["year"]
            ):
                most_recent_data[country] = {
                    "country": country,
                    "code": row["Code"],
                    "year": year,
                    "data": data,
                }
        most_recent_data = list(most_recent_data.values())
        if most_recent_data is None:
            print(f'most recent data is "None" for {url}')
        return most_recent_data

def energyUsePerCapita():
    url = "https://ourworldindata.org/grapher/per-capita-energy-use.csv"
    response = requests.get(url)
    if response.status_code == 200:
        csv_file = io.StringIO(response.text)
        reader = csv.DictReader(csv_file)

        most_recent_data = {}
        for row in reader:            
            if not row["Code"] or row["Code"] == "OWID_WRL":
                continue
            
            country = row["Entity"]
            year = row["Year"]
            data = row["Primary energy consumption per capita (kWh/person)"]
            if (
                country not in most_recent_data
                or year > most_recent_data[country]["year"]
            ):
                most_recent_data[country] = {
                    "country": country,
                    "code": row["Code"],
                    "year": year,
                    "data": data,
                }
        most_recent_data = list(most_recent_data.values())
        if most_recent_data is None:
            print(f'most recent data is "None" for {url}')
        return most_recent_data


def calorieSupplyPerCapita():
    url = "https://ourworldindata.org/grapher/daily-per-capita-caloric-supply.csv"
    response = requests.get(url)
    if response.status_code == 200:
        csv_file = io.StringIO(response.text)
        reader = csv.DictReader(csv_file)

        most_recent_data = {}
        for row in reader:            
            if not row["Code"] or row["Code"] == "OWID_WRL":
                continue
            
            country = row["Entity"]
            year = row["Year"]
            data = row["Daily calorie supply per person"]
            if (
                country not in most_recent_data
                or year > most_recent_data[country]["year"]
            ):
                most_recent_data[country] = {
                    "country": country,
                    "code": row["Code"],
                    "year": year,
                    "data": data,
                }
        most_recent_data = list(most_recent_data.values())
        if most_recent_data is None:
            print(f'most recent data is "None" for {url}')
        return most_recent_data


def humanDevelopmentIndex():
    url = "https://ourworldindata.org/grapher/human-development-index.csv"
    response = requests.get(url)
    if response.status_code == 200:
        csv_file = io.StringIO(response.text)
        reader = csv.DictReader(csv_file)

        most_recent_data = {}
        for row in reader:
            if not row["Code"] or row["Code"] == "OWID_WRL":
                continue
            
            country = row["Entity"]
            year = row["Year"]
            data = row["Human Development Index"]
            if (
                country not in most_recent_data
                or year > most_recent_data[country]["year"]
            ):
                most_recent_data[country] = {
                    "country": country,
                    "code": row["Code"],
                    "year": year,
                    "data": data,
                }
        most_recent_data = list(most_recent_data.values())
        if most_recent_data is None:
            print(f'most recent data is "None" for {url}')
        return most_recent_data


def literacyRate():
    url = "https://ourworldindata.org/grapher/cross-country-literacy-rates.csv"
    response = requests.get(url)
    if response.status_code == 200:
        csv_file = io.StringIO(response.text)
        reader = csv.DictReader(csv_file)

        most_recent_data = {}
        for row in reader:            
            if not row["Code"] or row["Code"] == "OWID_WRL":
                continue
            
            country = row["Entity"]
            year = row["Year"]
            data = row["Literacy rate"]
            if (
                country not in most_recent_data
                or year > most_recent_data[country]["year"]
            ):
                most_recent_data[country] = {
                    "country": country,
                    "code": row["Code"],
                    "year": year,
                    "data": data,
                }
        most_recent_data = list(most_recent_data.values())
        if most_recent_data is None:
            print(f'most recent data is "None" for {url}')
        return most_recent_data


def shareOfIndividualsUsingTheInternet():
    url = "https://ourworldindata.org/grapher/share-of-individuals-using-the-internet.csv"
    response = requests.get(url)
    if response.status_code == 200:
        csv_file = io.StringIO(response.text)
        reader = csv.DictReader(csv_file)

        most_recent_data = {}
        for row in reader:            
            if not row["Code"] or row["Code"] == "OWID_WRL":
                continue
            
            country = row["Entity"]
            year = row["Year"]
            data = row["Individuals using the Internet (% of population)"]
            if (
                country not in most_recent_data
                or year > most_recent_data[country]["year"]
            ):
                most_recent_data[country] = {
                    "country": country,
                    "code": row["Code"],
                    "year": year,
                    "data": data,
                }
        most_recent_data = list(most_recent_data.values())
        if most_recent_data is None:
            print(f'most recent data is "None" for {url}')
        return most_recent_data


def yearlyNumberOfObjectsLaunchedIntoOuterSpace():
    url = "https://ourworldindata.org/grapher/yearly-number-of-objects-launched-into-outer-space.csv"
    response = requests.get(url)
    if response.status_code == 200:
        csv_file = io.StringIO(response.text)
        reader = csv.DictReader(csv_file)

        most_recent_data = {}
        for row in reader:            
            if not row["Code"] or row["Code"] == "OWID_WRL":
                continue
            
            country = row["Entity"]
            year = row["Year"]
            data = row["Annual number of objects launched into outer space"]
            if (
                country not in most_recent_data
                or year > most_recent_data[country]["year"]
            ):
                most_recent_data[country] = {
                    "country": country,
                    "code": row["Code"],
                    "year": year,
                    "data": data,
                }
        most_recent_data = list(most_recent_data.values())
        if most_recent_data is None:
            print(f'most recent data is "None" for {url}')
        return most_recent_data


def militarySpendingAsAGShareOfGDP():
    url = "https://ourworldindata.org/grapher/military-spending-as-a-share-of-gdp-sipri.csv"
    response = requests.get(url)
    if response.status_code == 200:
        csv_file = io.StringIO(response.text)
        reader = csv.DictReader(csv_file)

        most_recent_data = {}
        for row in reader:            
            if not row["Code"] or row["Code"] == "OWID_WRL":
                continue
            
            country = row["Entity"]
            year = row["Year"]
            data = row["Military expenditure (% of GDP)"]
            if (
                country not in most_recent_data
                or year > most_recent_data[country]["year"]
            ):
                most_recent_data[country] = {
                    "country": country,
                    "code": row["Code"],
                    "year": year,
                    "data": data,
                }
        most_recent_data = list(most_recent_data.values())
        if most_recent_data is None:
            print(f'most recent data is "None" for {url}')
        return most_recent_data


def homicideRate():
    url = "https://ourworldindata.org/grapher/homicide-rate-unodc.csv"
    response = requests.get(url)
    if response.status_code == 200:
        csv_file = io.StringIO(response.text)
        reader = csv.DictReader(csv_file)

        most_recent_data = {}
        for row in reader:            
            if not row["Code"] or row["Code"] == "OWID_WRL":
                continue
            
            country = row["Entity"]
            year = row["Year"]
            data = row["Homicide rate per 100,000 population - sex: Total - age: Total"]
            if (
                country not in most_recent_data
                or year > most_recent_data[country]["year"]
            ):
                most_recent_data[country] = {
                    "country": country,
                    "code": row["Code"],
                    "year": year,
                    "data": data,
                }
        most_recent_data = list(most_recent_data.values())
        if most_recent_data is None:
            print(f'most recent data is "None" for {url}')
        return most_recent_data


def shareOfGDPFromTourism():
    url = "https://ourworldindata.org/grapher/tourism-gdp-proportion-of-total-gdp.csv"
    response = requests.get(url)
    if response.status_code == 200:
        csv_file = io.StringIO(response.text)
        reader = csv.DictReader(csv_file)

        most_recent_data = {}
        for row in reader:
            if not row["Code"] or row["Code"] == "OWID_WRL":
                continue
            
            country = row["Entity"]
            year = row["Year"]
            data = row["GDP from tourism as a share of total GDP"]
            if (
                country not in most_recent_data
                or year > most_recent_data[country]["year"]
            ):
                most_recent_data[country] = {
                    "country": country,
                    "code": row["Code"],
                    "year": year,
                    "data": data,
                }
        most_recent_data = list(most_recent_data.values())
        if most_recent_data is None:
            print(f'most recent data is "None" for {url}')
        return most_recent_data


def GDPPerCapita():
    url = "https://ourworldindata.org/grapher/gdp-per-capita-worldbank.csv"
    response = requests.get(url)
    if response.status_code == 200:
        csv_file = io.StringIO(response.text)
        reader = csv.DictReader(csv_file)

        most_recent_data = {}
        for row in reader:
            if not row["Code"] or row["Code"] == "OWID_WRL":
                continue
            
            country = row["Entity"]
            year = row["Year"]
            data = row["GDP per capita, PPP (constant 2021 international $)"]
            if (
                country not in most_recent_data
                or year > most_recent_data[country]["year"]
            ):
                most_recent_data[country] = {
                    "country": country,
                    "code": row["Code"],
                    "year": year,
                    "data": data,
                }
        most_recent_data = list(most_recent_data.values())
        if most_recent_data is None:
            print(f'most recent data is "None" for {url}')
        return most_recent_data


def uniqueSpecies():
    urls = {
        "mammals": "https://ourworldindata.org/grapher/endemic-mammal-species-by-country.csv",
        "birds": "https://ourworldindata.org/grapher/endemic-bird-species-by-country.csv",
        "amphibians": "https://ourworldindata.org/grapher/endemic-amphibian-species-by-country.csv",
    }

    # master dictionary
    most_recent_combined_data = {}

    for category, url in urls.items():
        response = requests.get(url)
        if response.status_code == 200:
            csv_file = io.StringIO(response.text)
            reader = csv.DictReader(csv_file)

            for row in reader:
                if not row["Code"] or row["Code"] == "OWID_WRL":
                    continue
                
                country = row["Entity"]
                year = row["Year"]
                # column name changes with category
                data_key = next(k for k in row.keys() if "species" in k.lower())
                value = row[data_key]

                # skip empty data
                if value == "":
                    continue

                # if the country isn’t in yet, create it
                if country not in most_recent_combined_data:
                    most_recent_combined_data[country] = {
                        "country": country,
                        "code": row["Code"],
                        "year": year,
                        "data": 0,
                    }

                # update to most recent year
                if year >= most_recent_combined_data[country]["year"]:
                    most_recent_combined_data[country]["year"] = year

                # add numeric total (convert safely)
                try:
                    most_recent_combined_data[country]["data"] += int(float(value))
                except ValueError:
                    pass  # skip invalid entries

    most_recent_combined_data = list(most_recent_combined_data.values())
    if most_recent_combined_data is None:
        print(f'most recent data is "None" for {url}')
    return most_recent_combined_data


def shareOfLandCoveredByLakesAndRivers():
    url = "https://ourworldindata.org/grapher/share-of-land-covered-by-lakes-and-rivers.csv"
    response = requests.get(url)
    if response.status_code == 200:
        csv_file = io.StringIO(response.text)
        reader = csv.DictReader(csv_file)

        most_recent_data = {}
        for row in reader:            
            if not row["Code"] or row["Code"] == "OWID_WRL":
                continue
            
            country = row["Entity"]
            year = row["Year"]
            data = row["6.6.1 - Lakes and rivers permanent water area (% of total land area) - EN_LKRV_PWAP"]
            if (
                country not in most_recent_data
                or year > most_recent_data[country]["year"]
            ):
                most_recent_data[country] = {
                    "country": country,
                    "code": row["Code"],
                    "year": year,
                    "data": data,
                }
        most_recent_data = list(most_recent_data.values())
        if most_recent_data is None:
            print(f'most recent data is "None" for {url}')
        return most_recent_data


def rankCountries(most_recent_data):
    valid_data = []
    for entry in most_recent_data:
        try:
            data_value = float(entry["data"])
            valid_data.append({**entry, "data": data_value})
        except (ValueError, TypeError):
            continue

    # Sort in descending order (highest value first)
    sorted_data = sorted(valid_data, key=lambda x: x["data"], reverse=True)

    # Add rank numbers
    ranked_data = []
    for i, entry in enumerate(sorted_data, start=1):
        ranked_entry = {**entry, "rank": i}
        ranked_data.append(ranked_entry)

    return ranked_data


data_options = [
    {"backend_name": "life_expectancy_data", "front_end_name": "👨‍🦳🧑‍🦳 Life Expectancy"},
    {"backend_name": "population_data", "front_end_name": "👨‍👩‍👧‍👦 Population"},
    {"backend_name": "co2_emissions_data", "front_end_name": "🏭 CO2 Emissions"},
    {"backend_name": "oil_production_data", "front_end_name": "🛢️ Oil Production"},
    {"backend_name": "wildfire_burn_area_data", "front_end_name": "🔥 Wildfires"},
    {"backend_name": "energy_use_per_capita_data", "front_end_name": "🔋 Energy Use (per capita)"},
    {"backend_name": "calorie_supply_per_capita_data", "front_end_name": "🍔 Calorie Supply (per capita)"},
    {"backend_name": "human_development_index_data", "front_end_name": "🏙️ HDI"},
    {"backend_name": "literacy_rate_data", "front_end_name": "📖 Literacy Rate"},
    {"backend_name": "share_of_individuals_using_the_internet_data", "front_end_name": "🛜 Internet Connectivity (% of population)"},
    {"backend_name": "yearly_number_of_objects_launched_into_outer_space_data", "front_end_name": "🛰️🪐 Space Objects"},
    {"backend_name": "military_spending_as_a_share_of_gdp_data", "front_end_name": "🪖 Military Spending (% of GDP)"},
    {"backend_name": "homicide_rate_data", "front_end_name": "☠️ Homicide Rate"},
    {"backend_name": "share_of_gdp_from_tourism_data", "front_end_name": "🗽 Tourism (% of GDP)"},
    {"backend_name": "gdp_per_capita_data", "front_end_name": "🏦 GDP (per capita)"},
    {"backend_name": "unique_species_data", "front_end_name": "🦋🪼 Unique Species"},
    {"backend_name": "share_of_land_covered_by_lakes_and_rivers_data", "front_end_name": "🏖️ Lakes and Rivers (% of Land)"},
]


def generateGameCategories():
    game_category_backend_names = []
    game_category_front_end_names = []
    while len(game_category_backend_names) < 9:
        random_option = random.choice(data_options)
        backend_name = random_option["backend_name"]
        front_end_name = random_option["front_end_name"]
        if backend_name not in game_category_backend_names:
            game_category_backend_names.append(backend_name)
            game_category_front_end_names.append(front_end_name)
    return game_category_backend_names, game_category_front_end_names


def getCountryData(game_category_backend_names):
    all_game_data = []
    for game_category_backend_name in game_category_backend_names:
        if game_category_backend_name == "life_expectancy_data":
            most_recent_data = lifeExpectancy()
        elif game_category_backend_name == "population_data":
            most_recent_data = population()
        elif game_category_backend_name == "co2_emissions_data":
            most_recent_data = co2Emissions()
        elif game_category_backend_name == "oil_production_data":
            most_recent_data = oilProduction()
        elif game_category_backend_name == "wildfire_burn_area_data":
            most_recent_data = wildfireBurnArea()
        elif game_category_backend_name == "energy_use_per_capita_data":
            most_recent_data = energyUsePerCapita()
        elif game_category_backend_name == "calorie_supply_per_capita_data":
            most_recent_data = calorieSupplyPerCapita()
        elif game_category_backend_name == "human_development_index_data":
            most_recent_data = humanDevelopmentIndex()
        elif game_category_backend_name == "literacy_rate_data":
            most_recent_data = literacyRate()
        elif game_category_backend_name == "share_of_individuals_using_the_internet_data":
            most_recent_data = shareOfIndividualsUsingTheInternet()
        elif game_category_backend_name == "yearly_number_of_objects_launched_into_outer_space_data":
            most_recent_data = yearlyNumberOfObjectsLaunchedIntoOuterSpace()
        elif game_category_backend_name == "military_spending_as_a_share_of_gdp_data":
            most_recent_data = militarySpendingAsAGShareOfGDP()
        elif game_category_backend_name == "homicide_rate_data":
            most_recent_data = homicideRate()
        elif game_category_backend_name == "share_of_gdp_from_tourism_data":
            most_recent_data = shareOfGDPFromTourism()
        elif game_category_backend_name == "gdp_per_capita_data":
            most_recent_data = GDPPerCapita()
        elif game_category_backend_name == "unique_species_data":
            most_recent_data = uniqueSpecies()
        elif game_category_backend_name == "share_of_land_covered_by_lakes_and_rivers_data":
            most_recent_data = shareOfLandCoveredByLakesAndRivers()
        most_recent_data_ranked = rankCountries(most_recent_data)

        # map the backend name to the front end name from our data_options list
        for data_option in data_options:
            if data_option["backend_name"] == game_category_backend_name:
                game_category_front_end_name = data_option["front_end_name"]

        dictionary = {"game_category_backend_name": game_category_backend_name, "game_category_front_end_name": game_category_front_end_name, "country_ranks": most_recent_data_ranked}
        all_game_data.append(dictionary)
    return all_game_data

countries = [
    {"country_name": "Afghanistan", "flag": "🇦🇫"},
    {"country_name": "Algeria", "flag": "🇩🇿"},
    {"country_name": "Argentina", "flag": "🇦🇷"},
    {"country_name": "Australia", "flag": "🇦🇺"},
    {"country_name": "Austria", "flag": "🇦🇹"},
    {"country_name": "Belgium", "flag": "🇧🇪"},
    {"country_name": "Brazil", "flag": "🇧🇷"},
    {"country_name": "Canada", "flag": "🇨🇦"},
    {"country_name": "Chile", "flag": "🇨🇱"},
    {"country_name": "China", "flag": "🇨🇳"},
    {"country_name": "Colombia", "flag": "🇨🇴"},
    {"country_name": "Congo", "flag": "🇨🇬"},
    {"country_name": "Costa Rica", "flag": "🇨🇷"},
    {"country_name": "Croatia", "flag": "🇭🇷"},
    {"country_name": "Cuba", "flag": "🇨🇺"},
    {"country_name": "Czechia", "flag": "🇨🇿"},
    {"country_name": "Denmark", "flag": "🇩🇰"},
    {"country_name": "Dominican Republic", "flag": "🇩🇴"},
    {"country_name": "Ecuador", "flag": "🇪🇨"},
    {"country_name": "Egypt", "flag": "🇪🇬"},
    {"country_name": "El Salvador", "flag": "🇸🇻"},
    {"country_name": "Finland", "flag": "🇫🇮"},
    {"country_name": "France", "flag": "🇫🇷"},
    {"country_name": "Germany", "flag": "🇩🇪"},
    {"country_name": "Ghana", "flag": "🇬🇭"},
    {"country_name": "Greece", "flag": "🇬🇷"},
    {"country_name": "Guatemala", "flag": "🇬🇹"},
    {"country_name": "Honduras", "flag": "🇭🇳"},
    {"country_name": "Hong Kong", "flag": "🇭🇰"},
    {"country_name": "Hungary", "flag": "🇭🇺"},
    {"country_name": "Iceland", "flag": "🇮🇸"},
    {"country_name": "India", "flag": "🇮🇳"},
    {"country_name": "Indonesia", "flag": "🇮🇩"},
    {"country_name": "Iran", "flag": "🇮🇷"},
    {"country_name": "Iraq", "flag": "🇮🇶"},
    {"country_name": "Ireland", "flag": "🇮🇪"},
    {"country_name": "Israel", "flag": "🇮🇱"},
    {"country_name": "Italy", "flag": "🇮🇹"},
    {"country_name": "Jamaica", "flag": "🇯🇲"},
    {"country_name": "Japan", "flag": "🇯🇵"},
    {"country_name": "Jordan", "flag": "🇯🇴"},
    {"country_name": "Kazakhstan", "flag": "🇰🇿"},
    {"country_name": "Kenya", "flag": "🇰🇪"},
    {"country_name": "Kyrgyzstan", "flag": "🇰🇬"},
    {"country_name": "Malaysia", "flag": "🇲🇾"},
    {"country_name": "Mexico", "flag": "🇲🇽"},
    {"country_name": "Montenegro", "flag": "🇲🇪"},
    {"country_name": "Morocco", "flag": "🇲🇦"},
    {"country_name": "New Zealand", "flag": "🇳🇿"},
    {"country_name": "Nigeria", "flag": "🇳🇬"},
    {"country_name": "North Korea", "flag": "🇰🇵"},
    {"country_name": "Norway", "flag": "🇳🇴"},
    {"country_name": "Pakistan", "flag": "🇵🇰"},
    {"country_name": "Panama", "flag": "🇵🇦"},
    {"country_name": "Peru", "flag": "🇵🇪"},
    {"country_name": "Philippines", "flag": "🇵🇭"},
    {"country_name": "Poland", "flag": "🇵🇱"},
    {"country_name": "Portugal", "flag": "🇵🇹"},
    {"country_name": "Puerto Rico", "flag": "🇵🇷"},
    {"country_name": "Qatar", "flag": "🇶🇦"},
    {"country_name": "Romania", "flag": "🇷🇴"},
    {"country_name": "Russia", "flag": "🇷🇺"},
    {"country_name": "Saudi Arabia", "flag": "🇸🇦"},
    {"country_name": "Senegal", "flag": "🇸🇳"},
    {"country_name": "Serbia", "flag": "🇷🇸"},
    {"country_name": "Singapore", "flag": "🇸🇬"},
    {"country_name": "Slovenia", "flag": "🇸🇮"},
    {"country_name": "South Africa", "flag": "🇿🇦"},
    {"country_name": "South Korea", "flag": "🇰🇷"},
    {"country_name": "Spain", "flag": "🇪🇸"},
    {"country_name": "Switzerland", "flag": "🇨🇭"},
    {"country_name": "Thailand", "flag": "🇹🇭"},
    {"country_name": "Turkey", "flag": "🇹🇷"},
    {"country_name": "Ukraine", "flag": "🇺🇦"},
    {"country_name": "United Kingdom", "flag": "🇬🇧"},
    {"country_name": "United States", "flag": "🇺🇸"},
    {"country_name": "Uruguay", "flag": "🇺🇾"},
    {"country_name": "Venezuela", "flag": "🇻🇪"},
    {"country_name": "Vietnam", "flag": "🇻🇳"}
]


def getCountries():
    random_countries = []
    for i in range(9):
        while True:
            random_number = random.randint(0, len(countries) - 1)
            if countries[random_number] not in random_countries:
                random_countries.append(countries[random_number])
                break
    return random_countries


def optimalSolution(all_game_data_for_front_end):
    # Step 1: Extract category information
    all_category_backend_names = [
        category_block["game_category_backend_name"] for category_block in all_game_data_for_front_end
    ]

    category_name_to_frontend_label = {
        category_block["game_category_backend_name"]: category_block[
            "game_category_front_end_name"
        ]
        for category_block in all_game_data_for_front_end
    }

    # Step 2: Extract all unique country names that appear in the dataset
    all_country_names = sorted(
        {
            entry["country_name"]
            for category_block in all_game_data_for_front_end
            for entry in category_block["country_ranks"]
        }
    )

    # Step 3: Build a lookup dictionary of ranks
    # rank_lookup[country_name][category_backend_name] = rank_value
    rank_lookup = {country_name: {} for country_name in all_country_names}

    for category_block in all_game_data_for_front_end:
        category_backend_name = category_block["game_category_backend_name"]

        for country_entry in category_block["country_ranks"]:
            country_name = country_entry["country_name"]
            country_rank_value = int(country_entry["rank"])
            rank_lookup[country_name][category_backend_name] = country_rank_value

    # Step 4: Initialize variables to track the best (lowest) total score
    lowest_total_score = None
    best_country_category_pairs = None

    # Step 5: Loop over every possible permutation of categories
    # Each permutation represents a unique 1-to-1 assignment of categories to countries.
    for category_permutation in permutations(all_category_backend_names):
        current_total_score = 0
        is_valid_permutation = True

        # Step 6: For each country, assign the corresponding category in this permutation
        for country_name, category_backend_name in zip(
            all_country_names, category_permutation
        ):
            # Look up the country's rank for this category
            current_rank = rank_lookup[country_name].get(category_backend_name)

            # If data is missing, mark this permutation as invalid and skip it
            if current_rank is None:
                is_valid_permutation = False
                break

            # Add the rank to the running total
            current_total_score += current_rank

            # Early exit: stop evaluating if this permutation is already worse than the best one
            if (
                lowest_total_score is not None
                and current_total_score >= lowest_total_score
            ):
                is_valid_permutation = False
                break

        # Step 7: If this permutation is valid and has a lower total score, update the best record
        if is_valid_permutation:
            if lowest_total_score is None or current_total_score < lowest_total_score:
                lowest_total_score = current_total_score
                best_country_category_pairs = list(
                    zip(all_country_names, category_permutation)
                )

    # Step 8: Prepare the output
    formatted_results = []
    for country_name, category_backend_name in best_country_category_pairs:
        formatted_results.append(
            {
                "country": country_name,
                "category_backend": category_backend_name,
                "category_frontend": category_name_to_frontend_label[
                    category_backend_name
                ],
                "rank": rank_lookup[country_name][category_backend_name],
            }
        )

    # Step 9: Return a nicely structured result
    return {
        "total_score": lowest_total_score,
        "pairs": sorted(formatted_results, key=lambda x: x["rank"]),
    }
