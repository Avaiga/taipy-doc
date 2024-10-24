from taipy import Config

s3_object_cfg = Config.configure_s3_object_data_node(
    id="my_s3_object",
    aws_access_key="YOUR AWS ACCESS KEY",
    aws_secret_access_key="YOUR AWS SECRET ACCESS KEY",
    aws_s3_bucket_name="YOUR AWS BUCKET NAME",
    aws_s3_object_key="taipy_object",
    aws_s3_client_parameters={
        "endpoint_url": "https://s3.custom-endpoint.com"
    },
    aws_s3_get_object_parameters={
        "Range": "bytes=0-1048576"
    },
    aws_s3_put_object_parameters={
        "CacheControl": "max-age=86400"
    }
)
