# Streamlit Google Auth Example

```bash
cat << EOT >> .streamlit/secrets_bk.toml
[client_config.web]
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
auth_uri = "https://accounts.google.com/o/oauth2/auth"
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"
project_id = "YOUR_PROJECT_ID"
redirect_uris = ["http://localhost:8501"]
token_uri = "https://oauth2.googleapis.com/token"
EOT
```

```console
poetry install
poetry run streamlit run main.py
```
