pipeline {
    agent {
        label 'slave-node' // Replace 'slave-node' with the label of your slave node
    }
    stages {
        stage('Ensure Slave Node is Running') {
            steps {
                script {
                    def nodeName = 'slave-node' // Replace with your slave node's name
                    def node = Jenkins.instance.getNode(nodeName)
                    if (node && !node.toComputer().isOnline()) {
                        echo "Starting slave node: ${nodeName}"
                        node.toComputer().connect(false) // Attempt to connect the node
                        sleep 10 // Wait for the node to come online
                        if (!node.toComputer().isOnline()) {
                            error "Failed to bring slave node ${nodeName} online"
                        }
                    } else {
                        echo "Slave node ${nodeName} is already online"
                    }
                }
            }
        }
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