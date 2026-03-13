pipeline {
    agent any

    environment {
        LABVIEWCLI = "C:\\Program Files (x86)\\National Instruments\\Shared\\LabVIEW CLI\\LabVIEWCLI.exe"
    }

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/rupakdhar/LabView_Python.git'
            }
        }

        stage('Build LabVIEW') {
            steps {
                bat "\"%LABVIEWCLI%\" -OperationName ExecuteBuildSpec -ProjectPath \"%WORKSPACE%\\MyProject.lvproj\" -BuildSpecName \"MyApplicationBuild\""
            }
        }

    }
}