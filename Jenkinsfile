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
        withCredentials([usernameColonPassword(credentialsId: '44418711-d740-465e-8027-b85b0cb8ac73', variable: 'key_access')]) {
          sh 'git remote set-url origin https://github.com/WILLIAMHIDALGO/Saleor.git'
          echo 'mostrando remote show origin'
          sh 'git remote show origin'
          echo 'mostrando ramas remotas'
          sh 'git branch -r'
          echo 'mostrando todas las ramas'
          sh 'git branch -a'
          echo 'ramas disponibles'
          sh 'git branch -v -a'
          sh 'git fetch origin'
          sh 'git checkout origin/master'
          sh 'git pull . origin/' + "${env.BRANCH_NAME}" + ' --allow-unrelated-histories'
          sh 'git merge origin/' + "${env.BRANCH_NAME}"
          //sh 'git pull'
          sh 'git push origin HEAD:master'
          echo 'Proceso finalizado de nuevo'
        }
      }
    }
    stage ("Paso 3: Rama master") {
      // si es la rama master no se hace integración
      when { branch 'master'}
      steps {
        echo 'Sólo se ejecuta en ramas de desarrolladores'
      }
    }
  }
}
