from sqlalchemy import create_engine
from sqlalchemy import MetaData, Column, Table, ForeignKey
from sqlalchemy import Integer, String
import MySQLdb
import re

def filter_lines(in_filename, out_filename):
    """Read records from in_filename and write records to out_filename if
    the beginning of the line (taken up to the first comma at or after
    position 11) is found in keys (which must be a set of byte strings).

    """
    counter = 0
    new_vals = 0
    myDB = MySQLdb.connect(host="",user="",passwd="",db="research_data")

    with open(in_filename, 'r', encoding='latin-1') as in_f, open(out_filename, 'w') as out_f:
        for line in in_f:
            sentence = re.sub(r'(?!(([^"]*"){2})*[^"]*$),', '', line)
            sentence = sentence.replace('"', '')
            counter += 1
            vals = sentence.split(",")
            if (counter % 100000 == 0):
                print("Another 100k done")
            if (counter % 1000000 == 0):
                print("Another milli done")
            if (counter>1):
                lrn = vals[0]
                provider_id = vals[1]
                frn = vals[2]
                provider_name = vals[3]
                dba_name = vals[4]
                hoco_name = vals[5]
                hoco_num = vals[6]
                hoco_final = vals[7]
                tech_code = vals[-7]
                fips = vals[-8]
                state = vals[-9]
                upload = vals[-4]
                download = vals[-5]
                final_line = "INSERT INTO table_name (Lrn,Blockcode,ProviderId,Frn,ProviderName,DbaName,HoldingName,HoldingNum,FccHoldingName,State,TechCode,UpSpeed,DownSpeed) VALUES ({},{},{},{},{},{},{},{},{},{},{},{},{}); \n".format(lrn,fips,provider_id,frn,provider_name,dba_name,hoco_name,hoco_num,hoco_final,state,tech_code,upload,download)
                out_f.write(final_line)
                # print(final_line)
                new_vals += 1

                # print(final_line)
                cHandler = myDB.cursor()
                cHandler.execute("INSERT INTO Final477Data (Lrn,Blockcode,ProviderId,Frn,ProviderName,DbaName,HoldingName,HoldingNum,FccHoldingName,State,TechCode,UpSpeed,DownSpeed) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (lrn,fips,provider_id,frn,provider_name,dba_name,hoco_name,hoco_num,hoco_final,state,tech_code,upload,download))
                # cHandler.execute("INSERT INTO 477_data (fips_code) VALUES ('%s')"%(fips))
                results = cHandler.fetchall()
                for items in results:
                    print(items[0])
                cHandler.close()
                myDB.commit()

                # cHandler = myDB.cursor()
                # cHandler.execute("INSERT INTO Final477Data (Lrn,Blockcode,ProviderId,Frn,ProviderName,DbaName,HoldingName,HoldingNum,FccHoldingName,State,TechCode,UpSpeed,DownSpeed) VALUES ({},{},{},{},{},{},{},{},{},{},{},{},{})".format(lrn,fips,provider_id,frn,provider_name,dba_name,hoco_name,hoco_num,hoco_final,state,tech_code,upload,download))
                # results = cHandler.fetchall()
                # for items in results:
                #     print(items[0])
                # cHandler.close()
                # if (counter<20):
                #     print(final_line)
                #     cHandler = myDB.cursor()
                #     cHandler.execute("INSERT INTO Final477Data (Lrn,Blockcode,ProviderId,Frn,ProviderName,DbaName,HoldingName,HoldingNum,FccHoldingName,State,TechCode,UpSpeed,DownSpeed) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (lrn,fips,provider_id,frn,provider_name,dba_name,hoco_name,hoco_num,hoco_final,state,tech_code,upload,download))
                #     # cHandler.execute("INSERT INTO 477_data (fips_code) VALUES ('%s')"%(fips))
                #     results = cHandler.fetchall()
                #     for items in results:
                #         print(items[0])
                #     cHandler.close()
                #     myDB.commit()

    myDB.close()

    return (counter, new_vals)




in_filename1 = "/Users/VamsiG/Music/Research_Work/fbd_us_without_satellite_dec2016_v1.csv"
out_filename1 = "/Users/VamsiG/Music/Research_Work/FCC_Output_2016.csv"

# in_filename2 = "/Users/VamsiG/fbd_us_with_satellite_dec2014_v1.csv"
# out_filename2 = "/Users/VamsiG/Music/2014_Data/FCC_Output.csv"

counter1, new_vals1 = filter_lines(in_filename1,out_filename1)
# counter2, new_vals2 = filter_lines(in_filename2,out_filename2)

print(counter1)
print(new_vals1)
# print(counter2)
# print(new_vals2)

