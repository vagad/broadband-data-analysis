def filter_lines(in_filename, out_filename):
    """Read records from in_filename and write records to out_filename if
    the beginning of the line (taken up to the first comma at or after
    position 11) is found in keys (which must be a set of byte strings).

    """
    counter = 0
    new_vals = 0
    fips_dictionary = {}
    with open(in_filename, 'r') as in_f, open(out_filename, 'w') as out_f:
        for line in in_f:
            counter += 1
            vals = line.split(",")
            fips = vals[2]
            if (counter % 100000 == 0):
                print("Another 100k done")

            if(fips in fips_dictionary):
                fips_dictionary[fips] = fips_dictionary[fips] + 1
            else:
                fips_dictionary[fips] = 1
        for k,v in fips_dictionary.items():
            new_line = k+","+str(v)+"\n"
            out_f.write(new_line)
            new_vals += 1

    return (counter, new_vals)

in_filename1 = "/Users/VamsiG/Music/2016_Data/FCC_Output.csv"
out_filename1 = "/Users/VamsiG/Music/2016_Data/FCC_Final_Output.csv"

in_filename2 = "/Users/VamsiG/Music/2014_Data/FCC_Output.csv"
out_filename2 = "/Users/VamsiG/Music/2014_Data/FCC_Final_Output.csv"

counter1, new_vals1 = filter_lines(in_filename1,out_filename1)
counter2, new_vals2 = filter_lines(in_filename2,out_filename2)
print(counter1)
print(new_vals1)
print(counter2)
print(new_vals2)
