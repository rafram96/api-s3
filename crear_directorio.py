import boto3
import json

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        bucket = body['bucket']
        folder = body['folder']

        s3 = boto3.client('s3')
        s3.put_object(Bucket=bucket, Key=f"{folder}/")

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Directorio creado correctamente",
                "path": f"s3://{bucket}/{folder}/"
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
