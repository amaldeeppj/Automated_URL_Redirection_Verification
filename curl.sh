#!/bin/bash

#echo $1

echo "Source URL, Redirect URL, Desired Path, Status Code, Redirection Status" > $2

while read url ;
do
source=$(echo $url | awk '{print $1}') ;
dest=$(echo $url | awk '{print $2}' | sed 's:/*$::') ;
#echo $source ;

#curl status code and redirected path
output=$(curl -I  -s  -o /dev/null -w "%{http_code} %{redirect_url} \n" $source) ;
status_code=$(echo "$output"|awk '{print $1}') ;
redirect_url=$(echo "$output"|awk '{print $2}' | sed 's:/*$::') ;
status="Not Working"
if [ "$dest" == "$redirect_url" ]; 
then
status="Working";
fi;
echo "$source, $redirect_url, $dest, $status_code, $status" >> $2 ;
echo "=========" ;
done < $1
