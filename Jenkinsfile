pipeline {
  agent { dockerfile {
            filename 'Dockerfile'
            args '-v /mnt/ssd:/mnt/ssd -v /home/brian/.ssh:/root/.ssh --privileged  --cap-add=CAP_MKNOD'
           }
  }
  stages {
    stage('DevOps') {
      steps {
        echo 'Deploy DevOps environment'
        sh label: 'Deploy Gitea', script: '''chmod +x scripts/deployGitea.py && python ./scripts/deployGitea.py'''
        sh label: 'Deploy CouchDB', script: '''chmod +x scripts/deployCouchDB.py && python ./scripts/deployCouchDB.py'''
      }
    }
  }
}