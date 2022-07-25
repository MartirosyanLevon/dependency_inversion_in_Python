import sys
import time


class TerminalPrinter:
    def write(self, msg):
        sys.stderr.write(f'{msg}\n')


class FilePrinter:
    def write(self, msg):
        with open('log.txt', 'a+', encoding='UTF8') as f:
            f.write(f'{msg}\n')


class Logger:
    def __init__(self):
        self.prefix = time.strftime('%Y-%b-%d %H:%M:%S', time.localtime())

    # instead log_stderr and log_file functions,created one log function which can use any classes for print!
    def log(self, message, notifier):
        notifier().write(f'{self.prefix} {message}')

    # def log_stderr(self, message):
    #     TerminalPrinter().write(f'{self.prefix} {message}')
    #
    # def log_file(self, message):
    #     FilePrinter().write(f'{self.prefix} {message}')


logger = Logger()
# logger.log_stderr('Starting the programm...')
# logger.log_stderr('An error!')

# Dependency inversion
logger.log('Starting the programm...', TerminalPrinter)
logger.log('An error!', FilePrinter)
