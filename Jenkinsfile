pipeline {
    agent any
    triggers {
        cron('0 12 * * *')
    }
    stages {
        stage('Blog') {
            steps {
                echo 'Blog...'
                sh 'make b d'
            }
        }
    }
}
