import logging
import unittest

import marvin
from marvin import ai_fn
from rich.logging import RichHandler
from rich.traceback import install

from main import Convertex

install()

logger = logging.getLogger("test")

logger.setLevel(logging.INFO)
handler = RichHandler(rich_tracebacks=True, tracebacks_show_locals=True)
formatter = logging.Formatter(
    "%(asctime)s %(message)s",
    datefmt="[%X]"
)
handler.setFormatter(formatter)
logger.addHandler(handler)

marvin.settings.llm_model = "gpt-4"
marvin.settings.llm_temperature = 0.2

@ai_fn
async def calculate_accuracy(original: str, transformed: str, prompt: str) -> float:
    """
    Determines how accurate it `transformed` content which was created from `original` content using 
    provided `prompt` and returns a score between 0.0 and 1.0 where 0.0 means result is completely off 
    and 1.0 means that this is exactly what was expected.
    """


class TestConvertex(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.convertex = Convertex()
        logger.info("Setup completed.")

    async def test_add_prompt_transform_content_similarity(self):
        # Test 1: Greetings
        initial_text = "Hello World!"
        expected_text = "Hi Universe!"
        additional_info = "Converts greetings"
        prompt = await self.convertex.add_prompt(initial_text, expected_text, additional_info, "greeting")
        logger.info(f"Test 1: Greetings - Prompt: \n{prompt}")
        new_initial_text = "Hello there!"
        transformed_text = await self.convertex.transform_content("greeting", new_initial_text)
        accuracy_score = await calculate_accuracy(new_initial_text, transformed_text, prompt)
        logger.info(
            f"Test 1: Greetings - Transformed text: \n{transformed_text}, \nAccuracy score: {accuracy_score}"
        )
        self.assertGreater(accuracy_score, 0.7)

        # Test 2: Farewells
        initial_text = "Goodbye, see you later!"
        expected_text = "Farewell, until next time!"
        additional_info = "Converts farewells"
        prompt = await self.convertex.add_prompt(initial_text, expected_text, additional_info, "farewell")
        logger.info(f"Test 2: Farewells - Prompt: \n{prompt}")
        new_initial_text = "See you, take care!"
        transformed_text = await self.convertex.transform_content("farewell", new_initial_text)
        accuracy_score = await calculate_accuracy(new_initial_text, transformed_text, prompt)
        logger.info(
            f"Test 2: Farewells - Transformed text: \n{transformed_text}, \nAccuracy score: {accuracy_score}"
        )
        self.assertGreater(accuracy_score, 0.7)

        # Test 3: Appreciation
        initial_text = "Thank you very much!"
        expected_text = "I greatly appreciate it!"
        additional_info = "Converts appreciation"
        prompt = await self.convertex.add_prompt(initial_text, expected_text, additional_info, "appreciation")
        logger.info(f"Test 3: Appreciation - Prompt: \n{prompt}")
        new_initial_text = "Thanks a lot!"
        transformed_text = await self.convertex.transform_content("appreciation", new_initial_text)
        accuracy_score = await calculate_accuracy(new_initial_text, transformed_text, prompt)
        logger.info(
            f"Test 3: Appreciation - Transformed text: \n{transformed_text}, \nAccuracy score: {accuracy_score}"
        )
        self.assertGreater(accuracy_score, 0.7)


if __name__ == "__main__":
    unittest.main()
