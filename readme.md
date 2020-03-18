# Make and upload code from cmd line
* Requires pip install aws-cli
make && aws lambda update-function-code \
    --function-name  bay_volume_test \
    --zip-file fileb://lambda.zip
