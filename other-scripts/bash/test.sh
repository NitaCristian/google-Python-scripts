> file.txt
filenames=$(grep .py filenames.txt)
for i in $filenames
do
    if test -e "$i" 
    then
        echo $i >> file.txt
    else
        echo "$i" 
    fi
done