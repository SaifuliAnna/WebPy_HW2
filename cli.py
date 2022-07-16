from abc import ABCMeta, abstractmethod, ABC

class CliOutputAbstract(metaclass=ABCMeta):

    @abstractmethod
    def output_cli(self):
        pass


class CliOutputInfo(CliOutputAbstract):

    def output_cli(self):
        pass


class CliOutputData(CliOutputAbstract):

    def output_cli(self):
        pass


class CliOutputNote(CliOutputAbstract):

    def output_cli(self):
        pass

    
