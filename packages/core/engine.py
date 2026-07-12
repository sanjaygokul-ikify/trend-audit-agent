import logging
import math
from typing import List, Dict, Any
from .types import *
from .exceptions import *

logger = logging.getLogger(__name__)

class InferenceEngine:
    def __init__(self, model_name: str, model_interface: ModelInterface):
        self.model_name = model_name
        self.model_interface = model_interface

    def infer(self, input_data: Any) -> Any:
        try:
            # Load model and perform inference
            model = self.model_interface.load_model(self.model_name)
            result = model.predict(input_data)
            return result
        except Exception as e:
            logger.error(f'Inference failed: {str(e)}')
            raise InferenceException('Inference failed')


class OrchestratorEngine:
    def __init__(self, execution_config: ExecutionConfig):
        self.execution_config = execution_config
        self.sandbox_enabled = execution_config.sandbox_enabled

    def schedule_execution(self, task: Task) -> ExecutionResult:
        try:
            # Schedule task for execution
            if self.sandbox_enabled:
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


class MerkleTree:
    def __init__(self, logs: List[LogEntry]):
        self.logs = logs

    def calculate_root(self) -> str:
        # Calculate Merkle tree root
        if not self.logs:
            return ''
        leaves = [log.hash for log in self.logs]
        while len(leaves) > 1:
            new_leaves = []
            for i in range(0, len(leaves), 2):
                if i + 1 < len(leaves):
                    # Hash two leaves together
                    new_leaf = self.hash_two_leaves(leaves[i], leaves[i + 1])
                    new_leaves.append(new_leaf)
                else:
                    # If there's only one leaf left, use it as is
                    new_leaves.append(leaves[i])
            leaves = new_leaves
        return leaves[0]

    def hash_two_leaves(self, leaf1: str, leaf2: str) -> str:
        # Combine two leaves into a single hash
        combined = leaf1 + leaf2
        return self.hash(combined)

    def hash(self, data: str) -> str:
        # Calculate SHA-256 hash of data
        import hashlib
        return hashlib.sha256(data.encode()).hexdigest()


class AuditLogger:
    def __init__(self, storage: str):
        self.storage = storage

    def store_log(self, log_entry: LogEntry):
        try:
            # Store log entry in storage
            with open(self.storage, 'a') as f:
                f.write(log_entry.to_string() + '\n')
        except Exception as e:
            logger.error(f'Failed to store log: {str(e)}')
            raise LoggingException('Failed to store log')


class VerificationAPI:
    def __init__(self, audit_logger: AuditLogger):
        self.audit_logger = audit_logger

    def query_log(self, log_id: str) -> LogEntry:
        try:
            # Query log entry from storage
            with open(self.audit_logger.storage, 'r') as f:
                logs = [LogEntry.from_string(line) for line in f.readlines()]
                for log in logs:
                    if log.id == log_id:
                        return log
            raise LogNotFoundException('Log not found')
        except Exception as e:
            logger.error(f'Failed to query log: {str(e)}')
            raise QueryException('Failed to query log')
