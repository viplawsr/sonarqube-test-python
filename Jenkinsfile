pipeline{
    agent any
    stages{
        
        
        stage('Sonar cube'){
            steps{
                script{
                    scannerHome = tool 'Sonar';
                }
                
                withSonarQubeEnv('sonar'){
                    sh 'sonar-scanner.bat -D"sonar.projectKey=prac" -D"sonar.python.coverage.reportPaths=coverage.xml" -D"sonar.pullrequest.key=4" -D"sonar.pullrequest.base=main" -D"sonar.pullrequest.branch=check"'
                    
                    
                }
                
            }
        }
    }
   
}
