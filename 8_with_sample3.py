class WithSample03:
    def __init__(self, file_path):
        self.file_path = file_path

    def __enter__(self):
        print("===== Enter!!! =====")
        return open(self.file_path, mode="r")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("===== Exit!!! =====")


if __name__ == "__main__":
    with WithSample03(file_path="users.csv") as s3:
        print(s3.read())
