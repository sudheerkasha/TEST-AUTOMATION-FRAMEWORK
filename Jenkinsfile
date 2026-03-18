pipeline {

    agent any

    environment {
        BASE_URL        = "https://react-frontend-api-testing.vercel.app"
        BROWSER         = "chrome"
        HEADLESS        = "true"
        EXECUTION_MODE  = "remote"
        GRID_URL        = "http://127.0.0.1:4444/wd/hub"
        ADMIN_EMAIL     = "admin@example.com"
        ADMIN_PASSWORD  = "Admin@123"
        USER_EMAIL      = "user@example.com"
        USER_PASSWORD   = "User@123"
        DEFAULT_WAIT    = "10"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/sudheerkasha/TEST-AUTOMATION-FRAMEWORK.git'
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                bat '''
                python -m venv venv
                venv\\Scripts\\python -m pip install --upgrade pip
                venv\\Scripts\\pip install -r requirements.txt
                '''
            }
        }

        stage('Start Selenium Grid') {
            steps {
                bat '''
                docker rm -f selenium-hub chrome-node-1 chrome-node-2 chrome-node-3
                docker-compose up -d
                timeout /t 30
                '''
            }
        }

        stage('Verify Grid') {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'UNSTABLE') {
                    bat 'curl http://127.0.0.1:4444/status'
                }
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                venv\\Scripts\\pytest -n 3 --dist=loadscope ^
                --alluredir=reports\\allure-results ^
                --junitxml=reports\\junit.xml ^
                -v
                '''
            }
        }

        stage('Generate Allure Report') {
            steps {
                allure([
                    includeProperties: false,
                    jdk: '',
                    reportBuildPolicy: 'ALWAYS',
                    results: [[path: 'reports/allure-results']]
                ])
            }
        }
    }

    post {

        always {

            // 
            bat 'docker-compose down'
            bat 'docker rm -f selenium-hub chrome-node-1 chrome-node-2 chrome-node-3'

            junit testResults: 'reports/junit.xml',
                  allowEmptyResults: true

            archiveArtifacts artifacts: 'reports/screenshots/*.png',
                             allowEmptyArchive: true

            archiveArtifacts artifacts: 'logs/automation.log',
                             allowEmptyArchive: true
        }

        success {
            echo 'All tests passed.'
        }

        failure {
            echo 'Tests failed. Check Allure report and screenshots.'
        }
    }
}
