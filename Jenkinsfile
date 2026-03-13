pipeline {
<<<<<<< HEAD
    agent any

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/rupakdhar/LabView_Python.git'
            }
        }

        stage('Verify Files') {
            steps {
                bat 'dir %WORKSPACE%'
            }
        }

        stage('Build LabVIEW') {
            steps {
                bat '''
                "C:\\Program Files (x86)\\National Instruments\\Shared\\LabVIEW CLI\\LabVIEWCLI.exe" ^
                -OperationName ExecuteBuildSpec ^
                -ProjectPath "%WORKSPACE%\\MyProject.lvproj" ^
                -BuildSpecName "MyApplicationBuild"
                '''
            }
        }
=======
  agent {
    node {
      label 'Start'
    }

  }
  stages {
    stage('Test Jenkins') {
      steps {
        echo 'Jenkins pipeline is working'
      }
    }

  }
}
>>>>>>> 1d0b7853afb977d38b91bd250c34cd56be2e6a02
