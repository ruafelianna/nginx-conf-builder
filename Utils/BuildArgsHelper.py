from enum import Enum
from typing import Any

class BuildArgsHelper:
    @staticmethod
    def value_or_empty(
        value : Any | None,
    ) -> str:
        return "" if value is None else str(value)

    @staticmethod
    def add_bool(
        args: list[str],
        name: str,
        condition: bool,
    ) -> None:
        if condition:
            args.append(name)

    @staticmethod
    def add_enum(
        args: list[str],
        name: str,
        value: Enum | None,
    ) -> None:
        if value is not None:
            args.append(f"{name}={value.name}")

    @staticmethod
    def add_enum_value(
        args: list[str],
        enum: Enum | None,
    ) -> None:
        if enum is not None:
            args.append(enum.value)

    @staticmethod
    def add_str(
        args: list[str],
        value: str | None,
    ) -> None:
        if value is not None:
            args.append(value)

    @staticmethod
    def add_value(
        args: list[str],
        name: str,
        value: Any | None,
    ) -> None:
        if value is not None:
            args.append(f"{name}={value}")
