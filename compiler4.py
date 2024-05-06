import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QTextEdit, QLabel
from PyQt5.QtCore import QProcess, QDateTime


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Code Executor')

        vbox = QVBoxLayout()

        self.languageButtons = []
        for language in ['Python', 'C', 'JavaScript']:
            button = QPushButton(language)
            button.clicked.connect(self.selectLanguage)
            self.languageButtons.append(button)
            vbox.addWidget(button)

        self.selectedLanguage = None
        self.codeTextEdit = QTextEdit()
        vbox.addWidget(self.codeTextEdit)

        self.compileButton = QPushButton('Compile & Run')
        self.compileButton.clicked.connect(self.compileAndRun)
        self.compileButton.setEnabled(False)
        vbox.addWidget(self.compileButton)

        self.outputTextEdit = QTextEdit()
        self.outputTextEdit.setReadOnly(True)
        vbox.addWidget(self.outputTextEdit)

        self.executionTimeLabel = QLabel()
        vbox.addWidget(self.executionTimeLabel)

        self.centralWidget = QWidget()
        self.centralWidget.setLayout(vbox)
        self.setCentralWidget(self.centralWidget)

    def selectLanguage(self):
        button = self.sender()
        self.selectedLanguage = button.text()
        self.compileButton.setEnabled(True)

    def compileAndRun(self):
        startTime = QDateTime.currentDateTime()

        code = self.codeTextEdit.toPlainText()
        with open('code.temp', 'w') as f:
            f.write(code)

        self.process = QProcess(self)
        self.process.readyReadStandardOutput.connect(self.onReadyReadStandardOutput)
        self.process.readyReadStandardError.connect(self.onReadyReadStandardError)
        self.process.finished.connect(self.onFinished)

        if self.selectedLanguage == 'Python':
            self.process.start('python', ['code.temp'])
        elif self.selectedLanguage == 'C':
            self.process.start('gcc', ['code.temp', '-o', 'code.out'])
            self.process.waitForFinished()
            if self.process.exitStatus() == QProcess.NormalExit:
                self.process.start('./code.out')
        elif self.selectedLanguage == 'JavaScript':
            self.process.start('node', ['code.temp'])

        endTime = QDateTime.currentDateTime()
        elapsed = startTime.msecsTo(endTime)
        self.executionTimeLabel.setText(f'Execution Time: {elapsed} ms')

    def onReadyReadStandardOutput(self):
        output = self.process.readAllStandardOutput().data().decode()
        self.outputTextEdit.append(output)

    def onReadyReadStandardError(self):
        error = self.process.readAllStandardError().data().decode()
        self.outputTextEdit.append(error)

    def onFinished(self):
        self.outputTextEdit.append(f'Process finished with exit code {self.process.exitCode()}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())