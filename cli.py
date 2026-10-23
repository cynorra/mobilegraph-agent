import argparse
import sys
import os
from mobilegraph.graphify import build_code_graph
from mobilegraph.security import run_security_audit


def main():
    parser = argparse.ArgumentParser(
        prog="mobilegraph",
        description="MobileGraph-Agent: Autonomous AST Graph Refactor & Security CLI"
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Command: graphify
    graph_parser = subparsers.add_parser("graphify", help="Extract AST Knowledge Graph from mobile codebase")
    graph_parser.add_argument("target", help="Path to Flutter/Android project directory")
    graph_parser.add_argument("--out", default="graph_index.json", help="Output path for graph index JSON")

    # Command: audit
    audit_parser = subparsers.add_parser("audit", help="Run static security and vulnerability scanner")
    audit_parser.add_argument("target", help="Path to project directory")
    audit_parser.add_argument("--security", action="store_true", default=True, help="Scan secrets and intent risks")

    # Command: check
    check_parser = subparsers.add_parser("check", help="Run full pipeline: graph indexing and security audit")
    check_parser.add_argument("target", help="Path to project directory")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(0)

    target_dir = os.path.abspath(args.target)
    if not os.path.exists(target_dir):
        print(f"[MobileGraph Error] Target directory does not exist: {target_dir}")
        sys.exit(1)

    if args.command == "graphify":
        build_code_graph(target_dir, args.out)
    elif args.command == "audit":
        run_security_audit(target_dir)
    elif args.command == "check":
        print(f"[MobileGraph] Running full diagnostic check on {target_dir}")
        build_code_graph(target_dir)
        run_security_audit(target_dir)


if __name__ == "__main__":
    main()
