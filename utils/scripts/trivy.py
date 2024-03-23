import os
import subprocess  # nosec # only executed in development


def create_trivy_report():
    os.makedirs("target/", exist_ok=True)
    os.chdir("target/")
    subprocess.run(  # nosec # only executed in development
        [
            "trivy",
            "fs",
            "--scanners",
            "vuln,secret,misconfig",
            "-f",
            "template",
            "-t",
            "@../utils/trivy/html.tpl",
            "-o",
            "trivy-report.html",
            "../",
        ]
    )
    print("Trivy report created.")


if __name__ == "__main__":
    create_trivy_report()
