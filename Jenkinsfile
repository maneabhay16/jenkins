pipeline {
    agent any

    parameters {
        choice(name: 'ENV', choices: ['dev', 'staging', 'prod'], description: 'Select environment to build and deploy')
    }

    environment {
        VENV = "${WORKSPACE}/venv"
        DJANGO_ENV = "${params.ENV}"
        // Uncomment this if using Jenkins Credentials Plugin
        // DJANGO_SECRET_KEY = credentials('django_secret_key')  
    }

    stages {
        stage('Clone Repo') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    export DJANGO_ENV=${DJANGO_ENV}
                    python manage.py test
                '''
            }
        }

        stage('Collect Static Files') {
            steps {
                sh '''
                    . venv/bin/activate
                    export DJANGO_ENV=${DJANGO_ENV}
                    python manage.py collectstatic --noinput
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo "Ready to deploy to ${params.ENV}..."
                // Add your deploy logic here: rsync, SSH, Docker push, etc.
            }
        }
    }

    post {
        always {
            echo "Build finished for environment: ${params.ENV}"
        }
        failure {
            echo "Build failed. Please check errors."
        }
    }
}
