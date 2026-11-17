pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Setup venv and Install Dependencies') {
            steps {
                sh '''
                    rm -rf venv
                    python3 -m venv venv
                    ./venv/bin/pip install --upgrade pip
                    ./venv/bin/pip install unittest-xml-reporting fastapi httpx
                '''
            }
        }

        stage('Run Tests for Part 1 (2.1)') {
            steps {
                // Запускаємо через xmlrunner з вказанням папки для XML-звітів
                sh './venv/bin/python3 -m xmlrunner discover -s 2.1 -p "test_*.py" -o test-reports'
            }
        }

        stage('Run Tests for Part 2 (2.2)') {
            steps {
                sh './venv/bin/python3 -m xmlrunner discover -s 2.2 -p "test_*.py" -o test-reports'
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