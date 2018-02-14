from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

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


    
    plt.title("Regions with At Least One Carrier Offering 25 Mbps in 2014")
    plt.show()


in_filename = "/Users/VamsiG/Music/2014_Data/FCC_Final_LatLong.csv"
mapTut(in_filename)