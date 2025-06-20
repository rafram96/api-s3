import base64
import boto3
import json

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        bucket = body['bucket']
        folder = body['folder']
        filename = body['filename']
        base64_str = body['base64_file']

        s3_path = f"{folder}/{filename}"

        s3 = boto3.resource('s3')
        s3.Object(bucket, s3_path).put(Body=base64.b64decode(base64_str))

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Archivo subido con éxito",
                "path": f"s3://{bucket}/{s3_path}"
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
