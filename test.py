from datetime import datetime, timedelta
from airflow import DAG
from airflow.models import BaseOperator
from airflow.operators.dummy_operator import DummyOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(1900, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(seconds=5)
}

def print_diff_time(diff_date):
    current_time = datetime.utcnow()
    time_difference = current_time - diff_date
    print(f"Diferencia de tiempo: {time_difference}")

dag = DAG(
    'test',
    schedule_interval=timedelta(days=1),
    default_args=default_args,
)

start_task = DummyOperator(task_id='start', dag=dag)
end_task = DummyOperator(task_id='end', dag=dag)

n = 5  
task_n = []
for i in range(n):
    task = DummyOperator(task_id=f'task_{i}', dag=dag)
    task_n.append(task)

start_task >> task_n[0]
for i in range(1,n):
    task_n[i] << task_n[i-1]
task_n[-1] >> end_task

class TimeDiffOperator(BaseOperator):
    def __init__(self, diff_date, *args, **kwargs):
        super(TimeDiffOperator, self).__init__(*args, **kwargs)
        self.diff_date = diff_date

    def execute(self, context):
        current_time = datetime.utcnow()
        time_difference = current_time - self.diff_date
        print(f"Diferencia de tiempo: {time_difference}")


diff_date_task = TimeDiffOperator(
    task_id='time_diff_task',
    diff_date=datetime(2023, 7, 26, 3, 0),  
    dag=dag
)


task_n[-1] >> diff_date_task
start_task >> diff_date_task

# Los Hooks en Airflow abstraen la complejidad de la interacción, proporcionando una API.
# Un Hook es una clase de alto nivel que proporciona métodos para interactuar con sistemas externos y
# encapsula la lógica específica de cada sistema. Por otro lado, una Connection es una
# entidad de la base de datos de metadatos que almacena la información de acceso a sistemas externos, como
# credenciales de bases de datos, claves API, contraseñas, etc. 