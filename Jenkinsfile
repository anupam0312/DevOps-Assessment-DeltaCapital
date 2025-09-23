pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/anupam0312/DevOps-Assessment-DeltaCapital.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t anupam03/clients-api:latest ./app'
            }
        }
        stage('Test') {
            steps {
                sh 'echo "Run your tests here (pytest, etc.)"'
            }
        }
        stage('Push Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh 'echo $PASS | docker login -u $USER --password-stdin'
                    sh 'docker push anupam03/clients-api:latest'
                }
            }
        }
        
        stage('List Files') {
    steps {
        sh 'ls -l'
    }
}

        stage('Deploy to K8s') {
            steps {
                sh 'kubectl apply -f k8s/'
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}
