# Author: Sandy Nguyen

from copy import copy

class Country:
    
    """
    Represents a country
    
    Instance Attributes: iso_code (str), name (str), continents (list), co2_emissions (dict), population (dict)
    Class Attributes: min_year_recorded (int), min_year_recorded (int).
    
    """
    
    min_year_recorded = 1000000
    max_year_recorded = 0
    
    
    def __init__(self, iso_code, name, continents, year, country_co2, country_pop):
        
        """ (str, str, list, int, float, int) -> void
        This constructor will initialize the object's attributes
        
        >>> r = Country("RUS", "Russia", ["ASIA","EUROPE"], 2007, 1604.778, 14266000)
        >>> r.continents
        ["ASIA","EUROPE"]
        
        >>> a = Country("AFG", "Afghnistan", ["ASIA"], 1949, 0.015, 7663783)
        >>> Country.min_year_recorded
        1949
        
        >>> b = Country("ALB", "Albania", ["EUROPE"], 2007, 3.924, 3034000)
        >>> b.population
        {2007: 3034000}

        """
        
        # Initializing the object attributes
        self.iso_code = iso_code
        self.name = name
        self.year = int(year)
        self.continents = continents.copy()
        self.country_co2 = country_co2
        self.country_pop = country_pop
        
        if self.country_co2 != '':
            self.country_co2 = float(self.country_co2)
        if self.country_pop != '':
            self.country_pop = int(self.country_pop)
        
        self.co2_emissions = {}
        self.population = {}
        
        # Updating the Country's minimum/maximum year recorded
        if Country.min_year_recorded > int(self.year):
            Country.min_year_recorded = int(self.year)
            
        if Country.max_year_recorded < int(self.year):
            Country.max_year_recorded = int(self.year)
        
        # If the country's ISO code isn't valid, raise an exception
        if len(iso_code) != 3 and iso_code != 'OWID_KOS':
            raise AssertionError
        
        # If we recorded the country's co2 emissions that year, add the year-co2 emission pair in self.co2_emissions 
        if self.country_co2 not in [-1, '']:
            self.co2_emissions[self.year] = self.country_co2
        
        # If we recorded the country's population that year, add the year-population pair in self.population
        if self.country_pop not in [-1, '']:
            self.population[self.year] = self.country_pop
            

    def __str__(self):
        
        """ obj -> str
        This string method takes an object and return a string representation of a country containting its name, continents,
        co2 emissions and population, all separated by a tab.
        
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> str(r)
        'Russia\\tASIA,EUROPE\\t{2007: 1604.778}\\t{2007: 14266000}'
        
        >>> a = Country("AFG", "Afghnistan", ["ASIA"], 1949, 0.015, 7663783)
        >>> str(a)
        'Afghnistan\\tASIA\\t{1949: 0.015}\\t{1949: 7663783}'
        
        >>> b = Country("ALB", "Albania", ["EUROPE"], 2007, 3.924, 3034000)
        >>> str(b)
        'Albania\\tEUROPE\\t{2007: 3.924}\\t{2007: 3034000}'

        """
        
        # If the country belongs to more than 1 continent
        if type(self.continents) == list:
            return self.name + '\t' + ','.join(self.continents) + '\t' + str(self.co2_emissions) + '\t' + str(self.population)
        
        # If the country belongs to only 1 continent
        else:
            return self.name + '\t' + self.continents + '\t' + str(self.co2_emissions) + '\t' + str(self.population)
    
    
    def add_yearly_data(self, str_data):
        
        """ (str) -> void
        This instance method takes a string representing the year, co2 emissions and population, all separated by a tab and updates
        the appropriate attributes of the country.
        
        >>> a = Country("AFG", "Afghnistan", ["ASIA"], 1949, 0.015, 7663783)
        >>> a.add_yearly_data('2018\\t9.439\\t37122000')
        >>> Country.max_year_recorded
        2018
        
        >>> q = Country("QAT", "Qatar", ["ASIA"], 2007, 62.899, 1218000)
        >>> q.add_yearly_data("1993\\t30.985\\t501000")
        >>> q.co2_emissions
        {2007: 62.899, 1993: 30.985}
        
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> r.add_yearly_data("1971\\t1533.262\\t130831000")
        >>> q.population
        {2007: 1218000, 1993: 501000}
        
        """
        
        str_data_list = str_data.split('\t')
        
        # Adding the key year and co2 emissions value into the self.co2_emissions dictionary
        if str_data_list[1] != '':
            self.co2_emissions[int(str_data_list[0])] = float(str_data_list[1])
        
        # Adding the key year and population value into the self.population dictionary
        if str_data_list[2] != '':
            self.population[int(str_data_list[0])] = int(str_data_list[2])
        
        # Updating the Country's minimum/maximum year recorded
        if Country.min_year_recorded > self.year:
            Country.min_year_recorded = self.year
            
        if Country.max_year_recorded < self.year:
            Country.max_year_recorded = self.year
        
        
    def get_co2_emissions_by_year(self, country_year):
        
        """ (int) -> float
        This instance method takes an integer as input and returns the co2 emissions of the country
        in the specified year if available, 0.0 otherwise.
        
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> r.get_co2_emissions_by_year(2007)
        1604.778
        
        >>> a = Country("AFG", "Afghnistan", ["ASIA"], 1949, 0.015, 7663783)
        >>> a.add_yearly_data('2018\\t9.439\\t37122000')
        >>> a.get_co2_emissions_by_year(2018)
        9.439
        
        >>> b = Country("ALB", "Albania", ["EUROPE"], 2007, 3.924, 3034000)
        >>> b.get_co2_emissions_by_year(2001)
        0.0
        
        """
        
        # Returning the country's co2 emissions for year
        try:
            return self.co2_emissions[country_year]
        
        # If the key year doesn't exist in the self.co2_emissions dictionary
        except KeyError:
            return 0.0
    
    
    def get_co2_per_capita_by_year(self, country_year):
        
        """ (int) -> float
        This instance method takes an integer as input and returns the co2 emissions per capita in tonnes
        for the specified year if available, None otherwise.
        
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> round(r.get_co2_per_capita_by_year(2007), 3)
        12.490
        
        >>> a = Country("AFG", "Afghnistan", ["ASIA"], 1949, 0.015, 7663783)
        >>> a.add_yearly_data('2018\\t9.439\\t37122000')
        >>> round(a.get_co2_per_capita_by_year(2018), 5)
        0.25427
        
        >>> b = Country("ALB", "Albania", ["EUROPE"], 2007, 3.924, 3034000)
        >>> print(b.get_co2_per_capita_by_year(2001))
        None

        """
        
        # Returning the country's co2 emissions per capita in tonnes for the year
        try:
            return (float(self.co2_emissions[country_year]) / int(self.population[country_year])) * 1000000
        
        # If the key year doesn't exist in the self.co2_emissions dictionary
        except KeyError:
            return None
    
    
    def get_historical_co2(self, country_year):
        
        """ (int) -> float
        This instance method takes an integer as input representing a year and returns the total co2 emissions
        in millions of tonnes that the country has produced for all years up to and including the specified year.
        
        >>> q = Country("QAT", "Qatar", ["ASIA"], 2007, 62.899, 1218000)
        >>> q.add_yearly_data("1993\\t30.985\\t501000")
        >>> q.add_yearly_data("1989\\t14.292\\t462000")
        >>> q.get_historical_co2(2000)
        45.277
        
        >>> a = Country("AFG", "Afghnistan", ["ASIA"], 1949, 0.015, 7663783)
        >>> a.add_yearly_data('2018\\t9.439\\t37122000')
        >>> a.get_historical_co2(2020)
        9.454
        
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> r.add_yearly_data("1971\\t1533.262\\t130831000")
        >>> r.get_historical_co2(1960)
        0.0

        """
        
        sum_co2_emissions = 0.0
        
        for key_year in self.co2_emissions:
            
            # If the key_year is smaller or equal to the country_year
            if key_year <= country_year:
                
                # Add the co2_emission of that year in sum_co2_emissions
                sum_co2_emissions += float(self.co2_emissions[key_year])
        
        return sum_co2_emissions
    
    
    @classmethod
    def get_country_from_data(self, country_info):
        
        """ (str) -> obj
        This class method takes a string that has a country's information and return a new Country object created
        from the data in the input string.
        
        >>> a = Country.get_country_from_data("ALB\\tAlbania\\tEUROPE\\t1991\\t4.283\\t3280000")
        >>> str(a)
        'Albania\\tEUROPE\\t{1991: 4.283}\\t{1991: 3280000}'
        
        >>> q = Country.get_country_from_data("QAT\\tQatar\\tASIA\\t2007\\t62.899\\t1218000")
        "Qatar\\tASIA\\t{'2007': '62.899'}\\t{'2007': '1218000'}"
        
        >>> r = Country.get_country_from_data("RUS\\tRussia\\tASIA,EUROPE\\t2007\\t1604.778\\t14266000")
        "Russia\tASIA,EUROPE\t{'2007': '1604.778'}\t{'2007': '14266000'}"

        """
        
        info = country_info.split('\t')
        
        if type(info[2]) == str:
            info[2] = [info[2]]
        
        # Creating a new Country object with the country's information
        return Country(info[0], info[1], info[2], info[3], info[4], info[5])
    
    
    @staticmethod
    def get_countries_by_continent(list_of_countries):
        
        """ (list) -> dict
        This function takes a list of countries (objects of type Country) and return a dictionary mapping
        a string representating a continent to a list of countries which all belong to that continent.
        
        >>> a = Country("AFG", "Afghanistan", ["ASIA"], 1949, 0.015, 7663783)
        >>> b = Country("ALB", "Albania", ["EUROPE"], 2007, 3.924, 3034000)
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> d = Country.get_countries_by_continent([a, b, r])
        >>> len(d)
        2
        
        >>> a = Country("AFG", "Afghanistan", ["ASIA"], 1949, 0.015, 7663783)
        >>> a.add_yearly_data("2018\\t9.439\\t37122000")
        >>> b = Country("ALB", "Albania", ["EUROPE"], 2007, 3.924, 3034000)
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> d = Country.get_countries_by_continent([a, b, r])
        >>> str(d['ASIA'][1])
        'Russia\\tASIA,EUROPE\\t{2007: 1604.778}\\t{2007: 14266000}'
        
        >>> q = Country("QAT", "Qatar", ["ASIA"], 2007, 62.899, 1218000)
        >>> q.add_yearly_data("1993\\t30.985\\t501000")
        >>> q.add_yearly_data("1989\\t14.292\\t462000")
        >>> d = Country.get_countries_by_continent([q])
        >>> d['ASIA'][0].name
        'Qatar'

        """
        
        continents_dict = {}
        
        # Looping through each country in the list of countries
        for country in list_of_countries:
            
            country_continents = country.continents
            
            # If the continents are in a list
            if type(country_continents) != list:
                country_continents = country.continents.split(', ')
                
            # Looping through each continent belonging to that country
            for continent in country_continents:
                
                # If the continent isn't already in the continents_dict dictionary, add key continent and country value
                if continent not in continents_dict:
                    continents_dict[continent] = [country]
                
                # If the continent is already in the continents_dict dictionary, append the country to the continent key value
                else:
                    continents_dict[continent].append(country)
                
        return continents_dict
    
    
    @staticmethod
    def get_total_historical_co2_emissions(list_of_countries, country_year):
        
        """ (list, int) -> dict
        This static method takes as input a list of countries (objects of type Country) and an integer representing a year and
        returns a dictionary mapping objects of type Country to floats representing the total co2 emissions produced by that
        country for all years up to and including the specified year.
        
        >>> b = Country("ALB", "Albania", ["EUROPE"], 2007, 3.924, 3034000)
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> q = Country("QAT", "Qatar", ["ASIA"], 2007, 62.899, 1218000)
        >>> b.add_yearly_data("1991\\t4.283\\t3280000")
        >>> q.add_yearly_data("1993\\t30.985\\t501000")
        >>> q.add_yearly_data("1989\\t14.292\\t462000")
        >>> Country.get_total_historical_co2_emissions([b, r, q], 2007)
        1721.161
        
        >>> b = Country("ALB", "Albania", ["EUROPE"], 2000, 3.924, 3034000)
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2000, 1604.778, 14266000)
        >>> q = Country("QAT", "Qatar", ["ASIA"], 2000, 62.899, 1218000)
        >>> Country.get_total_historical_co2_emissions([b, r, q], 2000)
        1671.601
        
        >>> b = Country("ALB", "Albania", ["EUROPE"], 2007, 3.924, 3034000)
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> q = Country("QAT", "Qatar", ["ASIA"], 2007, 62.899, 1218000)
        >>> Country.get_total_historical_co2_emissions([b, r, q], 2000)
        0.0
        
        """
        
        # Assigning local variables
        continents_dict = Country.get_countries_by_continent(list_of_countries)
        sum_co2_emissions = 0.0
        country_list = []
        
        # Looping through each continent from continents_dict
        for continent in continents_dict:
            
            # Looping through each country from the continent key value
            for country in continents_dict[continent]:
                
                # If the country isn't already in the list of countries (that means we haven't added the country's co2 emissions)
                if country not in country_list:
                    sum_co2_emissions += Country.get_historical_co2(country, country_year)
                    country_list.append(country)
        
        return sum_co2_emissions

    @staticmethod
    def get_total_co2_emissions_per_capita_by_year(list_of_countries, country_year):
        
        """ (list, int) -> dict
        This static method takes a list of countries (objects of type Country) and an integer representing a year as inputs and
        returns the co2 emissions per capita in tonnes produced by the countries in the given list of countries in the specified year.
        
        >>> b = Country("ALB", "Albania", ["EUROPE"], 2007, 3.924, 3034000)
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> round(Country.get_total_co2_emissions_per_capita_by_year([b, r], 2007), 5)
        92.98855
        
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2000, 1604.778, -1)
        >>> q = Country("QAT", "Qatar", ["ASIA"], 2000, 62.899, 1218000)
        >>> round(Country.get_total_co2_emissions_per_capita_by_year([r, q], 2000), 2)
        51.64
        
        >>> b = Country("ALB", "Albania", ["EUROPE"], 2007, 3.924, -1)
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, -1)
        >>> Country.get_total_co2_emissions_per_capita_by_year([b, r], 2007)
        0.0
        
        """
        
        # Assigning local variables
        sum_co2_emissions = 0.0
        sum_population = 0
        
        # Looping through each country in list_of_countries
        for country in list_of_countries:
            
            # If the year is a key in the country's co2_emissions and population dictionaries
            if country_year in country.co2_emissions and country_year in country.population:
                sum_co2_emissions += float(country.co2_emissions[country_year])
                sum_population += int(country.population[country_year])
        
        # Returning the co2 emissions per capita
        try:
            return (sum_co2_emissions / sum_population) * 1000000
        
        # If the total co2 emissions or population is 0
        except ZeroDivisionError:
            return 0.0
        
        
    @staticmethod
    def get_co2_emissions_per_capita_by_year(list_of_countries, country_year):
        
        """ (list, int) -> dict
        This static method takes a list of countries (objects of type Country) and an integer representing a year
        as inputs and returns a dictionary mapping objects of type Country to floats representing the co2 emissions
        per capita in tonnes produced by the country in the specified year.
        
        >>> b = Country("ALB", "Albania", ["EUROPE"], 2007, 3.924, 3034000)
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> d1 = Country.get_co2_emissions_per_capita_by_year([b, r], 2007)
        >>> round(d1[r], 5)
        112.4897
        
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2000, 1604.778, 14266000)
        >>> q = Country("QAT", "Qatar", ["ASIA"], 2000, 62.899, 1218000)
        >>> round(Country.get_co2_emissions_per_capita_by_year([r, q], 2000)[q], 2)
        51.64
        
        >>> b = Country("ALB", "Albania", ["EUROPE"], 2007, 3.924, 3034000)
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> d1 = Country.get_co2_emissions_per_capita_by_year([b, r], 1999)
        >>> d1[r]
        None

        """
        
        # Assigning a local variable
        country_co2_dict = {}
        
        # Looping through each country in list_of_countries
        for country in list_of_countries:
            
            # Creating a country key and country's co2 emissions per capita during country_year value
            country_co2_dict[country] = Country.get_co2_per_capita_by_year(country, country_year)
        
        return country_co2_dict
       
       
    @staticmethod
    def get_historical_co2_emissions(list_of_countries, country_year):
        
        """ (list, int) -> dict
        This static method takes a list of countries (objects of type Country) and an integer representing a year
        as inputs and returns a dictionary mapping objects of type Country to floats representing the co2 emissions
        per capita in tonnes produced by the country for all years up to and including the specified year.
        
        >>> q = Country("QAT", "Qatar", ["ASIA"], 2007, 62.899, 1218000)
        >>> q.add_yearly_data("1993\\t30.985\\t501000")
        >>> q.add_yearly_data("1989\\t14.292\\t462000")
        >>> d = Country.get_historical_co2_emissions([q], 2000)
        >>> round(d[q])
        45.277
        
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> a = Country("AFG", "Afghnistan", ["ASIA"], 1949, 0.015, 7663783)
        >>> a.add_yearly_data('2018\\t9.439\\t37122000')
        >>> d = Country.get_historical_co2_emissions([r, a], 2019)
        >>> d[a]
        9.454
        
        >>> b = Country("ALB", "Albania", ["EUROPE"], 2007, 3.924, 3034000)
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> q = Country("QAT", "Qatar", ["ASIA"], 2007, 62.899, 1218000)
        >>> d = Country.get_historical_co2_emissions([b, r, q], 1991)
        >>> print(d[r])
        0.0
        
        """
        
        # Assigning a local variable
        country_co2_dict = {}
        
        # Looping through each country in list_of_countries
        for country in list_of_countries:
            
            # Creating a country key and country's co2 emissions per capita during country_year value
            country_co2_dict[country] = Country.get_historical_co2(country, country_year)
        
        return country_co2_dict
    
    
    @staticmethod
    def get_top_n(countries_dict, n):
        
        """ (dict, int) -> list
        This static method takes a dictionary mapping objects of type Country to numbers and an integer n as inputs
        and returns a list of tuples.
        
        >>> a = Country("ALB", "Albania", [], 0, 0.0, 0)
        >>> b = Country("AUT", "Austria", [], 0, 0.0, 0)
        >>> c = Country("BEL", "Belgium", [], 0, 0.0, 0)
        >>> d = Country("BOL", "Bolivia", [], 0, 0.0, 0)
        >>> e = Country("BRA", "Brazil", [], 0, 0.0, 0)
        >>> f = Country("IRL", "Ireland", [], 0, 0.0, 0)
        >>> g = Country("MAR", "Marocco", [], 0, 0.0, 0)
        >>> h = Country("NZL", "New Zealand", [], 0, 0.0, 0)
        >>> i = Country("PRY", "Paraguay", [], 0, 0.0, 0)
        >>> j = Country("PER", "Peru", [], 0, 0.0, 0)
        >>> k = Country("SEN", "Senegal", [], 0, 0.0, 0)
        >>> l = Country("THA", "Thailand", [], 0, 0.0, 0)
        >>> t = Country.get_top_n({a: 5, b: 5, c: 3, d: 10, e: 3, f: 9, g: 7, h: 8, i: 7, j: 4, k: 6, l: 0}, 10)
        
        >>> t[:5]
        [('BOL', 10), ('IRL', 9), ('NZL', 8), ('MAR', 7), ('PRY', 7)]
        
        >>> t[2]
        ('NZL', 8)
        
        >>> print(t)
        [('BOL', 10), ('IRL', 9), ('NZL', 8), ('MAR', 7), ('PRY', 7), ('SEN', 6), ('ALB', 5), ('AUT', 5), ('PER', 4), ('BEL', 3)]

        """
        
        tuple_list = [] # List of tuples that will be returned at the end
        countries_list = [] # List containing all the country objects
        number_list = [] # List containing all the country objects' numbers
        countries_dup = [] # List of countries that have the same numbers
        
        # Looping through each country in countries_dict and unpairing its key-value into two separate lists
        for country in countries_dict:
            countries_list.append(country)
            number_list.append(countries_dict[country])
            
        # Looping through the top n countries
        while n > 0:
            
            try:
                number_max = max(number_list)
            except ValueError:
                break
            
            # If number_max doesn't occur more than once, create the country tuple and append into tuple_list
            if number_list.count(number_max) == 1:
                country_max = countries_list[number_list.index(number_max)]
                tuple_list.append((country_max.iso_code, number_max))
                countries_list.remove(country_max)
                number_list.remove(number_max)
                n -= 1
            
            # If number_max occur more than once
            else:
                
                # Appending all the countries that have the same number_max into countries_dup
                while number_list.count(number_max) != 0:
                    country_max = countries_list[number_list.index(number_max)]
                    countries_dup.append((country_max.name, country_max))
                    countries_list.remove(country_max)
                    number_list.remove(number_max)
                
                # As long as countries_dup isn't an empty list
                while countries_dup != []:
                    
                    # If n is not 0 yet, create the country tuple and append into tuple_list
                    if n != 0:
                        countries_dup.sort()
                        tuple_list.append((countries_dup[0][1].iso_code, number_max))
                        countries_dup.remove(countries_dup[0])
                        n -= 1
                    
                    # If n is 0, we don't want to add any more countries
                    else:
                        break
                
        return tuple_list


def get_countries_from_file(filename):
    """ (str) -> dict
    This function takes a string representing a filename as input and returns a dictionary mapping the countries' iso codes
    to object of type Country.
    
    >>> d1 = get_countries_from_file("small_co2_data.tsv")
    >>> d2 = get_countries_from_file("large_co2_data.tsv")
    
    >>> len(d1)
    9
    
    >>> 'RUS' in d1
    False
    
    >>> 'RUS' in d2
    True
    
    """
    
    # Opening files and creating local variables
    fobj = open(filename, "r", encoding="utf-8")
    fobj_dict = {}
    
    for line in fobj:
        
        # Striping and spliting line
        new_line = line.strip('\n')
        new_new_line = new_line.split('\t')
        
        # If the Country object hasn't been created yet
        if new_new_line[0] not in fobj_dict:
            country = Country.get_country_from_data(new_line)
            fobj_dict[country.iso_code] = country
        
        # If the Country object is already created, add yearly data
        else:
            join_new_new_line = (new_new_line[3] + '\t' + new_new_line[4] + '\t' + new_new_line[5])
            fobj_dict[new_new_line[0]].add_yearly_data(join_new_new_line)
    
    fobj.close()
            
    return fobj_dict