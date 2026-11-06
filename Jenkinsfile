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
                // Створюємо віртуальне середовище .venv та встановлюємо в нього залежності
                sh '''
                    python3 -m venv venv
                    ./venv/bin/pip install --upgrade pip
                    ./venv/bin/pip install unittest-xml-reporting fastapi httpx
                '''
            }
        }

        stage('Run Tests for Part 1 (2.1)') {
            steps {
                // Запускаємо тести з першої папки через python з віртуального середовища
                sh './venv/bin/python3 -m unittest discover -s 2.1 -p "test_*.py"'
            }
        }

        stage('Run Tests for Part 2 (2.2)') {
            steps {
                // Запускаємо тести з другої папки
                sh './venv/bin/python3 -m unittest discover -s 2.2 -p "test_*.py"'
            }
        }
    }

    post {
        always {
            junit '**/test-reports/*.xml'
        }
        success {
            echo 'Успіх! Усі тести з обох палок пройшли успішно.'
        }
        failure {
            echo 'Увага! Деякі тести провалилися.'
        }
    }
}