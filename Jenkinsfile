pipeline {

    agent any

    stages {

        stage('Install Dependencies') {

            steps {

                bat 'py -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {

            steps {

                bat 'py -m pytest --html=report.html --alluredir=allure-results'
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