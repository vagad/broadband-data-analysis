def filter_lines(in_filename, in_filename2, in_filename3, out_filename, out_filename2 , out_filename3):
    """Read records from in_filename and write records to out_filename if
    the beginning of the line (taken up to the first comma at or after
    position 11) is found in keys (which must be a set of byte strings).

    """
    counter = 0
    new_vals = 0
    new_twenty_vals = 0
    ten_to_twenty_vals = 0
    ten_fips_dict = {}
    twenty_fips_dict = {}
    with open(in_filename, 'r') as in_f, open(in_filename2, 'r') as in_f2, open(in_filename3, 'r') as in_f3, open(out_filename, 'w') as out_f, open(out_filename2, 'w') as out_f2, open(out_filename3, 'w') as out_f3:
        for line in in_f:
            fips_val = line.rstrip()
            ten_fips_dict[fips_val] = 0

        print(len(ten_fips_dict)) 

        for line in in_f2:
            fips_val = line.rstrip()
            twenty_fips_dict[fips_val] = 0  
        
        print(len(twenty_fips_dict)) 
        
        for line in in_f3:
            # lrn,fips,provider_id,frn,provider_name,dba_name,hoco_name,hoco_num,hoco_final,state,tech_code,upload,download,year
            if(counter >= 1):
                vals = line.split(",")
                if (counter % 100000 == 0):
                        print("Another 100k done" + str(counter))

                upload = vals[-3]
                download = vals[-2]
                fips = vals[1]
                if((fips in ten_fips_dict) and (fips not in twenty_fips_dict) and float(upload) >= 3 and float(download) >= 25):
                    ten_to_twenty_vals += 1
                    tech_code = vals[-4]
                    state = vals[-5]
                    hoco_name = vals[6]
                    provider_name = vals[4]
                    new_line = str(fips)+","+str(upload)+","+str(download)+","+str(tech_code)+","+str(state)+","+str(hoco_name)+","+str(provider_name)+"\n"
                    out_f3.write(new_line)
                
                if((fips not in ten_fips_dict) and float(upload) >= 1 and float(download) >= 10):
                    tech_code = vals[-4]
                    state = vals[-5]
                    hoco_name = vals[6]
                    provider_name = vals[4]

                    new_line = str(fips)+","+str(upload)+","+str(download)+","+str(tech_code)+","+str(state)+","+str(hoco_name)+","+str(provider_name)+"\n"
                    out_f.write(new_line)

                    new_vals += 1

                    if(float(upload) >= 3 and float(download) >= 25):
                        new_twenty_vals  += 1
                        
                        new_line = str(fips)+","+str(upload)+","+str(download)+","+str(tech_code)+","+str(state)+","+str(hoco_name)+","+str(provider_name)+"\n"
                        out_f2.write(new_line)
            counter += 1
        
    print(new_vals)
    print(new_twenty_vals)
    print(ten_to_twenty_vals)
    
    return 

in_filename = "/Users/VamsiG/Music/Research_Work/Research_Code/2014_101.csv"
in_filename2 = "/Users/VamsiG/Music/Research_Work/Research_Code/2014_253.csv"
in_filename3 = "/Users/VamsiG/Music/Research_Work/FCC_Output_2016.txt"
out_filename1 = "/Users/VamsiG/Music/Research_Work/Research_Code/2016_newblock_data.csv"
out_filename2 = "/Users/VamsiG/Music/Research_Work/Research_Code/2016_newtwenty_data.csv"
out_filename3 = "/Users/VamsiG/Music/Research_Work/Research_Code/2016_newtentotwenty_data.csv"

filter_lines(in_filename, in_filename2, in_filename3, out_filename1, out_filename2, out_filename3)