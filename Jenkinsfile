pipeline {

    agent any

    stages {

        stage('Install Dependencies') {

            steps {

                bat 'if not exist reports mkdir reports'
                bat 'if not exist allure-results mkdir allure-results'

                bat '"C:\\Users\\Rakesh\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {

            steps {

                bat '"C:\\Users\\Rakesh\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" -m pytest --html=reports/report.html --self-contained-html --alluredir=allure-results'
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
                jdk: '',
                results: [[path: 'allure-results']]
            ])
        }
    }
}