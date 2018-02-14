def filter_lines(in_filename, in_filename2,out_filename):
    """Read records from in_filename and write records to out_filename if
    the beginning of the line (taken up to the first comma at or after
    position 11) is found in keys (which must be a set of byte strings).

    """
    proper_convert = 0
    missing_convert = 0
    county_dictionary = {}
    with open(in_filename, 'r') as in_f, open(in_filename2, 'r') as in_f2, open(out_filename, 'w') as out_f:
        for line in in_f:
            vals = line.split("\t")
            fips = vals[1]
            lat = vals[-2]
            longitude = vals[-1]
            county_dictionary[fips] = (lat, longitude)
        
        for line in in_f2:
            vals = line.strip().split(",")
            fips = vals[0][:11]
            count = vals[1]
            lat,longitude = (0,0)
            if(fips in county_dictionary):   
                lat,longitude = county_dictionary[fips] 
                proper_convert += 1
            else:
                if(int(fips[:2]) <= 56):
                    missing_convert += 1
                    # print(vals)
            new_line = str(fips)+","+str(lat)+","+str(longitude)+"\n"
            out_f.write(new_line)
        


    return (proper_convert, missing_convert)

in_filename = "/Users/VamsiG/Music/2015_Gaz_tracts_national.txt"
in_filename1 = "/Users/VamsiG/Music/2016_Data/FCC_Final_Output.csv"
out_filename1 = "/Users/VamsiG/Music/2016_Data/FCC_Final_LatLong.csv"
in_filename2 = "/Users/VamsiG/Music/2014_Data/FCC_Final_Output.csv"
out_filename2 = "/Users/VamsiG/Music/2014_Data/FCC_Final_LatLong.csv"

counter1, new_vals1 = filter_lines(in_filename,in_filename1,out_filename1)
counter2, new_vals2 = filter_lines(in_filename,in_filename2,out_filename2)
print(counter1)
print(new_vals1)
print(counter2)
print(new_vals2)