import os

POSTGRES_USER = os.environ.get('POSTGRES_USER', '')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', '')
POSTGRES_HOST = os.environ.get('POSTGRES_HOST', '')
POSTGRES_PORT = os.environ.get('POSTGRES_PORT', 0)
POSTGRES_DB = os.environ.get('POSTGRES_DB', '')

ENGINE_STRING = 'postgresql+psycopg2://{}:{}@{}:{}/{}'.format(
    POSTGRES_USER,
    POSTGRES_PASSWORD,
    POSTGRES_HOST,
    POSTGRES_PORT,
    POSTGRES_DB
)

JOB_POSTS_TABLE = 'job_post'
