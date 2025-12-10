#!/usr/bin/env python3
"""
prompt-runner.py - Generic prompt runner

Runs a prompt template against a file, replacing placeholders.

Usage:
    ./prompt-runner.py <template.md> <file>
    ./prompt-runner.py ../prompts/part2-patterns/code-review.md myfile.py

Placeholders:
    [FILE_CONTENT] - Replaced with the file contents
    [FILE_NAME] - Replaced with the file name
    [LANGUAGE] - Replaced with file extension (or specify with -l)
"""

import argparse
import os
import subprocess
import sys


def get_language_from_extension(filename):
    """Guess language from file extension."""
    ext_map = {
        '.py': 'Python',
        '.js': 'JavaScript',
        '.ts': 'TypeScript',
        '.tsx': 'TypeScript/React',
        '.jsx': 'JavaScript/React',
        '.go': 'Go',
        '.rs': 'Rust',
        '.rb': 'Ruby',
        '.java': 'Java',
        '.c': 'C',
        '.cpp': 'C++',
        '.cs': 'C#',
        '.php': 'PHP',
        '.swift': 'Swift',
        '.kt': 'Kotlin',
        '.sql': 'SQL',
        '.sh': 'Bash',
        '.yaml': 'YAML',
        '.yml': 'YAML',
        '.json': 'JSON',
        '.md': 'Markdown',
    }
    _, ext = os.path.splitext(filename)
    return ext_map.get(ext.lower(), 'unknown')


def main():
    parser = argparse.ArgumentParser(
        description='Run a prompt template against a file'
    )
    parser.add_argument('template', help='Path to prompt template')
    parser.add_argument('file', help='Path to file to process')
    parser.add_argument('-l', '--language', help='Override language detection')
    parser.add_argument('--dry-run', action='store_true',
                       help='Print prompt instead of running')
    args = parser.parse_args()

    # Read template
    if not os.path.exists(args.template):
        print(f"Error: Template '{args.template}' not found", file=sys.stderr)
        sys.exit(1)

    with open(args.template, 'r') as f:
        template = f.read()

    # Read file
    if not os.path.exists(args.file):
        print(f"Error: File '{args.file}' not found", file=sys.stderr)
        sys.exit(1)

    with open(args.file, 'r') as f:
        file_content = f.read()

    # Determine language
    language = args.language or get_language_from_extension(args.file)

    # Replace placeholders
    prompt = template
    prompt = prompt.replace('[FILE_CONTENT]', file_content)
    prompt = prompt.replace('[FILE_NAME]', os.path.basename(args.file))
    prompt = prompt.replace('[LANGUAGE]', language)

    if args.dry_run:
        print(prompt)
        return

    # Get AI CLI from environment
    ai_cli = os.environ.get('AI_CLI')
    if not ai_cli:
        print("Warning: AI_CLI not set. Printing prompt instead.")
        print("-" * 40)
        print(prompt)
        print("-" * 40)
        print("\nSet AI_CLI environment variable to your AI CLI tool.")
        return

    # Run AI CLI
    try:
        result = subprocess.run(
            ai_cli.split(),
            input=prompt,
            text=True,
            capture_output=True
        )
        print(result.stdout)
        if result.stderr:
            print(result.stderr, file=sys.stderr)
    except Exception as e:
        print(f"Error running AI CLI: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
