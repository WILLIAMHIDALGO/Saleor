pipeline {
  agent any
  stages {
    stage('Paso 1: inicio') {
      steps {
        echo 'Entrando a pipeline'
      }
      steps {
        echo 'Rama ' + env.BRANCH_NAME
      }
      // si no es la rama master entonces ejecuta la integración continua
      when { not { branch 'master' } }
      steps {
        echo "entrando a hacer el pull request y merge"
        withCredentials([sshUserPrivateKey(credentialsId: '20f8159b-d214-48c3-9f07-4ae2aa3af5a9', keyFileVariable: '', passphraseVariable: '', usernameVariable: '')]) {
          sh 'cd projects/saleor_checkout/'
          sh 'git remote set-url origin https://Madesoft:Madesoft2018*@github.com/WILLIAMHIDALGO/Saleor.git'
          echo 'mostrando ramas remotas'
          sh 'git branch -r'
          sh 'git fetch origin'
          sh 'git checkout origin/master'
          sh 'git pull . origin/' + "${env.BRANCH_NAME}" + ' --allow-unrelated-histories'
          sh 'git merge origin/' + "${env.BRANCH_NAME}"
          //sh 'git pull'
          sh 'git push origin HEAD:master'
          echo 'Proceso finalizado exitosamente'
          echo 'probando nuevamente evento webhook con nueva url'
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
