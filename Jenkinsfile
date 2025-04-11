pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/shuttergeek1928/python_mathematics.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Build') {
            steps {
                sh 'echo "Building the Python project..."'
                sh 'python setup.py build' // Build the project using setup.py
                sh 'python setup.py sdist' // Create a source distribution
                sh 'python setup.py bdist_wheel' // Create a wheel distribution
            }
        }
        stage('Test') {
            steps {
                sh 'python -m unittest discover -s tests'
            }
        }
        stage('Deploy to Staging') {
            steps {
                sh 'echo "Deploying to staging..."'
                sh 'cp -r * C:/Users/atish/JenkinsDeployment'
                sh 'echo "Deployed to staging at JenkinsDeployment/python_mathematics"'
            }
        }
        stage('Deploy to Production') {
            steps {
                sh 'echo "Deploying to production..."'
                sh 'cp -r * C:/Users/atish/JenkinsProdDeployment'
                sh 'echo "Deployed to production at JenkinsProdDeployment/python_mathematics"'
            }
        }
    }
    post {
        failure {
            echo 'Pipeline failed!'
        }
        success {
            echo 'Pipeline succeeded!'
        }
    }
}