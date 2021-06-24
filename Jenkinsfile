pipeline{
    agent any
    stages{
        
        stage('Cloning'){
            steps{
                 
                git branch: 'main',  url: 'https://viplawsr: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@github.com/viplawsr/sonarqube-test-python.git'
            }
        }
        
        stage('Sonar cube'){
            steps{
                script{
                    scannerHome = tool 'Sonar';
                }
                
                withSonarQubeEnv('sonar'){
                    sh 'sonar-scanner.bat -D"sonar.projectKey=prac" -D"sonar.python.coverage.reportPaths=coverage.xml" -D"sonar.pullrequest.key=1" -D"sonar.pullrequest.base=main" -D"sonar.pullrequest.branch=check" -X'
                    
                    
                }
                
            }
        }
    }
   
}
