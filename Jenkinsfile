pipeline {
    agent any

    environment {
        VENV = '/var/lib/jenkins/venv'
        PYTHON = "${VENV}/bin/python"
        PIP = "${VENV}/bin/pip"
    }

    stages {
        stage('Install Dependencies') {
            steps {
                sh '''
                    ${PIP} install -r requirements.txt
                '''
            }
        }

        stage('Black - Format Check') {
            steps {
                sh '''
                    ${VENV}/bin/black --check --diff . || true
                '''
            }
        }

        stage('Flake8 - Style Check') {
            steps {
                sh '''
                    ${VENV}/bin/flake8 --format=pylint --output-file=flake8-report.txt . || true
                '''
            }
        }

        stage('Pylint - Deep Analysis') {
            steps {
                sh '''
                    ${VENV}/bin/pylint --output-format=parseable \
                      --disable=C0114,C0115,C0116 \
                      app.py > pylint-report.txt || true
                '''
            }
        }

        stage('Unit Test') {
            steps {
                sh '''
                    ${PYTHON} -m pytest tests/ \
                      --junitxml=reports/results.xml \
                      --cov=. --cov-report=html:reports/html
                '''
            }
        }
    }

    post {
        always {
            junit 'reports/results.xml'

            // 使用 qualityGates 定义质量门禁（推荐）
            recordIssues(
                tools: [
                    pyLint(pattern: 'pylint-report.txt'),
                    flake8(pattern: 'flake8-report.txt')
                ],
                qualityGates: [
                    [threshold: 50, type: 'TOTAL', criticality: 'UNSTABLE'],
                    [threshold: 100, type: 'TOTAL', criticality: 'FAILURE']
                ]
            )

            publishHTML(target: [
                reportDir: 'reports/html',
                reportFiles: 'index.html',
                reportName: 'Coverage Report'
            ])
        }
    }
}