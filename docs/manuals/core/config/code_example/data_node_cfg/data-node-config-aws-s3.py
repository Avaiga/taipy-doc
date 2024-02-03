import taipy as tp
import boto3
from taipy import Config, Core
from taipy.config import  Scope

# Configure S3 Object
s3_object_cfg = Config.configure_s3_object_data_node(
    id="my_s3_object", scope=Scope.GLOBAL,
    aws_access_key="YOUR AWS ACCESS KEY",  # Can be passed as env variable as well
    aws_secret_access_key="YOUR AWS SECRET ACCESS KEY", # Can be passed as env variable as well
    aws_s3_bucket_name="YOUR AWS BUCKET NAME", #Must be Already existing bucket
    aws_s3_object_key="taipy_object",
    aws_s3_object_parameters = {'CacheControl': 'max-age=86400'})

# Instantiate to S3 Object datanode
my_s3_global_object = tp.create_global_data_node(s3_object_cfg)
my_s3_global_object.write("Welcome to Taipy")  # Write welcome message to S3 object
s3_data= my_s3_global_object.read()  #Read data from S3 object 
print("S3 message : ", s3_data) # Print S3 data on console

if __name__ == "__main__":
    Core().run()
