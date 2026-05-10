pipeline {

    agent any

    stages {

        stage('Environment Check') {
            steps {
                bat '''
                    where python
                    python --version

                    if not exist reports mkdir reports
                    if not exist allure-results mkdir allure-results
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

        stage('Generate Allure Report') {
            steps {
                bat '''
                    allure generate allure-results -c -o allure-report
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