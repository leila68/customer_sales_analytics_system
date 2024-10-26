import pandas as pd
from google.cloud import storage
from io import StringIO

# client = storage.Client()
# buckets = client.list_buckets()
#
# for bucket in buckets:
#     print(bucket.name)

client = storage.Client()

bucket_name = 'example1122334455'
file_name = 'dataset/customer_profile_dataset.csv'
bucket = client.get_bucket(bucket_name)

blob = bucket.blob(file_name)

# Download the file content as a string and read it into pandas
data = blob.download_as_text()
products_df = pd.read_csv(StringIO(data))

# Display the DataFrame
print(products_df.head())