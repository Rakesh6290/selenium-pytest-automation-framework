pipeline {

    agent any

    stages {

        stage('Clone Repository') {

            steps {

                git 'https://github.com/Rakesh6290/selenium-pytest-automation-framework.git'
            }
        }

        stage('Install Dependencies') {
                            
            steps {

                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {

            steps {

                bat 'pytest --html=report.html --alluredir=allure-results'
            }
        }
    }

    post {

        always {

            publishHTML([
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: '.',
                reportFiles: 'report.html',
                reportName: 'Automation Report'
            ])
        }
    }
}