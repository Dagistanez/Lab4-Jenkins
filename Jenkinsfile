pipeline {
    agent {
        node {
            label '' // Запускає збірку на тому ж вузлі, де налаштований головний Jenkins
        }
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Run Tests') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install fastapi httpx unittest-xml-reporting
                    python -m unittest discover -s 2.1 -p "test_*.py"
                    python -m unittest discover -s 2.2 -p "test_*.py"
                '''
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t kokhan0/taxi-app:latest .'
            }
        }
        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh 'echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin'
                    sh 'docker push kokhan0/taxi-app:latest'
                }
            }
        }
    }
}