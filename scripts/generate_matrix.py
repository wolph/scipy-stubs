import json  
import sys  
from packaging.specifiers import SpecifierSet  
from packaging.version import Version  
import requests  
import os  
import tomli  # For Python 3.11+, you can use tomllib instead  
  
def get_pyproject_data():  
    """Reads and returns the data from pyproject.toml."""  
    pyproject_path = os.path.join(os.path.dirname(__file__), "../pyproject.toml")  
    with open(pyproject_path, "rb") as f:  
        pyproject = tomli.load(f)  
    return pyproject  
  
def get_minimum_python_version(pyproject):  
    """Extracts the minimum Python version from pyproject.toml."""  
    requires_python = pyproject["project"]["requires-python"]  
    specifier = SpecifierSet(requires_python)  
    min_python = None  
    for spec in specifier:  
        if spec.operator in (">=", "==", "~=", ">"):  
            version = Version(spec.version)  
            if min_python is None or version > min_python:  
                min_python = version  
    if min_python is None:  
        raise ValueError("Minimum Python version not found in requires-python.")  
    return str(min_python)  
  
def get_minimum_numpy_version(pyproject):  
    """Extracts the minimum NumPy version from pyproject.toml dependencies."""  
    dependencies = pyproject["project"].get("dependencies", [])  
    for dep in dependencies:  
        if dep.startswith("numpy"):  
            specifier_str = dep[len("numpy"):]  
            specifier = SpecifierSet(specifier_str)  
            min_numpy = None  
            for spec in specifier:  
                if spec.operator in (">=", "==", "~=", ">"):  
                    version = Version(spec.version)  
                    if min_numpy is None or version > min_numpy:  
                        min_numpy = version  
            if min_numpy is None:  
                raise ValueError("Minimum NumPy version not found in dependencies.")  
            return str(min_numpy)  
    raise ValueError("NumPy dependency not found in dependencies.")  
  
def get_python_versions(min_version_str):  
    """Generates a list of Python versions based on the minimum version."""  
    # Define the list of Python versions available in GitHub Actions  
    all_python_versions = ["3.9", "3.10", "3.11", "3.12", "3.13"]  
    min_version = Version(min_version_str)  
    python_versions = [v for v in all_python_versions if Version(v) >= min_version]  
    return python_versions  
  
def get_numpy_versions(min_version_str):  
    """Generates a list of NumPy versions starting from the minimum version."""  
    # You can fetch available versions from PyPI if needed  
    # For demonstration, we'll define a list of recent major NumPy versions  
    all_numpy_versions = ["1.21", "1.22", "1.23", "1.24", "1.25"]  
    min_version = Version(min_version_str)  
    numpy_versions = [v for v in all_numpy_versions if Version(v) >= min_version]  
    return numpy_versions  
  
def get_numpy_python_requirements(numpy_version):  
    """Gets the 'Requires-Python' field for a given NumPy version from PyPI."""  
    response = requests.get(f"https://pypi.org/pypi/numpy/{numpy_version}/json")  
    if response.status_code != 200:  
        return None  
    data = response.json()  
    requires_python = data['info'].get('requires_python', '')  
    return requires_python  
  
def is_python_version_compatible(python_version, requires_python_specifier):  
    """Checks if a Python version satisfies a version specifier."""  
    if not requires_python_specifier:  
        return True  
    specifier = SpecifierSet(requires_python_specifier)  
    return Version(python_version) in specifier  
  
def main():  
    pyproject = get_pyproject_data()  
    package_min_python_version = get_minimum_python_version(pyproject)  
    package_min_numpy_version = get_minimum_numpy_version(pyproject)  
  
    python_versions = get_python_versions(package_min_python_version)  
    numpy_versions = get_numpy_versions(package_min_numpy_version)  
  
    # Get 'Requires-Python' for each NumPy version  
    numpy_python_requirements = {}  
    for numpy_version in numpy_versions:  
        requires_python = get_numpy_python_requirements(numpy_version)  
        numpy_python_requirements[numpy_version] = requires_python  
  
    matrix = {"include": []}  
  
    for py_ver in python_versions:  
        for np_ver in numpy_versions:  
            np_requires_python = numpy_python_requirements.get(np_ver)  
            if np_requires_python is None:  
                continue  # Skip if we can't get requires_python for this NumPy version  
            if is_python_version_compatible(py_ver, np_requires_python):  
                # Add this combination to the matrix  
                matrix["include"].append({  
                    "python-version": py_ver,  
                    "numpy-version": np_ver  
                })  
  
    # Output the matrix as JSON  
    json.dump(matrix, sys.stdout)  
  
if __name__ == "__main__":  
    main()  
