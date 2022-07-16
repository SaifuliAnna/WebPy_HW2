from abc import ABCMeta, abstractmethod, ABC

class CliOutputAbstract(metaclass=ABCMeta):

    @abstractmethod
    def output_cli_info(self):
        pass

    def output_cli_data(self):
        pass

    def output_cli_note(self):
        pass

    
