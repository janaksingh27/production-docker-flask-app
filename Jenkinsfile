pipeline {
    agent any

    stages {

        stage('Git Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t janaksingh/production-docker-flask-app:v1 .'
            }
        }

        stage('Success') {
            steps {
                echo 'Docker Image Build Successful!'
            }
        }
    }
}
