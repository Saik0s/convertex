import argparse
import asyncio
import json
import logging
import os
from pathlib import Path

import marvin
from marvin import ai_fn
from rich import print
from rich.logging import RichHandler
from rich.traceback import install

install()

logger = logging.getLogger("main")

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

# Define the path to store prompts.json
CONFIG_PATH = Path.home() / ".config/convertex/prompts.json"


def load_prompts():
    if CONFIG_PATH.exists():
        with open(CONFIG_PATH, "r") as file:
            return json.load(file)
    return {}


def save_prompts(prompts):
    os.makedirs(CONFIG_PATH.parent, exist_ok=True)
    with open(CONFIG_PATH, "w") as file:
        json.dump(prompts, file, indent=4)


@ai_fn
async def generate_prompt(current_content: str, desired_content: str, additional_info: str) -> str:
    """
    Given the `current_content` and `desired_content` as text or code with optional `additional_info`, generate a clear and concise 
    instruction prompt that outlines the step-by-step process required to transform any similar content similar to this `current_content` 
    into its their corresponding desired content. The instructions should be generic, not tied to the `current_content` or `desired_content`. 
    It should be easily understood and applicable to similar pieces of text or code, while it should not include `current_content` or `desired_content`
    in the instructions. Each step should be clearly defined and focused on a single task. 
    """

@ai_fn
async def transform_content(prompt: str, current_content: str) -> str:
    """
    Given a generic `prompt` and the `current_content`, your task is to generate the transformed content. 
    The transformation should be accurately based on the instructions provided in the `prompt` and applied 
    to the `current_content`. It's crucial that the transformed content mirrors the intent of the `prompt` accurately.
    """


class Convertex:
    def __init__(self):
        self.prompts = load_prompts()

    async def add_prompt(self, current_content: str, desired_content: str, additional_info: str, name: str):
        prompt = await generate_prompt(current_content, desired_content, additional_info)
        self.prompts[name] = prompt
        save_prompts(self.prompts)
        return prompt

    async def transform_content(self, name: str, current_content: str):
        prompt = self.prompts[name]
        return await transform_content(prompt, current_content)

    def list_of_prompt_names(self):
        return self.prompts.keys()


async def async_main():
    parser = argparse.ArgumentParser(description="A utility tool for content transformation.")
    subparsers = parser.add_subparsers(dest="command")

    # add_prompt command
    parser_add = subparsers.add_parser("add_prompt", help="Add a new prompt.")
    parser_add.add_argument("current_content", help="The current content.")
    parser_add.add_argument("desired_content", help="The desired content.")
    parser_add.add_argument("additional_info", help="Additional info for this prompt.")
    parser_add.add_argument("name", help="A name for this prompt.")

    # transform_content command
    parser_gen = subparsers.add_parser("transform_content", help="Transform content based on a prompt.")
    parser_gen.add_argument("name", help="The name of the prompt.")
    parser_gen.add_argument("current_content", help="The content to be transformed.")

    # list_prompts command
    parser_list = subparsers.add_parser("list_prompts", help="List all available prompts.")

    args = parser.parse_args()

    convertex = Convertex()

    if args.command == "add_prompt":
        result = await convertex.add_prompt(args.current_content, args.desired_content, args.additional_info, args.name)
        print(f"[bold green]Prompt added successfully:[/bold green] {result}")
    elif args.command == "transform_content":
        result = await convertex.transform_content(args.name, args.current_content)
        print(f"[bold green]Transformed content:[/bold green] {result}")
    elif args.command == "list_prompts":
        result = convertex.list_of_prompt_names()
        print(f"[bold green]List of prompt names:[/bold green] {result}")
    else:
        parser.print_help()

def main():
    asyncio.run(async_main())

if __name__ == "__main__":
    main()
