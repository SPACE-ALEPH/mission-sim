import sys
import pathlib
import importlib.util

def run():
    base = pathlib.Path(__file__).parent
    tests_dir = base / "tests"

    # Add repo root to path so imports work when running from root.
    sys.path.insert(0, str(base / "src"))
    sys.path.insert(0, str(base))

    failed = 0
    for test_file in sorted(tests_dir.glob("test_*.py")):
        spec = importlib.util.spec_from_file_location(test_file.stem, test_file)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        # Run any function starting with test.
        for name in dir(module):
            if name.startswith("test_"):
                fn = getattr(module, name)
                try:
                    fn()
                except Exception as e:
                    failed += 1
                    print(f"[FAIL] {test_file.name}::{name} -> {e}")
                else:
                    print(f"[PASS] {test_file.name}::{name}")

    print("")
    if failed:
        print(f"Tests failed: {failed}")
        sys.exit(1)
    print("All tests passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(run())
