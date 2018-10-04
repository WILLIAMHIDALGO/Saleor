pipeline {
  agent any
  stages {
    stage('Paso 1: inicio') {
      steps {
        echo 'Entrando a pipeline'
      }
    }
    stage('Paso 2: rama de ejecución') {
      steps {
        echo 'Rama ' + env.BRANCH_NAME
      }
    }
    stage ("Paso 3: Rama de desarrollador") {
      // si no es la rama master entonces ejecuta la integración continua
      when { not { branch 'master' } }
      steps {
        echo "entrando a hacer el pull request y merge"
        //withCredentials([usernameColonPassword(credentialsId: 'c1eba0c7-651a-41ba-8065-6307a6cb1630', variable: 'key_jenkins')]) {
       withCredentials([usernameColonPassword( git credentialsId: 'c1eba0c7-651a-41ba-8065-6307a6cb1630', url: 'https://github.com/WILLIAMHIDALGO/Saleor/tree/andersonenriquez')]) {  
        sh 'git checkout master'
          sh 'git pull . origin/' + "${env.BRANCH_NAME}"
          sh 'git merge origin/' + "${env.BRANCH_NAME}"
          sh 'git pull'
          sh 'git push'
        }
      }
    }
    stage ("Paso 3: Rama master") {
      // si es la rama master no se hace integración
      when { branch 'master'}
      steps {
        echo 'Sólo se ejecuta en ramas de desarroladores'
      }
    }
  }
}
