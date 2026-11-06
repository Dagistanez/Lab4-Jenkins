pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh 'python3 -m pip install --user unittest-xml-reporting fastapi httpx'
            }
        }

        stage('Run Tests for Part 1 (2.1)') {
            steps {
                // Запуск тестів з першої папки
                sh 'python3 -m unittest discover -s 2.1 -p "test_*.py"'
            }
        }

        stage('Run Tests for Part 2 (2.2)') {
            steps {
                // Запуск тестів з другої папки
                sh 'python3 -m unittest discover -s 2.2 -p "test_*.py"'
            }
        }
    }

    post {
        always {
            junit '**/test-reports/*.xml'
        }
        success {
            echo 'Успіх! Усі тести з обох папок пройшли успішно.'
        }
        failure {
            echo 'Увага! Деякі тести провалилися.'
        }
    }
}