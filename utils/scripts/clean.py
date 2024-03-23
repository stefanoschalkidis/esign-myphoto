import shutil


def remove_build_dirs():
    try:
        shutil.rmtree("build/")
    except FileNotFoundError:
        pass

    try:
        shutil.rmtree("dist/")
    except FileNotFoundError:
        pass

    try:
        shutil.rmtree("target/")
    except FileNotFoundError:
        pass


if __name__ == "__main__":
    remove_build_dirs()
