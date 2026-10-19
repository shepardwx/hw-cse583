mkdir pronto
cd pronto
touch README.txt
nano README.txt
mkdir data
curl 'https://s3.amazonaws.com/pronto-data/open_data_year_one.zip' -o data/open_data_year_one.zip
cd data
unzip open_data_year_one.zip
head 2015_trip_data.csv

