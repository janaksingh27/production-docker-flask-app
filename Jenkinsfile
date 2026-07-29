pipeline {
    agent any

    environment {
        IMAGE_NAME = "janaksingh/production-docker-flask-app:v1"
    }

    stages {

        stage('Git Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Docker Hub Login') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh 'echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin'
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                sh 'docker push $IMAGE_NAME'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                docker stop production-app || true
                docker rm production-app || true

                docker pull $IMAGE_NAME

                docker run -d \
                  --name production-app \
                  -p 5000:5000 \
                  --restart unless-stopped \
                  $IMAGE_NAME
                '''
            }
        }

        stage('Success') {
            steps {
                echo 'Application Deployed Successfully!'
            }
        }
    }
}
