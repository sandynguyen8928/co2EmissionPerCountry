# Author: Sandy Nguyen

def find_delim(line):
    
    """ (str) -> str
    This function takes a string representing a line as input and returns the most commonly used
    delimiter in the input string.
    
    >>> find_delim("1,2,3,4")
    ','
    
    >>> find_delim("1 2 3,4")
    ' '
    
    >>> find_delim("1234")
    AssertionError

    """
    
    # Creating local variables
    delim = ['\t', ',', ' ', '-']
    delim_counter = [0, 0, 0, 0]
    
    for char in line:
        
        # If char is in delim, add 1 to the delim_counter to the char's index
        if char in delim:
            delim_counter[delim.index(char)] += 1
    
    # If the maximum integer in delim_counter is 0, that means there were no delim in the string
    if max(delim_counter) == 0:
        raise AssertionError
    
    # Returning the delim according to its maximum integer in delim_counter 
    else:
        return delim[delim_counter.index(max(delim_counter))]
    
    
def clean_one(input_filename, output_filename):
    
    """ (str, str) -> int
    This function takes two strings representing files (intput_filename and output_filename), reads the
    input_filename, makes changes to each of the line (each line should have a tab as delimiter in place
    of whichever delimiter each line originally had) and write the new version to output_filename.
    It returns an integer indicating the number of lines written to output_filename.
    
    >>> clean_one('books_raw_data.tsv', 'books_tab_sep_data.tsv')
    7
    
    >>> clean_one('movies_raw_data.tsv', 'movies_tab_sep_data.tsv')
    12
    
    >>> clean_one('shows_raw_data.tsv', 'shows_tab_sep_data.tsv')
    34

    """
    
    # Opening all the files and creating local variables
    fobj_input = open(input_filename, "r", encoding="utf-8")
    fobj_output = open(output_filename, "w", encoding="utf-8")
    num_of_lines = 0
    
    for line in fobj_input:
        
        # Replace all the delim with a tab and writing it in the output_filename
        delim = find_delim(line)
        new_line = line.replace(delim, '\t')
        fobj_output.write(new_line)
        num_of_lines += 1
    
    fobj_input.close()
    fobj_output.close()

    return num_of_lines  
     

def final_clean(input_filename, output_filename):
    
    """ (str, str) -> int
    This function takes two strings representing files (intput_filename and output_filename), reads the
    input_filename, makes changes to each of the line (each line should have 5 columns and all commas which are
    used to indicate a decimal number should be replace with dots) and write the new version to output_filename.
    It returns an integer indicating the number of lines written to output_filename.
    
    >>> final_clean('books_tab_sep_data.tsv', 'books_clean_data.tsv')
    7
    
    >>> final_clean('movies_tab_sep_data.tsv', 'movies_clean_data.tsv')
    12
    
    >>> final_clean('shows_tab_sep_data.tsv', 'shows_clean_data.tsv')
    34

    """
    
    # Opening all the files and creating local variables
    fobj_input = open(input_filename, "r", encoding="utf-8")
    fobj_output = open(output_filename, "w", encoding="utf-8")
    num_of_lines = 0
    
    for line in fobj_input:
        
        delim = find_delim(line)
        line_dot = line.replace(',', '.')
        line_list = line_dot.split(delim)
        
        # If the the list has 5 columns
        if len(line_list) == 5:
            line_list_tab = '\t'.join(line_list)
            fobj_output.write(line_list_tab)
            num_of_lines += 1
        
        # If the deliminiter is a comma, then line wasn't split into parts since they were all replaced by dots
        elif len(line_list) == 1:
            line_list = line_dot.split('.')
            line_list = line_list[:3] + [line_list[3] + '.' + line_list[4]] + [line_list[5]]
            line_list_tab = '\t'.join(line_list)
            fobj_output.write(line_list_tab)
            num_of_lines += 1
        
        # If the list has more than 6 columns
        else:
        
            while len(line_list) >= 5:
                
                # If the third column is an integer
                try:
                    if type(int(line_list[2])) == int:
                        
                        # If the the list has 5 columns, everything is goodies
                        if len(line_list) == 5:
                            line_list_tab = '\t'.join(line_list)
                            fobj_output.write(line_list_tab)
                            num_of_lines += 1
                            break
                        
                        # If the the list has 6 columns, join the third and fourth column with a dot
                        elif len(line_list) == 6:
                            line_list = line_list[:3] + [line_list[3] + '.' + line_list[4]] + [line_list[5]]
                            line_list_tab = '\t'.join(line_list)
                            fobj_output.write(line_list_tab)
                            num_of_lines += 1
                            break

                # If the third column isn't an integer, add the third and fourth column together
                except ValueError:
                    line_list = [line_list[0]] + [line_list[1] + ' ' + line_list[2]] + line_list[3:]
    
    fobj_input.close()
    fobj_output.close()
    
    return num_of_lines