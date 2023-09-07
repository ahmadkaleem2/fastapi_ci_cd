pipeline {
    agent any  // This runs the pipeline on any available agent (Jenkins node).

    stages {

        stage('Setup Virtual Environment') {
            steps {
                // Create a virtual environment and activate it.
                echo 'making venv'
                sh 'python -m venv venv'
                sh 'source venv/bin/activate'
            }
        }


        stage('Build') {
            steps {
                // Run your build commands here.
                // For example, if you're building a Java project with Maven:
            }
        }

        stage('Test') {
            steps {
                // Run your tests here.
                // For example, if you're running JUnit tests:
            }
        }

        stage('Deploy') {
            steps {
                // Deploy your application or artifacts to the desired environment.
                // This could involve copying files, deploying to a server, etc.
                // Replace this with your actual deployment steps.
            }
        }
    }

    post {
        success {
            // Actions to perform if the build is successful.
            // For example, you can send notifications or trigger downstream jobs.
        }
        failure {
            // Actions to perform if the build fails.
            // For example, you can send notifications or take corrective actions.
        }
    }
}
