from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client(project="usavm-334506")

# Construct a reference to the table
table_ref = client.get_table("usavm-334506.rtlm.channel_transcripts")

# Get the table schema
schema = table_ref.schema

# Print field names and their types
print("Table fields:")
for field in schema:
    print(f"{field.name}: {field.field_type}")


# Query the table
query_job = client.query(f"SELECT * FROM `{table_ref}` WHERE file_path = '2024-12-20_14-42-54.mp3'") # Replace with your query

# Iterate over the results and print them
for row in query_job:
    print(row.transcript_text)
