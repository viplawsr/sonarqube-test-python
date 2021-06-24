pipeline{
    agent any
    stages{
        
        stage('build') {
          steps {
            sh 'coverage run test_add.py'
            sh 'coverage report -m'
            sh 'coverage xml -i'
          }
        }
        stage('Sonar cube'){
            steps{
                script{
                    scannerHome = tool 'Sonar';
                }
                
                withSonarQubeEnv('sonar'){
                    sh 'sonar-scanner.bat -D"sonar.projectKey=platform-nuggets_sonarqube-test-python" -D"sonar.python.coverage.reportPaths=coverage.xml" -D"sonar.pullrequest.key=4" -D"sonar.pullrequest.base=main" -D"sonar.pullrequest.branch=check"'
                    
                    
                }
                
            }
        }
    }
   
}
