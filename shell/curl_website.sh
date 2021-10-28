while true; do
# for _ in {1..2}; do 
    cip="$(($RANDOM % 223 + 1)).$(($RANDOM % 225)).$(($RANDOM % 225)).1"
    webserver="https://wwwqas.dfzk.com/"
    args="
        -H "Cache-Control:no-cache" \
        -H "X-Forwarded-For:${cip}" \
        -H "X-Real-IP:${cip}" \
        -H "CLIENT-IP:${cip}" \
        -vI 
    "
    # curl -H "X-Forwarded-For:$(($RANDOM % 223 + 1)).$(($RANDOM % 225)).$(($RANDOM % 225)).1" -H "" -vI https://wwwqas.dfzk.com/
    # curl -H "Cache-Control:no-cache" -H "X-Forwarded-For:${cip}" -H "X-Real-IP:${cip}" -H "CLIENT-IP:${cip}" -vI ${webserver}
    curl ${args} ${webserver}
    sleep 0.5
done
