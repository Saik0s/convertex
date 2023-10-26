# Convertex: Your Daily Text and Code Transformation Tool

Convertex is a helpful tool that assists with small text or code-based tasks. It allows you to modify text based on prompts you define. This is particularly useful for repetitive tasks or when you need to make specific changes to different pieces of text or code.

To install Convertex, run the command:

```bash
make install
```

Here is a simple guide on how to use Convertex:

1. Add a new prompt: Define the transformation rules using the command:

```bash
python main.py add_prompt 'current content' 'desired content' 'additional info' 'prompt name'
```

2. Transform content based on a prompt: Apply a prompt to your content using the command:

```bash
python main.py transform_content 'prompt name' 'current content'
```

3. List all available prompts: View all your prompts with the command:

```bash
python main.py list_prompts
```

To test Convertex, run the following command:

```bash
make test
```

## License

Convertex is licensed under the MIT License. For more details, see the [LICENSE](LICENSE) file in the project root.
