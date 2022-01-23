# Author: Sandy Nguyen

def get_iso_codes_by_continent(iso_filename):
    """ (str) -> dict
    This function takes a file with format 'ISO country code\tcontinent\n' and returns a dictionary mapping continents'
    names to a list of ISO codes of countries that belongs to that continent.
    
    >>> d = get_iso_codes_by_continent("iso_codes_by_continent.tsv")
    
    >>> d['OCEANIA']
    ['NRU', 'VUT', 'NZL', 'TON', 'KIR', 'WSM', 'PLW', 'TUV', 'NIU', 'PNG', 'SLB', 'FJI', 'AUS', 'MHL']
    
    >>> len(d['AFRICA'])
    53
    
    >>> d['SOUTH AMERICA'][0]
    'URY'
    
    """
    
    fobj = open(iso_filename, "r", encoding="utf-8")
    continents_dict = {}
    
    for line in fobj:
        
        # Stripping line from \n and splitting it with \t
        line_strip = line.strip('\n')
        line_list = line_strip.split('\t')
        
        # If the continent key doesn't exist in the dictionary, add the continent-ISO pair into the dictionary
        if line_list[1].upper() not in continents_dict:
            continents_dict[line_list[1].upper()] = [line_list[0]]
        
        # If the continent key already exist in the dictionary, append ISO into its key continent.
        else:
            continents_dict[line_list[1].upper()].append(line_list[0])
    
    return continents_dict


def add_continents_to_data(input_filename, continents_filename, output_filename): 
    """ (str, str, str) -> int
    This function takes three strings representing files (input_filename, continents_filename, output_filename), reads the
    input_filename, makes changes to each of the line (each line should have a third column, after the name of the country,
    representing the continent to which the country belongs to) and write the new version to output_filename.
    It returns an integer indicating the number of lines written to output_filename.
    
     >>> add_continents_to_data('books_clean_data.tsv', 'books_rankings.tsv')
    7
    
    >>> add_continents_to_data('movies_clean_data.tsv', 'movies_rankings.tsv')
    12
    
    >>> add_continents_to_data('shows_clean_data.tsv', 'shows_rankings.tsv')
    34
    
    """
    
    # Opening files and creating local variables
    fobj_input = open(input_filename, "r", encoding="utf-8")
    fobj_continents = open(continents_filename, "r", encoding="utf-8")
    continents_dict = get_iso_codes_by_continent(continents_filename)
    num_of_lines = 0
    
    countries_dict = {}
    
    for line in fobj_input:
        
        # Creating a list with each country's informations
        line_list = line.split('\t')
        
        # Creating tuples with continents_dict
        for continent, countries in continents_dict.items():
            
            # If the country's ISO code is in the continent's countries
            if line_list[0] in countries:
                
                # If the country's ISO code is already a key in countries_dict
                if line_list[0] in countries_dict:
                    
                    # If the continent is already added as a value for the country's ISO code key
                    if continent not in countries_dict[line_list[0]]:
                        countries_dict[line_list[0]].append(continent)
                
                # If the country's ISO code is not a key in countries_dict yet 
                else:
                    countries_dict[line_list[0]] = [continent]
    
    # Closing files
    fobj_input.close()
    fobj_continents.close()
    
    # Opening files
    fobj_input = open(input_filename, "r", encoding="utf-8")
    fobj_output = open(output_filename, "w", encoding="utf-8")
                    
    for line in fobj_input:
        
        # Creating a list with each country's informations
        line_list = line.split('\t')
    
        # If the country only belongs to one continent    
        if len(countries_dict[line_list[0]]) == 1:
            line_continent = line_list[:2] + countries_dict[line_list[0]] + line_list[2:]
            line_continent_tab = '\t'.join(line_continent)
            fobj_output.write(line_continent_tab)
            num_of_lines += 1
        
        # If the country belongs to more than one continent
        else:
            line_continent = line_list[:2] + [','.join(countries_dict[line_list[0]])] + line_list[2:]
            line_continent_tab = '\t'.join(line_continent)
            fobj_output.write(line_continent_tab)
            num_of_lines += 1
            
    # Closing files 
    fobj_input.close()
    fobj_output.close()
    
    return num_of_lines