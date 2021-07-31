from bokeh.models.widgets import Div
from google.oauth2.credentials import Credentials
from google_auth_oauthlib import flow, helpers as oauthlib_helpers
from oauthlib.oauth2.rfc6749.errors import InvalidGrantError
import streamlit
from typing import Optional


def _render_sign_in(st: streamlit, authorization_url: str) -> None:
    if st.button('Sign in with Google'):
        js = "window.location.href = '{}'".format(authorization_url)
        html = '<img src onerror="{}">'.format(js)
        div = Div(text=html)
        st.bokeh_chart(div)
    st.stop()


def render_sign_in_or_credential(st: streamlit) -> Optional[Credentials]:
    client_config = st.secrets["client_config"]
    appflow = flow.InstalledAppFlow.from_client_config(
        client_config,
        scopes=[
            "https://www.googleapis.com/auth/bigquery.readonly",
            # MARK: https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/query
            "https://www.googleapis.com/auth/devstorage.read_only",
        ],
        redirect_uri=client_config["web"]["redirect_uris"][0]
    )
    if "oauth2session" in st.session_state:
        return oauthlib_helpers.credentials_from_session(
            st.session_state.oauth2session, client_config
        )
    else:
        authorization_url, _ = appflow.authorization_url()
        try:
            code = st.experimental_get_query_params()['code'][0]
        except KeyError:
            _render_sign_in(st, authorization_url)
        else:
            try:
                appflow.fetch_token(code=code)
            except InvalidGrantError:
                _render_sign_in(st, authorization_url)
        st.session_state.oauth2session = appflow.oauth2session
        return appflow.credentials
