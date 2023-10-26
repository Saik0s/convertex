# Convertex

Convertex is a utility tool for transforming any kind of text based on user-defined prompts.

## Installation

Run the following commands to install Convertex:

```bash
make install
```

## Usage

To add a new prompt:

```bash
python main.py add_prompt 'current content' 'desired content' 'additional info' 'prompt name'
```

To transform content based on a prompt:

```bash
python main.py transform_content 'prompt name' 'current content'
```

To list all available prompts:

```bash
python main.py list_prompts
```

## Testing

To run the tests:

```bash
make test
```
