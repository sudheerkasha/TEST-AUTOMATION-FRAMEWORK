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

        stage('Setup Virtual Environment') {
            steps {
                bat "\"C:\\Users\\SUDHEER\\AppData\\Local\\Programs\\Python\\Python313\\python.exe\" -m venv venv"
                bat 'venv\\Scripts\\pip install -r requirements.txt'
            }
        }

        stage('Start Selenium Grid') {
            steps {
                bat(script: 'docker rm -f selenium-hub chrome-node-1 chrome-node-2 chrome-node-3 || exit 0', returnStatus: true)
                bat 'docker-compose up -d'
                bat '''
:loop
curl http://127.0.0.1:4444/status | find "ready" > nul
if %errorlevel% neq 0 (
    echo Waiting for Grid...
    timeout /t 5 > nul
    goto loop
)
'''
            }
        }

        stage('Verify Grid') {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'UNSTABLE') {
                    bat 'curl -s http://127.0.0.1:4444/status'
                }
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                    venv\\Scripts\\pytest -n 3 --dist=loadscope ^
                           --alluredir=reports/allure-results ^
                           --junitxml=reports/junit.xml ^
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
            bat(script: 'docker-compose down', returnStatus: true)
            bat(script: 'docker rm -f selenium-hub chrome-node-1 chrome-node-2 chrome-node-3 || exit 0', returnStatus: true)

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
    }
}
