#!/bin/sh

rm xiaobiao
touch xiaobiao

combo="if(NR!=1){print $2}"
stand="if(NR!=1){print $3}"
for(( i=1; i<=11; i++ ));do
    for j in 100-0.5L 100-1 220-0.5L 220-1 ; do
        filename=校$i—$j.txt
	echo $filename: >> xiaobiao
	echo "    电流:" >> xiaobiao
	echo -n "        combo值:" >> xiaobiao
	# echo $filename
	# combo_i=`cat $filename | grep "^COMBO_Irms" | awk -F' ' '{print $2}'`
	# cat $filename | grep "^COMBO_Irms" | awk -F' ' '{if(NR!M=1){print $2}}'
	combo_i=`cat $filename | grep "^COMBO_Irms" | awk -F' ' '{if(NR!=1){print $2}}'`
	echo -n $combo_i >> X
	echo $combo_i >> xiaobiao
	echo -n "        标准表值:" >> xiaobiao
	stand_i=`cat $filename | grep "^Irms" | awk -F ' ' '{if(NR!=1){print $3}}'`
	echo -n $stand_i >> Y
	echo $stand_i >> xiaobiao
	echo -n "        最小二乘法结果:" >> xiaobiao
	i_result=`python lsqe.py X Y`
	echo $i_result > temp
	cat temp | awk -F' ' '{print $3}' >> result_k_i
	cat temp | awk -F' ' '{print $7}' >> result_b_i
	echo `python lsqe.py X Y` >> xiaobiao
	rm X; rm Y

	echo "    功率:" >> xiaobiao
	echo -n "        combo值:" >> xiaobiao
	combo_p=`cat $filename | grep "^COMBO_Prms" | awk -F' ' '{if(NR!=1){print $2}}'`
	echo -n $combo_p >> X
	echo $combo_p >> xiaobiao
	echo -n "        标准表值:" >> xiaobiao
	stand_p=`cat $filename | grep "^PowerP" | awk -F' ' '{if(NR!=1){print $3}}'`
	echo -n $stand_p >> Y
	echo $stand_p >> xiaobiao
	echo -n "        最小二乘法结果:" >> xiaobiao
	i_result=`python lsqe.py X Y`
	echo $i_result > temp
	cat temp | awk -F' ' '{print $3}' >> result_k_p
	cat temp | awk -F' ' '{print $7}' >> result_b_p
	echo `python lsqe.py X Y` >> xiaobiao
	rm X; rm Y
	
	combo_u=`cat $filename | grep "^COMBO_Urms" | awk -F' ' '{if(NR!=1){print $2}}'`
	echo -n $combo_u >> uX
	echo -n " " >> uX
	stand_u=`cat $filename | grep "^Urms" | awk -F' ' '{if(NR!=1){print $3}}'`
	echo -n $stand_u >> uY
	echo -n " " >> uY
    done;
    echo "表$i电压" >> xiaobiao
    echo -n "    combo值:" >> xiaobiao
    echo `cat uX` >> xiaobiao
    echo -n "    标准表值:" >> xiaobiao
    echo `cat uY` >> xiaobiao
    echo -n "    最小二乘法结果:" >> xiaobiao
    i_result=`python lsqe.py uX uY`
    echo $i_result > temp
    cat temp | awk -F' ' '{print $3}' >> result_k_u
    cat temp | awk -F' ' '{print $7}' >> result_b_u

    echo `python lsqe.py uX uY` >> xiaobiao
    rm uX; rm uY
    echo "======================================================================" >> xiaobiao
    echo "======================================================================" >> xiaobiao
    echo "======================================================================" >> xiaobiao
    echo "======================================================================" >> xiaobiao
done;


echo "最终的中位数:" >> xiaobiao
echo -n "    电流的K值的中位数:" >> xiaobiao
echo `python median.py result_k_i` >> xiaobiao
echo -n "    电流的B值的中位数:" >> xiaobiao
echo `python median.py result_b_i` >> xiaobiao
echo -n "    功率的K值的中位数:" >> xiaobiao
echo `python median.py result_k_p` >> xiaobiao
echo -n "    功率的B值的中位数:" >> xiaobiao
echo `python median.py result_b_p` >> xiaobiao
echo -n "    电压的K值的中位数:" >> xiaobiao
echo `python median.py result_k_u` >> xiaobiao
echo -n "    电压的B值的中位数:" >> xiaobiao
echo `python median.py result_b_u` >> xiaobiao

rm result_k_i
rm result_b_i
rm result_k_p
rm result_b_p
rm result_k_u
rm result_b_u
