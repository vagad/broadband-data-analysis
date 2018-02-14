def filter_lines(in_filename, in_filename2,out_filename):
    """Read records from in_filename and write records to out_filename if
    the beginning of the line (taken up to the first comma at or after
    position 11) is found in keys (which must be a set of byte strings).

    """
    proper_convert = 0
    missing_convert = 0
    fourteen_set = set()
    with open(in_filename, 'r') as in_f, open(in_filename2, 'r') as in_f2, open(out_filename, 'w') as out_f:
        for line in in_f:
            vals = line.strip().split(",")
            fips = vals[0]
            if(fips not in fourteen_set):
                fourteen_set.add(fips)
        
        for line in in_f2:
            vals = line.strip().split(",")
            fips = vals[0]
            count = vals[1]
            proper_convert += 1
            if(fips not in fourteen_set):
                new_line = str(fips)+","+str(count)+"\n"
                out_f.write(new_line)
                missing_convert += 1

    return (proper_convert, missing_convert)

in_filename = "/Users/VamsiG/Music/2014_Data/FCC_Final_Output.csv"
in_filename1 = "/Users/VamsiG/Music/2016_Data/FCC_Final_Output.csv"
out_filename= "/Users/VamsiG/Music/FCC_Overlap_CompleteFips.csv"

counter1, new_vals1 = filter_lines(in_filename,in_filename1,out_filename)
print(counter1)
print(new_vals1)