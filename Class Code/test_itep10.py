import re
from statistics import mean
from statistics import median_grouped

def filter_lines(in_filename, in_filename2,out_filename):
    """Read records from in_filename and write records to out_filename if
    the beginning of the line (taken up to the first comma at or after
    position 11) is found in keys (which must be a set of byte strings).

    """
    proper_convert = 0
    missing_convert = 0
    missing_us_convert = 0
    counter = 0
    counter2 = 0
    county_dictionary = {}
    county_set = set()
    repeat = 0
    
    with open(in_filename, 'r', encoding='latin-1') as in_f:
        for line in in_f:
            vals1 = re.sub(r'"[^"]*"', lambda m: m.group(0).replace(',', ''), line)
            vals = vals1.split(",")
            fips = vals[0].strip()
            urb_pop = vals[186].strip()
            mid_pop = vals[187].strip()
            rur_pop = vals[188].strip()
            pop_5 = vals[196].strip()
            pop_517 = vals[199].strip()
            pop_1824 = vals[202].strip()
            pop_2544 = vals[205].strip()
            pop_4564 = vals[208].strip()
            pop_65 = vals[211].strip()
            pop_noths = vals[243].strip()
            pop_college = vals[245].strip()
            rec_home = vals[330].strip()
            med_inc = vals[129].strip()
            med_home = vals[166].strip()
            pct_move = vals[298].strip()
        
            county_dictionary[fips] = (urb_pop, mid_pop, rur_pop, pop_5, pop_517, pop_1824, pop_2544,
                pop_4564, pop_65, pop_noths, pop_college, rec_home, med_inc, med_home, pct_move)
            if(counter <= 1):
                print(county_dictionary[fips])
            counter += 1
    
    with open(in_filename2, 'r') as in_f2, open(out_filename, 'w') as out_f:
        for line in in_f2:
            vals = line.strip().split(",")
            fips = str(vals[0][:12])
            if((fips in county_dictionary) and (fips not in county_set)): 
                county_set.add(fips)  
                urb_pop, mid_pop, rur_pop, pop_5, pop_517, pop_1824, pop_2544,pop_4564, pop_65, pop_noths, pop_college, rec_home, med_inc, med_home, pct_move = county_dictionary[fips] 
                
                new_line = str(fips)+","+str(urb_pop)+","+str(mid_pop)+","+str(rur_pop)+","+str(pop_5)+","+str(pop_517)+","+str(pop_1824)+","+str(pop_2544)+","+str(pop_4564)+","+str(pop_65)+","+str(pop_noths)+","+str(pop_college)+","+str(rec_home)+","+str(med_inc)+","+str(med_home)+","+str(pct_move)+"\n"
                
                out_f.write(new_line)
                proper_convert += 1
            else:
                if (fips not in county_set):
                    repeat +=1
                else:
                    if(int(fips[:2]) <= 56):
                        missing_us_convert += 1
                        print(fips)
                    missing_convert += 1    # print(vals)

    return (proper_convert, missing_convert, missing_us_convert, repeat)

def get_stats(in_filename):
    """Read records from in_filename and write records to out_filename if
    the beginning of the line (taken up to the first comma at or after
    position 11) is found in keys (which must be a set of byte strings).

    """
    counter = 0
    new_vals = 0

    pop_noths_list = []
    pop_college_list = []
    rec_home_list = []
    med_inc_list = []
    med_home_list = []
    pct_move_list = []
    
    with open(in_filename, 'r') as in_f:
        for line in in_f:
            counter += 1
            vals = line.split(",")
            # urb_pop = float(vals[1].strip())
            # mid_pop = vals[2].strip()
            # rur_pop = vals[3].strip()
            # pop_5 = vals[4].strip()
            # pop_517 = vals[5].strip()
            # pop_1824 = vals[6].strip()
            # pop_2544 = vals[7].strip()
            # pop_4564 = vals[8].strip()
            # pop_65 = vals[9].strip()

            if(vals[1].strip() != "" and float(vals[1].strip()) <= 50.0):
                counter += 1
                if(vals[10].strip() != ""):
                    pop_noths = float(vals[10].strip())
                    pop_noths_list.append(pop_noths)
                if(vals[11].strip() != ""):
                    pop_college = float(vals[11].strip())
                    pop_college_list.append(pop_college)
                if(vals[12].strip() != ""):
                    rec_home = float(vals[12].strip())
                    rec_home_list.append(rec_home)
                if(vals[13].strip().replace('"', '').replace('$', '') != ""):
                    med_inc = float(vals[13].strip().replace('"', '').replace('$', ''))
                    med_inc_list.append(med_inc)
                if(vals[14].strip().replace('"', '').replace('$', '') != ""):
                    med_home = float(vals[14].strip().replace('"', '').replace('$', ''))
                    med_home_list.append(med_home)
                if(vals[15].strip() != ""):
                    pct_move = float(vals[15].strip())
                    pct_move_list.append(pct_move)
            else:
                if(vals[1].strip() != "" and float(vals[1].strip()) > 50.0):
                    new_vals += 1

            
            if (counter % 10000 == 0):
                print("Another 10k done")
    
    mean_noths = mean(pop_noths_list)
    med_noths = median_grouped(pop_noths_list)
    print(mean_noths)
    print(med_noths)

    mean_college = mean(pop_college_list)
    med_college = median_grouped(pop_college_list)
    print(mean_college)
    print(med_college)

    mean_rechome = mean(rec_home_list)
    med_rechome = median_grouped(rec_home_list)
    print(mean_rechome)
    print(med_rechome)

    mean_medinc = mean(med_inc_list)
    med_medinc = median_grouped(med_inc_list)
    print(mean_medinc)
    print(med_medinc)

    mean_medhome = mean(med_home_list)
    med_medhome = median_grouped(med_home_list)
    print(mean_medhome)
    print(med_medhome)

    mean_pctmove = mean(pct_move_list)
    med_pctmove = median_grouped(pct_move_list)
    print(mean_pctmove)
    print(med_pctmove)


    return (counter, new_vals)

in_filename = "/Users/VamsiG/Music/pdb2016bgv8_us.csv"
in_filename1 = "/Users/VamsiG/Music/FCC_Overlap_CompleteFips.csv"
out_filename1 = "/Users/VamsiG/Music/FCC_Overlap_CensusBlockGroup.csv"

# counter1, new_vals1, new_vals2, repeat = filter_lines(in_filename,in_filename1,out_filename1)
mean, median = get_stats(out_filename1)
print(mean)
print(median)
# print(counter1)
# print(new_vals1)
# print(new_vals2)
# print(repeat)
