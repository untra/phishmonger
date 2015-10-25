#! /bin/bash

api_Call(){

BASE_URL='https://api.sbx.gomo.do'
KEY='btzWLwrrDsTgLBWGYLXQzbO4H8zrt9sT'
SECRET='NSHkfKh9grhJWSLroddgLIy0PGY4H5dBZSdvvmpbkw5qxgh-ORYvuKHf743BzI8P'
# ACCOUNT=""
# API='/YiiModo/api_v2/people/register'
# POST_DATA='phone=2145426078&is_modo_terms_agree=1'
DATE=`date +%s`
TIMESTAMP=`echo $((DATE*1000 - 9999))`
BODY_HASH=`echo -n $POST_DATA | openssl sha -sha256 -r | awk '{print $1;}'`
SIGNING_KEY=`echo -n $TIMESTAMP | openssl dgst -sha256 -hex -hmac 'MODO1'$SECRET -r | awk '{print $1;}'`
STRING_TO_SIGN=$TIMESTAMP'&'$API'&'$BODY_HASH
SIGNATURE=`echo -n $STRING_TO_SIGN | openssl dgst -sha256 -hex -mac HMAC -macopt "hexkey:$SIGNING_KEY" -r | awk '{print $1;}'`
curl -s -H 'X-Modo-Date:'$TIMESTAMP -H 'Authorization: MODO1 key='$KEY', sig='$SIGNATURE -d $POST_DATA $BASE_URL''$API  #output
}

api_Call
