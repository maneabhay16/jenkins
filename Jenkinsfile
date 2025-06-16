pipeline {
    agent any

    environment {
        VENV = "${WORKSPACE}/venv"
    }

    stages {
        stage('Clone Repo') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                sh(script: '''
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install -r requirements.txt
                ''', shell: '/bin/bash')
            }
        }

        stage('Run Tests') {
            steps {
                sh(script: '''
                    source venv/bin/activate
                    python manage.py test
                ''', shell: '/bin/bash')
            }
        }
    }
}
