pipeline {

    agent any

    stages {

        stage('Environment Check') {
            steps {
                bat '''
                    where python
                    python --version

                    if exist reports rmdir /s /q reports
                    if exist allure-results rmdir /s /q allure-results

                    mkdir reports
                    mkdir allure-results
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
                    --alluredir=allure-results ^
                    --reruns 2 ^
                    --reruns-delay 2
                '''
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