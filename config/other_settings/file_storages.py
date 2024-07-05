from config.env import env

from google.oauth2 import service_account

GS_CREDENTIALS = service_account.Credentials.from_service_account_file(env('GS_CREDENTIALS_PATH'))


STORAGES = {
    "default": {
        "BACKEND": "storages.backends.gcloud.GoogleCloudStorage",
        "OPTIONS": {
            'bucket_name': env('GS_MEDIA_BUCKET_NAME'),
            'project_id': env('GS_PROJECT_ID'),
            'file_overwrite': False,
            'credentials': GS_CREDENTIALS,
        },
    },
    "staticfiles": {
        "BACKEND": "storages.backends.gcloud.GoogleCloudStorage",
        "OPTIONS":{
            'bucket_name': env('GS_STATIC_BUCKET_NAME'),
            'project_id': env('GS_PROJECT_ID'),
            'credentials': GS_CREDENTIALS,
        }
    }
}