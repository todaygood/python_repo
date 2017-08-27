
for i in $(ls *.py); do
	b=$(echo $i | awk -F. '{print $1}')
	mv $i  $b_mh.py; 
done
