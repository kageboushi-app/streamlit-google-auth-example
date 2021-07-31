from google.cloud import bigquery
import streamlit as st

from streamlit_google_auth_example.utils import MultiPage
from streamlit_google_auth_example.auth import render_sign_in_or_credential


def page1():
    st.title("Shakespeare")

    credentials = render_sign_in_or_credential(st)
    client = bigquery.Client(credentials=credentials)

    limit = st.number_input('Limit', 1, format="%i")

    query = "SELECT word FROM `bigquery-public-data.samples.shakespeare` LIMIT {}".format(limit)
    query_job = client.query(query)
    rows_raw = query_job.result()
    rows = [dict(row) for row in rows_raw]

    st.write("Some wise words from Shakespeare:")
    for row in rows:
        st.write("✍️ " + row['word'])


def page2():
    st.title("BigQuery Datasets")

    credentials = render_sign_in_or_credential(st)
    client = bigquery.Client(credentials=credentials)

    st.write("All datasets:")
    for dt in client.list_datasets():
        st.write("✍️ " + dt.dataset_id)


if __name__ == "__main__":
    pages = MultiPage(st)
    pages.append(("shakespeare", page1))
    pages.append(("datasets", page2))
    pages.run()
