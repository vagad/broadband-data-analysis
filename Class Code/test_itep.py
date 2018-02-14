def filter_lines(in_filename, out_filename):
    """Read records from in_filename and write records to out_filename if
    the beginning of the line (taken up to the first comma at or after
    position 11) is found in keys (which must be a set of byte strings).

    """
    counter = 0
    new_vals = 0
    with open(in_filename, 'r', encoding='latin-1') as in_f, open(out_filename, 'w') as out_f:
        for line in in_f:
            counter += 1
            vals = line.split(",")
            download = vals[-5]
            if (counter % 1000000 == 0):
                print("Another 1 milli done")
            # if(counter <= 20):
            #     print(download)
            if (counter>1 and float(download) >= 25):
                provider_id = vals[1]
                provider_name = vals[3]
                fips = vals[-8]
                state = vals[-9]
                upload = vals[-4]
                new_line = provider_name.replace('"', '')+","+provider_id+","+fips+","+state+","+upload+","+download+"\n"
                if(counter <= 20):
                    print(counter)
                    print(new_line)
                out_f.write(new_line)
                new_vals += 1

    return (counter, new_vals)

in_filename1 = "/Users/VamsiG/fbd_us_with_satellite_dec2016_v1.csv"
out_filename1 = "/Users/VamsiG/Music/2016_Data/FCC_Output.csv"

in_filename2 = "/Users/VamsiG/fbd_us_with_satellite_dec2014_v1.csv"
out_filename2 = "/Users/VamsiG/Music/2014_Data/FCC_Output.csv"

counter1, new_vals1 = filter_lines(in_filename1,out_filename1)
counter2, new_vals2 = filter_lines(in_filename2,out_filename2)

print(counter1)
print(new_vals1)
print(counter2)
print(new_vals2)
