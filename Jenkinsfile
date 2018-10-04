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
      // si no es la rama master entonces ejecuta la integración continua  sh git checkout origin/master
      when { not { branch 'master' } }
      steps {
        echo "entrando a hacer el pull request y merge"
        withCredentials([usernameColonPassword(credentialsId: 'c1eba0c7-651a-41ba-8065-6307a6cb1630', variable: 'key_jenkins')]) {
          echo "Succes Credentials"
          sh 'git checkout master'
          echo "Checkout succes"+ env.BRANCH_NAME
          sh 'git pull . origin/' + "${env.BRANCH_NAME}"
          echo "Pull succes"+ env.BRANCH_NAME
          sh 'git merge origin/' + "${env.BRANCH_NAME}"
          echo "merge succes"+ env.BRANCH_NAME
          sh 'git pull'
          echo "pull succes"
          sh 'git push'
          echo "push succes"
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
