from collections import defaultdict

def filter_lines(in_filename, out_filename, out_filename2 , out_filename3, out_filename4):
    """Read records from in_filename and write records to out_filename if
    the beginning of the line (taken up to the first comma at or after
    position 11) is found in keys (which must be a set of byte strings).

    """
    counter = 0
    
    state_dict = defaultdict(int)
    tech_dict = defaultdict(int)
    hoco_dict = defaultdict(int)
    provider_dict = defaultdict(int)

    with open(in_filename, 'r') as in_f, open(out_filename, 'w') as out_f, open(out_filename2, 'w') as out_f2, open(out_filename3, 'w') as out_f3, open(out_filename4, 'w') as out_f4:
        for line in in_f:
            vals = line.split(",")
            state = vals[4]
            tech = vals[3]
            hoco = vals[5]
            provider = vals[6]

            state_dict[state] += 1
            tech_dict[tech] += 1
            hoco_dict[hoco] += 1
            provider_dict[provider] += 1
            counter += 1

        for k,v in state_dict.items():
            out_f.write("{}: {} \n".format(k.rstrip(),v))
        for k,v in tech_dict.items():
            out_f2.write("{}: {} \n".format(k.rstrip(),v))
        for k,v in hoco_dict.items():
            out_f3.write("{}: {} \n".format(k.rstrip(),v))
        for k,v in provider_dict.items():
            out_f4.write("{}: {} \n".format(k.rstrip(),v))

        
    print(counter)
    print(len(state_dict))
    print(len(tech_dict))
    print(len(hoco_dict))
    print(len(provider_dict))
    
    return 


in_filename = "/Users/VamsiG/Music/Research_Work/Research_Code/2016_newblock_data.csv"
in_filename2 = "/Users/VamsiG/Music/Research_Work/Research_Code/2016_newtwenty_data.csv"
in_filename3 = "/Users/VamsiG/Music/Research_Work/Research_Code/2016_newtentotwenty_data.csv"

out_filename = "/Users/VamsiG/Music/Research_Work/Research_Code/histograms_new/state.txt"
out_filename2 = "/Users/VamsiG/Music/Research_Work/Research_Code/histograms_new/tech_code.txt"
out_filename3 = "/Users/VamsiG/Music/Research_Work/Research_Code/histograms_new/hoco_name.txt"
out_filename4 = "/Users/VamsiG/Music/Research_Work/Research_Code/histograms_new/provider_name.txt"

aout_filename = "/Users/VamsiG/Music/Research_Work/Research_Code/histograms_new20/state.txt"
aout_filename2 = "/Users/VamsiG/Music/Research_Work/Research_Code/histograms_new20/tech_code.txt"
aout_filename3 = "/Users/VamsiG/Music/Research_Work/Research_Code/histograms_new20/hoco_name.txt"
aout_filename4 = "/Users/VamsiG/Music/Research_Work/Research_Code/histograms_new20/provider_name.txt"

bout_filename = "/Users/VamsiG/Music/Research_Work/Research_Code/histograms_converted/state.txt"
bout_filename2 = "/Users/VamsiG/Music/Research_Work/Research_Code/histograms_converted/tech_code.txt"
bout_filename3 = "/Users/VamsiG/Music/Research_Work/Research_Code/histograms_converted/hoco_name.txt"
bout_filename4 = "/Users/VamsiG/Music/Research_Work/Research_Code/histograms_converted/provider_name.txt"

filter_lines(in_filename, out_filename, out_filename2, out_filename3, out_filename4)
filter_lines(in_filename2, aout_filename, aout_filename2, aout_filename3, aout_filename4)
filter_lines(in_filename3, bout_filename, bout_filename2, bout_filename3, bout_filename4)


