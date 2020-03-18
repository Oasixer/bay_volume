COMMAND=/fjord

# [[ $0 == *bay ]] && COMMAND=/bay
# [[ $0 == *todo ]] && COMMAND=/todo
# [[ $0 == *agenda ]] && COMMAND=/agenda
# [[ $COMMAND == x ]] && exit 1

DOMAIN=waterloorocketry
USER=1234
USER_NAME=kaelan
ARGS=$1

DATA="-d team_domain=$DOMAIN&user_name=$USER_NAME&user_id=$USER&command=$COMMAND&text=$ARGS"

# debug
echo $DATA
# curl -sX POST -H 'Content-Type: application/x-www-form-urlencoded' https://0ax3yn32di.execute-api.us-east-1.amazonaws.com/test/test $DATA \
    # | python -c "import json;print(json.loads(input()))"

#curl -sX POST -H 'Content-Type: application/x-www-form-urlencoded' https://a31ke233ba.execute-api.us-east-1.amazonaws.com/bay_resource_post $DATA
curl -sX POST -H 'Content-Type: application/x-www-form-urlencoded' https://j4oiwbr2vg.execute-api.us-east-1.amazonaws.com/prod_stage/test4 $DATA 

#\
    #| python -c "import json; print(json.loads(input()))"
