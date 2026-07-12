import logging
from typing import Any
from . import *

logger = logging.getLogger(__name__)

class Executor:
    def __init__(self, execution_config: ExecutionConfig):
        self.execution_config = execution_config

    def execute(self, task: Task) -> ExecutionResult:
        try:
            # Execute task
            if self.execution_config.sandbox_enabled:
                # Create sandboxed environment for execution
                sandbox = Sandbox()
                result = sandbox.execute(task)
            else:
                # Execute task in non-sandboxed environment
                result = task.execute()
            return ExecutionResult(result)
        except Exception as e:
            logger.error(f'Execution failed: {str(e)}')
            raise ExecutionException('Execution failed')
