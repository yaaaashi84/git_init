class WithSample02:
    def __enter__(self):
        print("===== Enter!!! =====")
        return "Bob"

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("===== Exit!!! =====")


if __name__ == "__main__":
    with WithSample02() as s2:
        print(s2)