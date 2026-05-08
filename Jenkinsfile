pipeline {

    agent any

    stages {

        stage('Install Dependencies') {

            steps {

                bat 'python -m pip install -r requirements.txt'
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