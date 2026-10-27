import argparse

from dotenv import load_dotenv
from openai import (
    APIConnectionError,
    APIStatusError,
    AuthenticationError,
    RateLimitError,
)

from devagent.providers import ask_llm


def main():
    load_dotenv()

    parser = argparse.ArgumentParser(
        description="DevAgent: a multi-LLM terminal assistant"
    )

    parser.add_argument(
        "--provider",
        choices=["deepseek", "openai"],
        default="deepseek",
        help="LLM provider to use",
    )

    parser.add_argument(
        "prompt",
        help="Your question or instruction",
    )

    args = parser.parse_args()

    try:
        answer = ask_llm(args.provider, args.prompt)

        print(f"\nDevAgent ({args.provider}):\n")
        print(answer)

    except ValueError as error:
        print(f"Configuration error: {error}")
        raise SystemExit(1)

    except AuthenticationError:
        print("Authentication failed. Check your API key.")
        raise SystemExit(1)

    except RateLimitError:
        print("Rate limit reached. Check your API usage and limits.")
        raise SystemExit(1)

    except APIConnectionError:
        print("Could not connect to the API. Check your internet connection.")
        raise SystemExit(1)

    except APIStatusError as error:
        print(f"API error: HTTP {error.status_code}")
        print(f"Details: {error.message}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()