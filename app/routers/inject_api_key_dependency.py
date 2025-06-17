import os
import re

ROUTERS_DIR = "./app/routers"  # ajustează calea

DEPENDENCY_SNIPPET = "dependencies=[Depends(verify_api_key)]"

# Regex care detectează decoratorul router, fără dependencies sau cu dependencies dar fără verify_api_key
ROUTER_DECORATOR_RE = re.compile(
    r"(@router\.(get|post|put|delete|patch)\([^)]*)\)", re.MULTILINE
)

def already_has_dependency(decorator_text):
    return DEPENDENCY_SNIPPET in decorator_text

def add_dependency(decorator_text):
    if "dependencies=" in decorator_text:
        # Adaugă verify_api_key în lista existentă
        # Ex: dependencies=[...], îl vom insera în interiorul listei
        return re.sub(r"dependencies=\[(.*?)\]", 
                      lambda m: f"dependencies=[Depends(verify_api_key), {m.group(1)}]", 
                      decorator_text)
    else:
        # Pur și simplu adaugă dependencies
        return decorator_text[:-1] + f", {DEPENDENCY_SNIPPET})"

def process_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    modified = False

    def replacer(match):
        nonlocal modified
        decorator = match.group(1) + ")"
        if already_has_dependency(decorator):
            return decorator
        modified = True
        new_decorator = add_dependency(decorator)
        return new_decorator

    new_content = ROUTER_DECORATOR_RE.sub(replacer, content)

    if modified:
        print(f"Updated dependencies in {filepath}")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)

def main():
    for root, _, files in os.walk(ROUTERS_DIR):
        for file in files:
            if file.endswith(".py"):
                process_file(os.path.join(root, file))

if __name__ == "__main__":
    main()
