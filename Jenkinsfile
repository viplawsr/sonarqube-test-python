pipeline{
    agent any
    stages{
        
        stage('Sonar qube'){
            steps{
                script{
                     def scannerHome = tool 'SonarScan';
                    
                        withSonarQubeEnv('Sonar'){
                          sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=check"
                        
                    }
                    
                    
                }
                
                
                
            }
        }
    }
   
}
