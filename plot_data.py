# Author: Sandy Nguyen
 
import matplotlib.pyplot as plt
from build_countries import *
 
def get_bar_co2_pc_by_continent(countries_dict, country_year):
    
    """ (dict, int) -> list
    This function creates a bar plot representing the co2 emissions per capita (in tonnes)
    produced by all the countries in each continent and returns a list of values being plotted.
    
    >>> d = get_countries_from_file("large_co2_data.tsv")
    >>> data = get_bar_co2_pc_by_continent(d, 2000)
    
    >>> data[:2]
    [1.0975340644568221, 2.6980486411788904]
    
    >>> len(data)
    6
    
    >>> round(data[2], 1)
    8.0
 
    """
    
    # Assigning local variables
    continents_list = ['AFRICA', 'ASIA', 'EUROPE', 'NORTH AMERICA', 'OCEANIA', 'SOUTH AMERICA']
    continents_co2_list = [0, 0, 0, 0, 0, 0]
    countries_list = []
    continents_list_copy = []
    continents_co2_list_copy = []
    
    # Adding the Country objects into a list
    for country in countries_dict:
        countries_list.append(countries_dict[country])
    
    # Getting the dictionary continent-countries key-value
    continents_dict = Country.get_countries_by_continent(countries_list)
    
    # Looping through each continent of continents_dict
    for continent in continents_dict:
        
        # Getting the continent's total co2 emissions per capita by year
        continent_co2 = Country.get_total_co2_emissions_per_capita_by_year(continents_dict[continent], country_year)
        
        # Adding continent_co2 to continents_co2_list at the right continent's index
        if continent_co2 != None:
            continents_co2_list[continents_list.index(continent)] += continent_co2
    
    # Looping through each continent's co2 emissions in continents_co2_list
    for continent_co2_value in continents_co2_list:
        
        # Doing a copy of continents_list and continents_co2_list while removing the continents that didn't have co2 emissions
        if continent_co2_value != 0:
            continents_list_copy.append(continents_list[continents_co2_list.index(continent_co2_value)])
            continents_co2_list_copy.append(continent_co2_value)
        
    # Creating the bar graph
    plt.bar(continents_list_copy, continents_co2_list_copy)
    plt.title('CO2 emissions per capital in ' + str(country_year) + ' by sandy.nguyen2@mail.mcgill.ca')
    plt.ylabel('co2 (in tonnes)')
    plt.savefig('co2_pc_by_continent_' + str(country_year))
    plt.show()
    
    return continents_co2_list_copy
    
def get_bar_historical_co2_by_continent(countries_dict, country_year):
    
    """ (dict, int) -> list
    This function creates a bar plot representing the historical co2 emissions (in millions of tonnes)
    produced by all the countries in each continent and returns a list of values being plotted.
 
    >>> d = get_countries_from_file("large_co2_data.tsv")
    >>> data = get_bar_historical_co2_by_continent(d, 2018)
    
    >>> data[:2]
    [44731.870999999985, 585465.9030000004]
    
    >>> len(data)
    6
    
    >>> round(data[2], 1)
    523681.8
 
    """
    
    # Assigning local variables
    continents_list = ['AFRICA', 'ASIA', 'EUROPE', 'NORTH AMERICA', 'OCEANIA', 'SOUTH AMERICA']
    continents_co2_list = [0, 0, 0, 0, 0, 0]
    countries_list = []
    continents_list_copy = []
    continents_co2_list_copy = []
    
    # Adding the Country objects into a list
    for country in countries_dict:
        countries_list.append(countries_dict[country])
    
    # Getting the dictionary continent-countries key-value
    continents_dict = Country.get_countries_by_continent(countries_list)
    
    # Looping through each continent of continents_dict
    for continent in continents_dict:
        
        # Getting the continent's total co2 emissions per capita by year
        continent_co2 = Country.get_total_historical_co2_emissions(continents_dict[continent], country_year)
        
        # Adding continent_co2 to continents_co2_list at the right continent's index
        if continent_co2 != None:
            continents_co2_list[continents_list.index(continent)] += continent_co2
    
    # Looping through each continent's co2 emissions in continents_co2_list
    for continent_co2_value in continents_co2_list:
        
        # Doing a copy of continents_list and continents_co2_list while removing the continents that didn't have co2 emissions
        if continent_co2_value != 0:
            continents_list_copy.append(continents_list[continents_co2_list.index(continent_co2_value)])
            continents_co2_list_copy.append(continent_co2_value)
        
    # Creating the bar graph
    plt.bar(continents_list_copy, continents_co2_list_copy)
    plt.title('Historical CO2 emissions up to ' + str(country_year) + ' by sandy.nguyen2@mail.mcgill.ca')
    plt.ylabel('co2 (in millions of tonnes)')
    plt.savefig('hist_co2_pc_by_continent_' + str(country_year))
    plt.show()
    
    return continents_co2_list_copy
 
def get_bar_co2_pc_top_ten(countries_dict, country_year):
    
    """ (dict, int) -> list
    This function creates a bar plot representing the co2 emissions per capita (in tonnes) produced by the top 10
    producing countries in the dictionary and returns a list of values being plotted.
 
    >>> d = get_countries_from_file("large_co2_data.tsv")
    >>> data = get_bar_co2_pc_top_ten(d, 2000)
    
    >>> data[:2]
    [58.388513513513516, 35.669432035737074]
    
    >>> len(data)
    10
    
    >>> round(data[2], 1)
    28.3
 
    """
    
    country_dict = {}
    country_list = []
    co2_emissions_list = []
    
    for country in countries_dict:
        
        # Getting the country's co2 emissions at that year
        country_co2 = Country.get_co2_per_capita_by_year(countries_dict[country], country_year)
        
        # Taking into account if the country_co2 was a NoneType
        if country_co2 != None:
            country_dict[countries_dict[country]] = country_co2
        else:
            country_dict[countries_dict[country]] = -1
    
    # Getting the top 10 countries' co2 emissions
    top_10_country = Country.get_top_n(country_dict, 10)
    
    for country_tup in top_10_country:
        
        # Adding the country's iso code and co2 emissions in their respective lists
        country_iso_code, country_co2_emissions = country_tup
        country_list.append(country_iso_code)
        co2_emissions_list.append(country_co2_emissions)
    
    # If there's less than 10 countries and some has -1 co2 emissions
    for i in range(co2_emissions_list.count(-1)):
        co2_emissions_list.remove(-1)
        
    country_list = country_list[:len(co2_emissions_list)]
    
    # Creating the bar graph
    plt.bar(country_list, co2_emissions_list)
    plt.title('Top 10 countries for CO2 emissions pc in ' + str(country_year) + ' by sandy.nguyen2@mail.mcgill.ca')
    plt.ylabel('co2 (in tonnes)')
    plt.savefig('top_10_co2_pc_' + str(country_year))
    plt.show()
    
    return co2_emissions_list
 
 
def get_bar_top_ten_historical_co2(countries_dict, country_year):
    """ (dict, int) -> list
    This function creates a bar plot representing the historical co2 emissions (in millions of tonnes) produced
    by the top 10 producing countries in the dictionary and returns a list of values being plotted.
 
    >>> d = get_countries_from_file("large_co2_data.tsv")
    >>> get_bar_top_ten_historical_co2(d, 2015)
    
    >>> data[:2]
    [388775.708, 180593.26000000004]
    
    >>> len(data)
    10
    
    >>> round(data[2], 1)
    95745.0
    
    """
    
    country_dict = {}
    country_list = []
    co2_emissions_list = []
    
    for country in countries_dict:
        
        # Getting the country's historical co2 emissions at that year
        country_co2 = Country.get_historical_co2(countries_dict[country], country_year)
        
        # Taking into account if the country_co2 was a NoneType
        if country_co2 != None:
            country_dict[countries_dict[country]] = country_co2
        else:
            country_dict[countries_dict[country]] = -1
    
    # Getting the top 10 countries' historical co2 emissions
    top_10_country = Country.get_top_n(country_dict, 10)
    
    for country_tup in top_10_country:
        
        # Adding the country's iso code and historical co2 emissions in their respective lists
        country_iso_code, country_co2_emissions = country_tup
        country_list.append(country_iso_code)
        co2_emissions_list.append(country_co2_emissions)
    
    # If there's less than 10 countries and some has -1 historical co2 emissions
    for i in range(co2_emissions_list.count(-1)):
        co2_emissions_list.remove(-1)
        
    country_list = country_list[:len(co2_emissions_list)]
    
    # Creating the bar graph
    plt.bar(country_list, co2_emissions_list)
    plt.title('Top 10 countries for historical CO2 up to ' + str(country_year) + ' by sandy.nguyen2@mail.mcgill.ca')
    plt.ylabel('co2 (in millions tonnes)')
    plt.savefig('top_10_hist_co2_' + str(country_year))
    plt.show()
    
    return co2_emissions_list
 
def get_plot_co2_emissions(countries_dict, isocodes_list, min_year, max_year):
    """ (dict, list, int, int) -> 2D list
    This function will plot the co2 emissions of the selected countries (those whose ISO appears in the input list)
    from min_year to max_year and return a 2D list where each sublist contains the co2 emissions of a selected country
    from min_year to max_year.
    
    >>> d = get_countries_from_file("large_co2_data.tsv")
    >>> data = get_plot_co2_emissions(d, ["USA", "CHN", "RUS", "DEU", "GBR"], 1990, 2000)
    
    >>> data[0]
    [5121.179, 5071.564, 5174.671, 5281.387, 5375.034, 5436.698, 5625.042, 5701.921, 5749.893, 5829.52, 5997.299]
    
    >>> len(data)
    5
    
    >>> round(data[2], 1)
    1957.9
 
    """
    country_min_year = min_year + 0
    
    # Empty lists
    x_coord = []
    y_coord = []
    y_coord_to_return = []
    
    # Empty sublists
    country_x_coord = []
    country_y_coord = []
    
    # Lines and variables
    lines = ['-', ':', '--', '-.', '-']
    markers = ['4', 'o', '|', 'd', 's']
    
    steps = round((max_year - min_year) / 10)
    
    for isocode in isocodes_list:
        
        # Appending the country's year (up by steps) and co2 emissions to their respective sublists
        while country_min_year <= max_year:
            country_co2 = Country.get_co2_emissions_by_year(countries_dict[isocode], country_min_year)
            country_x_coord.append(country_min_year)
            country_y_coord.append(country_co2)
            country_min_year += steps
        
        # Appending and initializing the local variables
        x_coord.append(country_x_coord)
        y_coord.append(country_y_coord)
        country_x_coord = []
        country_y_coord = []
        country_min_year = min_year + 0
        
        # Appending the country's co2 emissions for every year (up by 1) to country_y_coord
        while country_min_year <= max_year:
            country_co2 = Country.get_co2_emissions_by_year(countries_dict[isocode], country_min_year)
            country_y_coord.append(country_co2)
            country_min_year += 1
        
        # Appending and initializing the local variables
        y_coord_to_return.append(country_y_coord)
        country_x_coord = []
        country_y_coord = []
        country_min_year = min_year + 0
        
    # Creating the bar graph
    for i in range (len(x_coord)):
        plt.plot(x_coord[i], y_coord[i], (markers[i] + lines[i]))
    plt.title('CO2 emissions between ' + str(min_year) + ' and ' + str(max_year) + ' by sandy.nguyen2@mail.mcgill.ca')
    plt.ylabel('co2 (in millions tonnes)')
    plt.legend(isocodes_list)
    plt.savefig('co2_emissions_' + str(min_year) + '_' + str(max_year))
    plt.show()
    
    return y_coord_to_return