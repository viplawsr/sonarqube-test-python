node{
   
        
        stage('Sonar qube'){
            steps{
                
                     def scannerHome = tool 'SonarScan';
                    
                        withSonarQubeEnv('Sonar'){
                          sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=check"
                           }
                
                
                
            }
        }
    
   
}
