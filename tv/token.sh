CURRENT_DIR=$(cd $(dirname $0); pwd)
token=$(cat $CURRENT_DIR/token.txt)
ntoken=$(curl https://api.aliyundrive.com/token/refresh -X POST -H "User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36" -H "Rererer:https://www.aliyundrive.com/" -H "Content-Type:application/json" -d '{"refresh_token":"'$token'"}' | sed 's/,/\n/g' | grep refresh_token | cut -d \: -f2 | sed 's/"//g')
if [ ! -n "$ntoken" ]; then
ntoken=$(curl https://auth.aliyundrive.com/v2/account/token -X POST -H "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36" -H "Rererer:https://www.aliyundrive.com/" -H "Content-Type:application/json" -d '{"refresh_token":"'$token'", "grant_type": "refresh_token"}'| sed 's/,/\n/g' | grep refresh_token | cut -d \: -f2 | sed 's/"//g')
fi
echo  -n ${ntoken} > $CURRENT_DIR/token.txt
