pipeline {

    agent any

    stages {

        stage('Environment Check') {
            steps {
                bat 'where python'
                bat 'python --version'
                bat 'if not exist reports mkdir reports'
                bat 'if not exist allure-results mkdir allure-results'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m pytest --html=reports/report.html --self-contained-html --alluredir=allure-results'
            }
        }
    }

    post {

        always {

            publishHTML([
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'reports',
                reportFiles: 'report.html',
                reportName: 'Automation Report'
            ])

            allure([
                includeProperties: false,
                results: [[path: 'allure-results']]
            ])
        }
    }
}