pipeline {
  agent { docker { image 'python:3.10.0' } }
  stages {
    stage('build') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh 'python3 -m pytest tests/ --html=report.html'
      }   
    }
  }
}