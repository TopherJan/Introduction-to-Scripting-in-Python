"""
Project for Week 3 of "Python Data Visualization".
Unify data via common country name.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import csv
import math
import pygal

def reconcile_countries_by_name(plot_countries, gdp_countries):
    """
    Inputs:
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      gdp_countries  - Dictionary whose keys are country names used in GDP data

    Output:
      A tuple containing a dictionary and a set.  The dictionary maps
      country codes from plot_countries to country names from
      gdp_countries The set contains the country codes from
      plot_countries that were not found in gdp_countries.
    """
    plot_dict = {}
    plot_set = set()

    for code, name in plot_countries.items():
        if name in gdp_countries.keys():
            plot_dict[code] = name
        else:
            plot_set.add(code)

    return (plot_dict, plot_set)


def build_map_dict_by_name(gdpinfo, plot_countries, year):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      year           - String year to create GDP mapping for

    Output:
      A tuple containing a dictionary and two sets.  The dictionary
      maps country codes from plot_countries to the log (base 10) of
      the GDP value for that country in the specified year.  The first
      set contains the country codes from plot_countries that were not
      found in the GDP data file.  The second set contains the country
      codes from plot_countries that were found in the GDP data file, but
      have no GDP data for the specified year.
    """

    logplot_dict = {}
    not_found_set = set()
    no_gdp_set = set()

    gdp_countries = {}
    with open(gdpinfo['gdpfile'], "r", newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile,
                                    delimiter=gdpinfo['separator'],
                                    quotechar=gdpinfo['quote'],
                                    quoting=csv.QUOTE_MINIMAL)
        for row in csv_reader:
            gdp_countries[row[gdpinfo['country_name']]] = row

    plot_dict, not_found_set = reconcile_countries_by_name(plot_countries, gdp_countries)

    for code, name in plot_dict.items():
        if name in gdp_countries.keys():
            if gdp_countries[name][year] != '':
                logplot_dict[code] = math.log(float(gdp_countries[name][year]), 10)
            else:
                no_gdp_set.add(code)

    return (logplot_dict, not_found_set, no_gdp_set)


def render_world_map(gdpinfo, plot_countries, year, map_file):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      year           - String year to create GDP mapping for
      map_file       - Name of output file to create

    Output:
      Returns None.

    Action:
      Creates a world map plot of the GDP data for the given year and
      writes it to a file named by map_file.
    """
    logplot_dict, not_found_set, no_gdp_set = build_map_dict_by_name(gdpinfo, plot_countries, year)

    world_map = pygal.maps.world.World()
    title_map = 'GDP by country for ' + year + '(log scale), unified by common country NAME'
    world_map.title = title_map
    world_map.add('GDP for ' + year, logplot_dict)
    world_map.add('Missing Data', not_found_set)
    world_map.add('No GDP Data', no_gdp_set)
    world_map.render_in_browser()


def test_render_world_map():
    """
    Test the project code for several years.
    """
    gdpinfo = {
        "gdpfile": "isp_gdp.csv",
        "separator": ",",
        "quote": '"',
        "min_year": 1960,
        "max_year": 2015,
        "country_name": "Country Name",
        "country_code": "Country Code"
    }

    # Get pygal country code map
    pygal_countries = pygal.maps.world.COUNTRIES

    # 1960
    render_world_map(gdpinfo, pygal_countries, "1960", "isp_gdp_world_name_1960.svg")

    # 1980
    render_world_map(gdpinfo, pygal_countries, "1980", "isp_gdp_world_name_1980.svg")

    # 2000
    render_world_map(gdpinfo, pygal_countries, "2000", "isp_gdp_world_name_2000.svg")

    # 2010
    render_world_map(gdpinfo, pygal_countries, "2010", "isp_gdp_world_name_2010.svg")


# Make sure the following call to test_render_world_map is commented
# out when submitting to OwlTest/CourseraTest.

# test_render_world_map()
