from . import translator


def main(detailed_logging=False):
    try:
        translator_instance = translator.Translator(detailed_logging=detailed_logging)
        translator_instance.run()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
