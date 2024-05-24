import logging

from cltl.template.api import DemoProcessor

logger = logging.getLogger(__name__)


class DummyDemoProcessor(DemoProcessor):
    """
    Dummy implementation of the component.
    """
    def __init__(self, phrase: str):
        self.__phrase = phrase

    def respond(self, statement: str) -> str:
        logger.debug("Responding to statement: %s", statement)

        return f"Mhm, you mean {self.__phrase}?." if statement else "Hi!"
