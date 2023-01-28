from airflow import DAG
from airflow.operators import PythonOperator
from datetime import datetime

default_args = {
    'owner' = 'airflow_user'
    'depends_on_past': 'False',
    'start_date': datetime(2018, 1, 1),
    'retries': 0
}

dag = DAG('python_hello_world_dag',
    default_args = default_args,
    catchup = False,
    schedule_interval = '00 20 * * *')
def hello():
    return print('hello_wrld')
def sum_int():
    return print(2+2)
t1 = PythonOperator(
    task_id='calculate_task',
    python_callable = hello,
    dag=dag
t2 = PythonOperator(
    task_id='calculate_task_2',
    python_callable = sum_int,
    dag=dag
t3 = BashOperator(
    task_id='calculate_task_3',
    bash_command = 'python AirFlow/hello_wooooold_pyt.py',
    dag=dag
t1 >> t2 >> t3    
