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
        withCredentials([sshUserPrivateKey(credentialsId: '20f8159b-d214-48c3-9f07-4ae2aa3af5a9', keyFileVariable: '', passphraseVariable: '', usernameVariable: '')]) {
          sh 'git --version'
          sh 'git remote set-url origin https://Madesoft:Madesoft2018*@github.com/WILLIAMHIDALGO/Saleor.git'
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
          sh 'git config user.name "Madesoft"'
          sh 'git config user.email "madesoft.2.2018@gmail.com"'
          sh 'git push origin HEAD:master'
          echo 'Proceso finalizado'
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
