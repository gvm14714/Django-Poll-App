pipeline {
    agent any
    environment {
        DOCKER_IMAGE = 'weezy'
        DOCKER_REGISTRY = 'gym14714'
        KUBECONFIG_CREDENTIAL_ID = 'my-kubeconfig-file'
        DOCKER_COMMAND = '/usr/local/bin/docker'
        KUBECTL_COMMAND = '/usr/local/bin/kubectl'
        PYTHON_COMMAND = '/usr/local/bin/python3'
    }
    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Prepare Environment') {
            steps {
                script {
                    sh "${PYTHON_COMMAND} -m venv venv"
                    sh 'source venv/bin/activate'
                    sh "${PYTHON_COMMAND} -m pip install django"
                    sh "${PYTHON_COMMAND} -m pip install -r requirements.txt"
                    sh "${PYTHON_COMMAND} manage.py makemigrations"
                    sh "${PYTHON_COMMAND} manage.py migrate"
                    sh "${PYTHON_COMMAND} -m pip install faker"
                    sh "echo \"import seeder; seeder.seed_all(30)\" | ${PYTHON_COMMAND} manage.py shell"
                }
            }
        }
    }
}
     