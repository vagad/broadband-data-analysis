# broadband-data-analysis
Analysis of trends in broadband data based on FCC 477 data alongside FCC MBA data. We used the Census' PDB for social statistics.

To run code or even generally connect to the MySQL instance, you have to start off by granting access to yourself. Here are the steps to do so.:
1) Go to the Google Compute Instance and find the SQL page on the dropdown in the top left corner
2) Click on the authorization tab in the SQL page corresponding to our project.
3) Add your name and IP address to the authorization pane and MAKE SURE TO CLICK SAVE.
4) Now, you can try to see if this works. Firstly, make sure you have the mysql client for your terminal. To connect, use the following command: mysql --host=[INSTANCE_IP] --user=root --password 
5) The instance IP can be found in an e-mail I sent earlier and the password that you will be asked to enter after can also be found there.

Variables in 477 data: 
Lrn = logical record number
Blockcode = fips code
ProviderId
Frn = code pertaining to each company
ProviderName
DbaName
HoldingName
HoldingNum
FccHoldingName
State = state code
TechCode = FCC tech code pertaining to broadband offering
UpSpeed = upload speed
DownSpeed = download speed
477year = year the data is for
