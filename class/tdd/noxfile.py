import platform
import nox

@nox.session(python=[platform.python_version()])
def tests(session):
    # old variant without --cov:
    # session.run("pytest", external=True)

    args = session.posargs or ["--cov"]
    session.install("pytest", "pytest-cov")
    session.run("pytest", *args)

# How to run the program?
# nox -- unit_test.py