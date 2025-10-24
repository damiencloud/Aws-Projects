import json
import boto3

def lambda_handler(event, context):
    client = boto3.client("rekognition")
    s3 = boto3.client("s3")

    fileObj = s3.get_object(Bucket="rekognitionbucket47", Key="360_F_546016914_qE7KlgNMJCzFSueLhBZ1Qo7NbmIVfu9e.jpg")
    file_content = fileObj["Body"].read()

    response = client.detect_labels(
        Image={"S3Object": {"Bucket": "rekognitionbucket47", "Name": "360_F_546016914_qE7KlgNMJCzFSueLhBZ1Qo7NbmIVfu9e.jpg"}},
        MaxLabels=3,
        MinConfidence=70
    )

    print(response)
    return {
        'statusCode': 200,
        'body': json.dumps("Hello from Lambda!")
    }
