import dagshub
import mlflow
dagshub.init(repo_owner='Gandharv29', repo_name='MLops-mini-proj', mlflow=True)
mlflow.set_tracking_uri('https://dagshub.com/Gandharv29/MLops-mini-proj.mlflow')


with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)