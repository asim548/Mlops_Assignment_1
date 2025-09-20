pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master',
                    url: 'https://github.com/asim548/MLOps_Assignment_1.git'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'pytest --maxfail=1 --disable-warnings -q'
            }
        }

        stage('Build Docker Image (Mock)') {
            steps {
                echo "Simulating Docker build for mlops-assignment-app:${env.BUILD_NUMBER}"
            }
        }

        stage('Push Docker Image (Mock)') {
            steps {
                echo "Simulating push to DockerHub (skipped because Docker is not installed)"
            }
        }
    }

    post {
        success {
            mail to: 'admin@example.com',
                 subject: "✅ Jenkins Build Successful: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                 body: "The pipeline has successfully run tests and simulated Docker build/push."
        }
        failure {
            mail to: 'admin@example.com',
                 subject: "❌ Jenkins Build Failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                 body: "The pipeline failed. Please check Jenkins logs."
        }
    }
}
