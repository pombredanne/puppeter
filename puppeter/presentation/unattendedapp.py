import puppeter
from puppeter import container
from puppeter.domain.model.answers import Answers  # NOQA
from puppeter.domain.gateway.answers import AnswersGateway
from puppeter.presentation.app import App


class UnattendedApp(App):
    def __init__(self, parsed):
        App.__init__(self, parsed)
        self.__log = puppeter.get_logger(UnattendedApp)

    def run(self):
        App.run(self)
        file = self._parsed.answers
        answers = self.__load_answers(container.get(AnswersGateway), file)
        if self._parsed.execute:
            self.__log.warning('Installation will be performed from answer file:'
                               ' %s. System will be altered!!!', file.name)
        else:
            self.__log.info('Installation commands will be generated based on answers file'
                            ' %s and printed out. System will NOT be altered.', file.name)
        self.__log.debug(answers)

    @staticmethod
    def __load_answers(gateway, file):
        # type: (AnswersGateway, file) -> Answers
        return gateway.read_answers_from_file(file)
