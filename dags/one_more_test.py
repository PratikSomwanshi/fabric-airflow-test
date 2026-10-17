
from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator


def say_hello():
    print("Hello from GitHub deployed to Microsoft Fabric Airflow!)


with DAG(
    dag_id="triple_hello_fabric",
    description="Test GitHub Git Sync with Fabric Airflow",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["github", "fabric", "test"],
) as dag:

    hello_task = PythonOperator(
        task_id="say_hello",
        python_callable=say_hello,
    )
