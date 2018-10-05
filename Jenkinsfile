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
        //withCredentials([usernameColonPassword(credentialsId: 'c1eba0c7-651a-41ba-8065-6307a6cb1630', variable: 'key_jenkins')]) {
        //withCredentials([usernameColonPassword( git credentialsId: 'c1eba0c7-651a-41ba-8065-6307a6cb1630', url: 'https://github.com/WILLIAMHIDALGO/Saleor/tree/andersonenriquez')]) {
        withCredentials([usernameColonPassword(credentialsId: '954ecaac-dc69-4712-9835-857c65b79f80', variable: 'key_access')]) {
          //bat 'git fetch --depth=1 origin -p --tags'
          bat 'git config remote.origin.url https://github.com/WILLIAMHIDALGO/Saleor.git'
          echo 'mostrando remote show origin'
          bat 'git remote show origin'
          echo 'mostrando ramas remotas'
          bat 'git branch -r'
          echo 'mostrando todas las ramas'
          bat 'git branch -a'
          echo 'ramas disponibles'
          bat 'git branch -v -a'
          bat 'git checkout master'
          bat 'git pull . origin/' + "${env.BRANCH_NAME}"
          bat 'git merge origin/' + "${env.BRANCH_NAME}"
          bat 'git pull'
          bat 'git push'
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
