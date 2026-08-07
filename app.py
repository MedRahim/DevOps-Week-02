#!/usr/bin/env python3
"""Sample app for DevOps Week 2 Git practice."""

APP_VERSION = "0.2.0"


def greet(name: str = "DevOps team") -> str:
    return f"Hello, {name}!"


def main():
    print(f"DevOps Week 02 sample app v{APP_VERSION}")
    print(greet())
    print("Git + GitHub collaboration demo")


if __name__ == "__main__":
    main()
