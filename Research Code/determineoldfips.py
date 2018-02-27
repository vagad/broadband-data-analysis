def filter_lines(in_filename, out_filename, out_filename1):
    """Read records from in_filename and write records to out_filename if
    the beginning of the line (taken up to the first comma at or after
    position 11) is found in keys (which must be a set of byte strings).

    """
    counter = 0
    ten_vals = 0
    twenty_vals = 0
    ten_dict = {}
    twenty_dict = {}
    with open(in_filename, 'r') as in_f, open(out_filename, 'w') as out_f, open(out_filename1, 'w') as out_f1:
        for line in in_f:
            if(counter >= 1):
                vals = line.split(",")
                fips = vals[1]
                upload = vals[-3]
                download = vals[-2]

                if (counter % 100000 == 0):
                    print("Another 100k done" + str(counter))

                if(float(upload) >= 3 and float(download) >= 25):
                    if fips not in twenty_dict:
                        twenty_dict[fips] = 1
                        twenty_vals += 1
                        new_line = fips+"\n"
                        out_f.write(new_line)

                if(float(upload) >= 1 and float(download) >= 10):
                    if fips not in ten_dict:
                        ten_dict[fips] = 1
                        ten_vals += 1
                        new_line = fips+"\n"
                        out_f1.write(new_line)

            counter += 1
        
    print(ten_vals)
    print(twenty_vals)
    print(counter)
    
    return 

in_filename1 = "/Users/VamsiG/Music/Research_Work/FCC_Output_2014.txt"
out_filename1 = "/Users/VamsiG/Music/Research_Work/Research_Code/2014_253.csv"
out_filename2 = "/Users/VamsiG/Music/Research_Work/Research_Code/2014_101.csv"

filter_lines(in_filename1,out_filename1,out_filename2)