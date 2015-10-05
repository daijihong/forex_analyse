echo '5 minutes'
python cal_time_serial.py ../$1.txt 5 > ../data/$1_5.txt
echo '15 minutes'
python cal_time_serial.py ../$1.txt 15 > ../data/$1_15.txt
echo '30 minutes'
python cal_time_serial.py ../$1.txt 30 > ../data/$1_30.txt
echo '1 hours'
python cal_time_serial.py ../$1.txt 60 > ../data/$1_60.txt
echo '4 hours'
python cal_time_serial.py ../$1.txt 240 > ../data/$1_240.txt
echo '1 day'
python cal_time_serial.py ../$1.txt 1440 > ../data/$1_1440.txt
