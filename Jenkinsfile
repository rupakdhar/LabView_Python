pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/rupakdhar/LabView_Python.git'
            }
        }

        stage('Build LabVIEW') {
            steps {
                bat """
                "C:\\Program Files (x86)\\National Instruments\\Shared\\LabVIEW CLI\\LabVIEWCLI.exe" ^
                -OperationName ExecuteBuildSpec ^
                -ProjectPath "%WORKSPACE%\\MyProject.lvproj" ^
                -BuildSpecName "MyApplicationBuild"
                """
            }
        }
    }
}