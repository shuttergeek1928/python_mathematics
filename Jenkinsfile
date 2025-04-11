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
                sh 'mkdir -p staging/python_mathematics && cp -r * deployment/staging/python_mathematics/'
                sh 'echo "Deployed to staging at deployment/staging/python_mathematics"'
            }
        }
        stage('Deploy to Production') {
            when {
                branch 'release'
            }
            steps {
                sh 'mkdir -p production/python_mathematics && cp -r * production/python_mathematics/'
                sh 'echo "Deployed to production at production/python_mathematics"'
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