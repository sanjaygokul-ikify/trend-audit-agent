from dataclasses import dataclass
from typing import Any

@dataclass
class ModelInterface:
    model_name: str

    def load_model(self, model_name: str) -> Any:
        # Load model implementation
        pass

@dataclass
class ExecutionConfig:
    sandbox_enabled: bool

@dataclass
class Task:
    def execute(self) -> Any:
        # Task execution logic
        pass

@dataclass
class ExecutionResult:
    result: Any

@dataclass
class LogEntry:
    id: str
    data: Any

    def to_string(self) -> str:
        return f"{self.id}:{self.data}"

    @classmethod
    def from_string(cls, string: str) -> 'LogEntry':
        id, data = string.split(':')
        return cls(id, data)

@dataclass
class Sandbox:
    def execute(self, task: Task) -> Any:
        # Sandbox execution logic
        return task.execute()