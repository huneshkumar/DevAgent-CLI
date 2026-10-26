
import argparse

from dotenv import load_dotenv

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
    except Exception as error:
        print(f"Error: {error}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
