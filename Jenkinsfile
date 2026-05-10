pipeline {

    agent any

    stages {

        stage('Clean Workspace') {
            steps {
                bat '''
                    if exist reports rmdir /s /q reports
                    if exist allure-results rmdir /s /q allure-results

                    mkdir reports
                    mkdir allure-results
                '''
            }
        }

        stage('Environment Check') {
            steps {
                bat '''
                    where python
                    python --version
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                    python -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                    python -m pytest ^
                    --html=reports/report.html ^
                    --self-contained-html ^
                    --alluredir=allure-results
                '''
            }   
        }
    }

    post {

        always {

            // HTML Report
            publishHTML([
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'reports',
                reportFiles: 'report.html',
                reportName: 'Automation Report'
            ])

            // Allure Report
            allure([
                includeProperties: false,
                results: [[path: 'allure-results']]
            ])
        }
    }
}