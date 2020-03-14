#DAG NAME:: Sambad_dag
OPERATORS, SENSORS, AND TASKShttps://medium.com/@dustinstansbury/understanding-apache-airflows-key-concepts-a96efed52b1a
"""
 Following DAG is for showing dependencies between Tasks
"""

import logging
import os
import time
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python_operator import PythonOperator

logger = logging.getLogger(__name__)

default_args = {
    'owner': 'FA_TEAM',
    'start_date': days_ago(1),
    'depends_on_past': False,
    'catchup': False,
    'retries': 0,
}

DAG_ID = os.path.basename(__file__).replace(".pyc", "").replace(".py", "")
SCHEDULE_INTERVAL = None ##(as requirement you can schedule it)

dag = DAG(DAG_ID, default_args=default_args, schedule_interval=SCHEDULE_INTERVAL)
dag.doc_md = __doc__

with dag:

    def operation1():
        for i in range(5):
            logger.info("Operation one step {} getting running now".format(i))
            time.sleep(5)

    def operation2():
        for i in range(5):
            logger.info("Operation two step {} getting running now".format(i))
            time.sleep(5)

    def operation3():
        for i in range(5):
            logger.info("Operation three step {} getting running now".format(i))
            time.sleep(5)

    def operation4():
        for i in range(5):
            logger.info("Operation four step {} getting running now".format(i))
            time.sleep(5)

    task1 = PythonOperator(
        task_id='task1',
        python_callable=operation1
    )

    task2 = PythonOperator(
        task_id='task2',
        python_callable=operation2
    )

    task3 = PythonOperator(
        task_id='task3',
        python_callable=operation3
    )

    task4 = PythonOperator(
        task_id='task4',
        python_callable=operation4
    )

    ##Triggering tasks with dependencies
    task1 >> [task2, task3] >> task4

if __name__ == "__main__":
    dag.cli()