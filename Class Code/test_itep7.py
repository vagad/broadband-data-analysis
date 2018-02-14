from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

def filter_lines(in_filename, in_filename2,out_filename):
    """Read records from in_filename and write records to out_filename if
    the beginning of the line (taken up to the first comma at or after
    position 11) is found in keys (which must be a set of byte strings).

    """
    proper_convert = 0
    missing_convert = 0
    fourteen_dictionary = {}
    with open(in_filename, 'r') as in_f, open(in_filename2, 'r') as in_f2, open(out_filename, 'w') as out_f:
        for line in in_f:
            vals = line.split(",")
            if(len(vals) == 3):
                fips = vals[0]
                lat = vals[1]
                lon = vals[2]
                fourteen_dictionary[fips] = (lat, lon)
        
        for line in in_f2:
            vals = line.strip().split(",")
            if(len(vals) == 3):
                fips = vals[0]
                lat = vals[1]
                lon = vals[2]

                if(not (fips in fourteen_dictionary)):    
                    missing_convert += 1
                    new_line = str(fips)+","+str(lat)+","+str(lon
                    )+"\n"
                    out_f.write(new_line)
                else:
                    proper_convert += 1

    return (proper_convert, missing_convert)

def mapTut(in_filename):

    m = Basemap(projection='mill',llcrnrlat=20,urcrnrlat=50,\
                llcrnrlon=-130,urcrnrlon=-60,resolution='c')
    m.drawcoastlines()
    m.drawcountries()
    m.drawstates()
    m.fillcontinents(color='#04BAE3',lake_color='#FFFFFF')
    m.drawmapboundary(fill_color='#FFFFFF')

    lat = []
    lon = []

    with open(in_filename, 'r') as in_f:
        for line in in_f:
            # print(line)
            vals = line.strip().split(",")
            if(len(vals) == 3):
                lat.append(float(vals[1]))
                lon.append(float(vals[2]))
    print(len(lat))
    print(len(lon))


    x,y = m(lon,lat)
    m.plot(x,y,'ro',markersize=0.05,alpha=.5)
    
    # counter = 0
    # with open(in_filename, 'r') as in_f:
    #     for line in in_f:
    #         counter += 1
    #         if(counter % 100000 == 0):
    #             print("100k processed")
    #         vals = line.split(",")
    #         if(len(vals) == 3):
    #             lat = float(vals[1])
    #             lon = float(vals[2])
    #             x,y = m(lon,lat)
    #             m.plot(x,y, 'go')
    plt.title("New Regions with At Least One Carrier Offering 25 Mbps in 2017")
    plt.show()

in_filename = "/Users/VamsiG/Music/2014_Data/FCC_Final_LatLong.csv"
in_filename1 = "/Users/VamsiG/Music/2016_Data/FCC_Final_LatLong.csv"
out_filename= "/Users/VamsiG/Music/FCC_Overlap_LatLong.csv"

counter1, new_vals1 = filter_lines(in_filename,in_filename1,out_filename)
print(counter1)
print(new_vals1)
mapTut(out_filename)