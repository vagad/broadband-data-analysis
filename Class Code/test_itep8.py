import re

def filter_lines(in_filename, in_filename2,out_filename):
    """Read records from in_filename and write records to out_filename if
    the beginning of the line (taken up to the first comma at or after
    position 11) is found in keys (which must be a set of byte strings).

    """
    proper_convert = 0
    missing_convert = 0
    missing_us_convert = 0
    repeat = 0
    counter = 0
    counter2 = 0
    county_dictionary = {}
    county_set = set()
    with open(in_filename, 'r', encoding='latin-1') as in_f:
        for line in in_f:
            vals1 = re.sub(r'"[^"]*"', lambda m: m.group(0).replace(',', ''), line)
            vals = vals1.split(",")
            fips = vals[0].strip()
            urb_pop = vals[298].strip()
            mid_pop = vals[299].strip()
            rur_pop = vals[300].strip()
            pop_5 = vals[308].strip()
            pop_517 = vals[311].strip()
            pop_1824 = vals[314].strip()
            pop_2544 = vals[317].strip()
            pop_4564 = vals[320].strip()
            pop_65 = vals[323].strip()
            pop_noths = vals[435].strip()
            pop_college = vals[437].strip()
            rec_home = vals[548].strip()
            med_inc = vals[245].strip()
            med_home = vals[280].strip()
            pct_move = vals[516].strip()
        
            county_dictionary[fips] = (urb_pop, mid_pop, rur_pop, pop_5, pop_517, pop_1824, pop_2544,
                pop_4564, pop_65, pop_noths, pop_college, rec_home, med_inc, med_home, pct_move)
            if(counter <= 1):
                print(county_dictionary[fips])
                print(vals1)
            counter += 1
    
    with open(in_filename2, 'r') as in_f2, open(out_filename, 'w') as out_f:
        for line in in_f2:
            vals = line.strip().split(",")
            fips = vals[0][:11]
            if((fips in county_dictionary) and (fips not in county_set)): 
                county_set.add(fips)  
                urb_pop, mid_pop, rur_pop, pop_5, pop_517, pop_1824, pop_2544,pop_4564, pop_65, pop_noths, pop_college, rec_home, med_inc, med_home, pct_move = county_dictionary[fips] 
                
                new_line = str(fips)+","+str(urb_pop)+","+str(mid_pop)+","+str(rur_pop)+","+str(pop_5)+","+str(pop_517)+","+str(pop_1824)+","+str(pop_2544)+","+str(pop_4564)+","+str(pop_65)+","+str(pop_noths)+","+str(pop_college)+","+str(rec_home)+","+str(med_inc)+","+str(med_home)+","+str(pct_move)+"\n"
                out_f.write(new_line)
                proper_convert += 1
            else:
                if (fips not in county_set):
                    repeat += 1
                else:
                    if(int(fips[:2]) <= 56):
                        missing_us_convert += 1
                    missing_convert += 1    # print(vals)

            counter2 += 1
            
        


    return (proper_convert, missing_convert, missing_us_convert, repeat)

in_filename = "/Users/VamsiG/Music/pdb2016trv8_us.csv"
in_filename1 = "/Users/VamsiG/Music/FCC_Overlap_CompleteFips.csv"
out_filename1 = "/Users/VamsiG/Music/FCC_Overlap_CensusTractFips.csv"

counter1, new_vals1, new_vals2, repeat = filter_lines(in_filename,in_filename1,out_filename1)
print(counter1)
print(new_vals1)
print(new_vals2)
print(repeat)