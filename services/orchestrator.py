from packages.core import OrchestratorEngine, ExecutionConfig, Task
from packages.core.exceptions import ExecutionException


class OrchestratorService:
    def __init__(self, execution_config: ExecutionConfig):
        self.orchestrator_engine = OrchestratorEngine(execution_config)

    def schedule_execution(self, task: Task) -> ExecutionResult:
        try:
            result = self.orchestrator_engine.schedule_execution(task)
            return result
        except Exception as e:
            # Handle the exception
            raise ExecutionException(str(e))
