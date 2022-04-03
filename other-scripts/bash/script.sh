line="--------------------"
echo "Starting at: $(date)"; echo $line

if grep "127.0.0.1" in /etc/hosts; then
    echo "Everything ok"
else 
    echo "ERROR"
fi