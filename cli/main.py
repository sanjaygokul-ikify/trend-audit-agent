import argparse
from packages.core import ModelInterface, ExecutionConfig, Task, LogEntry
from services.orchestrator import OrchestratorService


def main():
    parser = argparse.ArgumentParser(description='Audit Agent CLI')
    parser.add_argument('--model_name', type=str, help='Model name')
    parser.add_argument('--sandbox_enabled', action='store_true', help='Enable sandboxing')
    args = parser.parse_args()

    execution_config = ExecutionConfig(sandbox_enabled=args.sandbox_enabled)
    model_interface = ModelInterface(model_name=args.model_name)
    task = Task()
    orchestrator_service = OrchestratorService(execution_config)
    result = orchestrator_service.schedule_execution(task)
    print(result)

if __name__ == '__main__':
    main()
